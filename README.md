### [MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/)  

### Links

[Discord](https://discord.com/invite/SP2cz4JcGg)  
[weather-server-typescript](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)  
[Cursor / MCP](https://cursor.com/docs/context/mcp)  

### Sample of a mcp.json (Cursor file to configure MCP servers)
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
