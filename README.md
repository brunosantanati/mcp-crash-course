### [MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/)  

#### Links

[Discord](https://discord.com/invite/SP2cz4JcGg)  
[weather-server-typescript](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)  
[Cursor / MCP](https://cursor.com/docs/context/mcp)  
[Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)  
[Core architecture- official Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/learn/architecture)  
[MCP Spec- Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)  
[Running MCP Servers with Transports- FastMCP 2.0](https://gofastmcp.com/servers/server#running-the-server)  
[Server (Low Level)](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/lowlevel/server.py)  
[FastMCP](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/fastmcp/server.py)  
[FastMCP 2.0](https://gofastmcp.com/getting-started/welcome)  
[MCP Inspector Official Docs](https://modelcontextprotocol.io/docs/tools/inspector)  
[MCP Inspector Github Repository Open Source](https://github.com/modelcontextprotocol/inspector)  
[LangChain LLM.txt](https://langchain-ai.github.io/langgraph/llms-txt-overview/)  
[mcpdoc Github Repo](https://github.com/langchain-ai/mcpdoc)  
[MCP Crash Course Github Repository](https://github.com/emarco177/mcp-crash-course)  
[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)  
[MCP Docs](https://modelcontextprotocol.io/docs/getting-started/intro)  
[Cursor rules for Python](https://cursor.directory/rules/python)  

#### Sample of a mcp.json (Cursor file to configure MCP servers)
The file should be located in ~/.cursor/mcp.json
```json
{
  "mcpServers": {
    "weather": {
      "command": "/home/anyuser/.nvm/versions/node/v20.11.0/bin/node",
      "args": [
        "/home/anyuser/quickstart-resources/weather-server-typescript/build/index.js"
      ]
    },
    "langgraph-docs-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "mcpdoc",
        "mcpdoc",
        "--urls",
        "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt LangChain:https://python.langchain.com/llms.txt",
        "--transport",
        "stdio"
      ]
    },
    "shell": {
      "command": "/snap/bin/uv",
      "args": [
        "--directory", "/home/anyuser/shellserver", "run", "server.py"
      ]
    }
  }
}
```
#### Sample of a Claude Desktop file to configure MCP servers
The file should be located in a path such as `~/Library/Application\ Support/Claude/claude_desktop_config.json`  

- Sample for a Python MCP server  
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

- Sample for a Typescript MCP server  
```json
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js"]
    }
  }
}
```
#### Commands used
```
- INSTALL MCPDOC AND TEST IT USING INSPECTOR
sudo snap install astral-uv --classic
uv venv
source .venv/bin/activate
uv pip install .
which uv

uvx --from mcpdoc mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost

nvm list
nvm use 20.11.0

npx @modelcontextprotocol/inspector

- CREATE A NEW PROJECT (MCP SERVER)
uv init shellserver
cd shellserver/
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
touch server.py
rm main.py
cursor .
uv run server.py

- ADDITIONAL COMMANDS
Deactivate virtual environment:
deactivate

- PROMPT FOR TERMINAL TOOL
Note: before you run this prompt you should import the MCP documentation and MCP Python SDK to be indexed by Cursor, and then you will be able to tag these documentations in your prompt.

I want you to implement me a simple MCP Server from @MCP documentation . Use the Python SDK @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple.
```
