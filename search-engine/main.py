from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
# - A tool is any function that an agent can execute
# - We can use a tool to call an API or search in a database
# The simplest way to create a tool is with th @tool decorator. By default, the function's docstring
# becomes the tool's description that helps the model understand when to use it.
from langchain_core.messages import HumanMessage
# from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
# from langchain_openai import ChatOpenAI



@tool
def search(query: str) -> str :
    """
    Tool that searches over the internet
    Args :
        query : The query to search for
    Returns :
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

# llm = ChatGroq(temperature=0, model="llama-3.3-70b-versatile")
llm = ChatOllama(temperature=0, model="qwen3:8b")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from search-engine!")
    result = agent.invoke({"messages":[HumanMessage(content="What is the weather in tokyo")]})
    print(result)


if __name__ == "__main__":
    main()
