from fastmcp import FastMCP

mcp = FastMCP("research-prompt")

@mcp.prompt()
def get_research_prompt(topic: str) -> str:
    """
    Get a research prompt for a given topic.
    """
    return f"Research the topic: {topic}"




if __name__ == "__main__":
    # print(get_research_prompt.__doc__)
    # print(get_research_prompt.fn.__doc__)
    # mcp.run(transport="http") # Log -> ERROR:    Cancel 0 running task(s), timeout graceful shutdown exceeded
    mcp.run(transport="stdio")
