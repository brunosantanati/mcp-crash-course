### [MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/)  

#### Links

[Discord](https://discord.com/invite/SP2cz4JcGg)  
[weather-server-typescript](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)  
[Cursor / MCP](https://cursor.com/docs/context/mcp)  
[Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server)  

#### Sample of a mcp.json (Cursor file to configure MCP servers)
```json
{
  "mcpServers": {
    "weather": {
      "command": "/home/anyuser/.nvm/versions/node/v20.11.0/bin/node",
      "args": [
        "/home/anyuser/quickstart-resources/weather-server-typescript/build/index.js"
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
      "args": [
        "/home/anyuser/quickstart-resources/weather-server-typescript/build/index.js"
      ]
    }
  }
}
```
