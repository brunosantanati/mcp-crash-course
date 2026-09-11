### [MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/)  

#### :information_source: Links

- [Discord](https://discord.com/invite/SP2cz4JcGg)  
- [weather-server-typescript](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)  
- [Cursor / MCP](https://cursor.com/docs/context/mcp)  
- [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)  
- [Core architecture- official Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/learn/architecture)  
- [MCP Spec- Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)  
- [Running MCP Servers with Transports- FastMCP 2.0](https://gofastmcp.com/servers/server#running-the-server)  
- [Server (Low Level)](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/lowlevel/server.py)  
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/fastmcp/server.py)  
- [FastMCP 2.0](https://gofastmcp.com/getting-started/welcome)  
- [MCP Inspector Official Docs](https://modelcontextprotocol.io/docs/tools/inspector)  
- [MCP Inspector Github Repository Open Source](https://github.com/modelcontextprotocol/inspector)  
- [LangChain LLM.txt](https://langchain-ai.github.io/langgraph/llms-txt-overview/)  
- [mcpdoc Github Repo](https://github.com/langchain-ai/mcpdoc)  
- [MCP Crash Course Github Repository](https://github.com/emarco177/mcp-crash-course)  
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)  
- [MCP Docs](https://modelcontextprotocol.io/docs/getting-started/intro)  
- [Cursor rules for Python](https://cursor.directory/rules/python)  
- [hacked.txt](https://gist.githubusercontent.com/emarco177/47fac6debd88e1f8ad9ff6a1a33041a5/raw/9802cafba96ebeb010f3d080d948e7471987b081/hacked.txt)  
- [OWASP Top 10 for Large Language Model Applications](https://owasp.github.io/www-project-top-10-for-large-language-model-applications/)  
- [The Model Context Protocol: Simplifying Building AI apps with Anthropic Claude Desktop and Docker](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)  

#### :information_source: Sample of a mcp.json (Cursor file to configure MCP servers)
The file should be located in `~/.cursor/mcp.json`
```json
{
  "mcpServers": {
    "weather": {
      "command": "/home/anyuser/.nvm/versions/node/v20.11.0/bin/node",
      "args": [
        "/home/anyuser/path-to/quickstart-resources/weather-server-typescript/build/index.js"
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
        "--directory", "/home/anyuser/path-to/shellserver", "run", "server.py"
      ]
    }
  }
}
```
#### :information_source: Sample of a Claude Desktop file to configure MCP servers
The file should be located in a path such as `~/Library/Application\ Support/Claude/claude_desktop_config.json` (or in my case `/home/bruno/.config/Claude/claude_desktop_config.json`)  

##### Sample for a Python MCP server  
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/path-to/quickstart-resources/weather-server-python",
        "run",
        "weather.py"
      ]
    }
  }
}
```

##### Sample for a Typescript MCP server  
```json
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/path-to/quickstart-resources/weather-server-typescript/build/index.js"]
    }
  }
}
```

##### Entire file content
```json
{
  "coworkUserFilesPath": "/home/anyuser/Claude",
  "preferences": {
    ...
  },
  "mcpServers": {
    "weather": {
      "command": "/home/anyuser/.nvm/versions/node/v20.11.0/bin/node",
      "args": [
        "/home/anyuser/path-to/quickstart-resources/weather-server-typescript/build/index.js"
      ]
    },
    "langgraph-docs-mcp": {
      "command": "/snap/bin/uvx",
      "args": [
      	"--with",
    	"mcp<2",
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
        "--directory",
        "/home/anyuser/path-to/mcp-crash-course/original-files/mcp-crash-course",
        "run",
        "server.py"
      ]
    }
  }
}
```

##### Connecting to a dockerized MCP Server
```json
  "mcpServers": {
    "docker-shell": {
      "command": "docker",
      "args": ["run", "-i",  "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "shellserver-app"]
    }
  }
```

##### :warning: Important Note
Close Claude Desktop and run `pkill -f claude` after changing the file, in order to apply changes and enable MCP Servers.

#### :information_source: Commands used

##### Install mcpdoc and test it using inspector
```sh
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
```

##### Create a new project (MCP server)
```sh
uv init shellserver
cd shellserver/
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
touch server.py
rm main.py
cursor .
uv run server.py
```

##### Additional commands
```sh
Deactivate virtual environment:
deactivate
```

##### Prompt for terminal tool
```
Note: before you run this prompt you should import the MCP documentation and MCP Python SDK to be indexed by Cursor, and then you will be able to tag these documentations in your prompt.

I want you to implement me a simple MCP Server from @MCP documentation . Use the Python SDK @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple.
```

##### Dockerize shellserver project
Run it in the folder `mcp-crash-course/original-files/mcp-crash-course`:
```sh
docker build -t shellserver-app .
docker run -it --rm shellserver-app
docker logs bfccac040a8a
docker kill bfccac040a8a
```