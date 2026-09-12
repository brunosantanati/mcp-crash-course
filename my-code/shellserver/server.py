import asyncio
import json
from typing import Any, Dict, List

import anyio

try:
	# MCP Python SDK
	from mcp.server import Server
	from mcp.server.stdio import stdio_server
	from mcp.types import Tool
except Exception as exc:  # pragma: no cover
	raise SystemExit(
		"The 'mcp' Python package is required. Install with: pip install mcp"
	) from exc


SERVER_NAME = "shellserver"
MAX_OUTPUT_BYTES = 200_000  # avoid flooding the client


server = Server(SERVER_NAME)


@server.list_tools()
async def handle_list_tools() -> List[Tool]:
	"""Expose the single 'terminal' tool with a simple JSON schema."""
	return [
		Tool(
			name="terminal",
			description="Run a shell command on the host and return stdout/stderr.",
			input_schema={
				"type": "object",
				"properties": {
					"command": {"type": "string", "description": "Shell command to execute"},
					"timeout": {
						"type": "number",
						"minimum": 0,
						"description": "Optional timeout in seconds (default 30)",
					},
				},
				"required": ["command"],
			},
		)
	]


async def _run_command(command: str, timeout: float) -> Dict[str, Any]:
	"""Run a shell command with timeout, return result dict.

	The result contains: { returncode, stdout, stderr, truncated }.
	"""
	process = await asyncio.create_subprocess_shell(
		command,
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE,
	)

	try:
		stdout_bytes, stderr_bytes = await asyncio.wait_for(process.communicate(), timeout)
	except asyncio.TimeoutError:
		process.kill()
		await process.wait()
		return {
			"returncode": None,
			"stdout": "",
			"stderr": f"Command timed out after {timeout} seconds",
			"truncated": False,
		}

	# Truncate outputs if too large
	truncated = False
	if len(stdout_bytes) + len(stderr_bytes) > MAX_OUTPUT_BYTES:
		truncated = True
		budget = MAX_OUTPUT_BYTES // 2
		stdout_bytes = stdout_bytes[:budget]
		stderr_bytes = stderr_bytes[:budget]

	return {
		"returncode": process.returncode,
		"stdout": stdout_bytes.decode(errors="replace"),
		"stderr": stderr_bytes.decode(errors="replace"),
		"truncated": truncated,
	}


@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
	"""Handle tool invocation for 'terminal'."""
	if name != "terminal":
		return [
			{"type": "text", "text": f"Unknown tool: {name}"},
		]

	command = str(arguments.get("command", "")).strip()
	if not command:
		return [
			{"type": "text", "text": "Missing required argument: command"},
		]

	timeout = float(arguments.get("timeout", 30))
	result = await _run_command(command, timeout)

	summary = {
		"command": command,
		"returncode": result["returncode"],
		"truncated": result["truncated"],
	}

	# Return two text parts: JSON summary and combined output
	combined = "".join(
		part
		for part in (
			result["stdout"],
			"\n" if result["stdout"] and result["stderr"] else "",
			result["stderr"],
		)
	)

	return [
		{"type": "text", "text": json.dumps(summary, ensure_ascii=False, indent=2)},
		{"type": "text", "text": combined or "(no output)"},
	]


async def _main() -> None:
	"""Run the MCP server over stdio."""
	async with stdio_server() as (read_stream, write_stream):
		await server.run(read_stream, write_stream)


if __name__ == "__main__":
	anyio.run(_main)
