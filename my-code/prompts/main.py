from fastmcp import FastMCP

mcp = FastMCP("research-prompt")

@mcp.prompt()
def get_research_prompt(topic: str) -> str:
    """
    Get a research prompt for a given topic.
    """
    return f"Research the topic: {topic}"




if __name__ == "__main__":
    # Print the docstring
    # print(get_research_prompt.__doc__)
    # print(get_research_prompt.fn.__doc__)

    # mcp.run(transport="stdio") # Integrate with Claud Desktop
    mcp.run(transport="http") # Test with Inspector

    # I had to use Node 22 in order to execute the Inspector:
    # nvm install 22
    # nvm use 22
    # npx -y @modelcontextprotocol/inspector
