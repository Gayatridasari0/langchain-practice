import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

SERVERS = {
    "math": {
        "transport":"stdio",
        "command": r"c:\Users\Gayatri_dasari\OneDrive\Desktop\langgraph projects\.venv\Scripts\python.exe",
        "args": ["math-server.py"]
    },
    "expense": {
            "transport": "stdio",
            "command": r"c:\Users\Gayatri_dasari\OneDrive\Desktop\langgraph projects\.venv\Scripts\python.exe",
            "args": ["expense-server.py"],
        }
}

async def main():
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()

    named_tools = {}
    for tool in tools:
        named_tools[tool.name] = tool

    print("Available tools:", named_tools.keys())

    llm = ChatGroq(model="llama-3.1-8b-instant")
    llm_with_tools = llm.bind_tools(tools)

    prompt = "Addition of 2 and 3"
    response = await llm_with_tools.ainvoke(prompt)

    if not getattr(response, "tool_calls", None):
        print("\nLLM Reply:", response.content)
        return
    tool_messages = []
    for tc in response.tool_calls:
        selected_tool = tc['name']
        selected_tool_args = tc.get("args") or {}
        selected_tool_id = tc["id"]

        result = await named_tools[selected_tool].ainvoke(selected_tool_args)
        tool_messages.append(ToolMessage(tool_call_id=selected_tool_id, content=json.dumps(result)))

    final_response = await llm_with_tools.ainvoke(
    [HumanMessage(content=prompt), response, *tool_messages])
    print(f"Final response: {final_response.content}")

if __name__ == "__main__":
    asyncio.run(main())
