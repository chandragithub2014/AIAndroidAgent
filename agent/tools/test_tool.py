from agents import function_tool

@function_tool
def test_tool(message: str = "test") -> str:
    print("TEST TOOL CALLED")
    return f"SUCCESS: {message}"