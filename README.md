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
- [FastMCP 2.0 Docs](https://gofastmcp.com/getting-started/welcome)  
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
- [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
- [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)
- [Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)
- [GPT Researcher Prompt Example](https://github.com/assafelovic/gptr-mcp/blob/master/server.py#L258)
- [FastMCP Prompts](https://gofastmcp.com/servers/prompts)
- [FastMCP Resources & Templates](https://gofastmcp.com/servers/resources)
- [Claude Code - Setup and access Advanced setup](https://code.claude.com/docs/en/setup)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [Search MCP Servers](https://glama.ai/mcp/servers)
- [playwright-mcp](https://github.com/microsoft/playwright-mcp)
- [Cloudflare AI](https://github.com/cloudflare/ai)
- [TODOs API GitHub Code](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-auth0/todos-api/src/index.ts)
- [Middleware GitHub Code](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-auth0/todos-api/src/middlewares/jwt.ts)
- [Secure and Deploy Remote MCP Servers with Auth0 and Cloudflare](https://auth0.com/blog/secure-and-deploy-remote-mcp-servers-with-auth0-and-cloudflare/)
- [Validate JSON Web Tokens](https://auth0.com/docs/secure/tokens/json-web-tokens/validate-json-web-tokens)
- [What Is JWT and Why Should You Use JWT](https://www.youtube.com/watch?v=7Q17ubqLfaM&t=176s)
- [OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)
- [.well-known/oauth-authorization-server](https://www.perplexity.ai/search/47350c91-7daf-4388-8fc3-3a77f745cca3)
- [oauth /register](https://www.perplexity.ai/search/47350c91-7daf-4388-8fc3-3a77f745cca3#1)
- [Cloudflare Workers AI LLM Playground](https://playground.ai.cloudflare.com/)
- [mcp-remote NPM package](https://www.npmjs.com/package/mcp-remote)
- [Agent2Agent Protocol (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [FastMCP 2.0 Github Repository](https://github.com/PrefectHQ/fastmcp)

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
    },
    "research-prompt-mcp": {
      "command": "/home/anyuser/path-to/mcp-crash-course/my-code/prompts/.venv/bin/python3",
      "args": [
        "/home/anyuser/path-to/mcp-crash-course/my-code/prompts/main.py"
      ]
    },
    "pokemon": {
      "command": "/snap/bin/uv",
      "args": ["--directory", "/home/anyuser/path-to/mcp-crash-course/my-code/resources", "run", "main.py"]
    },
    "playwright": {
      "command": "/home/anyuser/.nvm/versions/node/v22.23.2/bin/npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ],
      "env": {
        "PATH": "/home/anyuser/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin"
      }
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

##### Create a new project shellserver (MCP server)
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
Run it in the folder `mcp-crash-course/original-files/shellserver`:
```sh
docker build -t shellserver-app .
docker run -it --rm shellserver-app
docker logs <CONTAINER_ID>
docker logs <CONTAINER_ID> --follow
docker kill <CONTAINER_ID>
docker exec -it <CONTAINER_ID> sh
```

##### Create the project langchain-mcp-adapters
```sh
# it was created from the original repo' main branch
git checkout --orphan project/langchain-mcp-adapters
git rm -rf .
uv init
uv venv
source .venv/bin/activate
uv add langchain-mcp-adapters langgraph langchain-openai
uv add python-dotenv
git add .
# Alternative commands to clone the resulting state:
git clone -b project/langchain-mcp-adapters https://github.com/emarco177/mcp-crash-course.git
cd langchain-mcp-adapters
git checkout f3567e5babb9bc91e8406d41ee82f2331f5641fe

# Run servers
uv run servers/math_server.py
uv run servers/weather_server.py

# Run main program
uv run main.py
```

##### Integrate Claude Code with a MCP Server
```sh
# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Add a MCP Server
claude mcp list
claude mcp add -t http pokemon http://127.0.0.1:8000/mcp/
claude mcp get pokemon

# Use the MCP Server
claude
# Inside Claude Code we can ask these questions to use the MCP Server
# > which mcps do you have?
# > can you use the pokemon starters?
# > get me the pokemon 25
# > get me all fire pokemons
# > get me info about charizard
# > get me info about mewtwo
```

##### Run the sse project
```sh
uv run servers/math_server.py
uv run servers/weather_server.py
uv run langchain_client.py
```