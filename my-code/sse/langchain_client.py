import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

math_server_path = os.getenv("MATH_SERVER_PATH")
if not math_server_path:
    raise ValueError("MATH_SERVER_PATH environment variable is not set.")

llm = ChatOpenAI()

async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    math_server_path
                ],
            },
            "weather": {
                "url": "http://0.0.0.0:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        tools = client.get_tools()
        # print(tools)
        agent = create_react_agent(llm, tools)
        # result = await agent.ainvoke({"messages": "What is 2 + 2?"})
        result = await agent.ainvoke(
            {"messages": "What is the weather in San Francisco?"}
        )

        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
