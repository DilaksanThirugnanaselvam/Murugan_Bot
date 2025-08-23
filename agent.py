import os

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

from rag import create_rag_chain, rag_tool


def create_agent(groq_api_key: str) -> AgentExecutor:
    """Create an AI agent for Murugan Bot with RAG + Web Search capabilities."""
    try:
        # Initialize RAG chain
        rag_chain = create_rag_chain(groq_api_key)

        # Tools
        rag_tool_instance = Tool(
            name="Murugan_Knowledge_Base",
            func=lambda query: rag_tool(query, rag_chain),
            description=(
                "Use this to get information about Lord Murugan, his mythology, "
                "temples, festivals, and Tamil diaspora worship "
                "(e.g., Thamizh Muppattan, Eezham Thamizh)."
            ),
        )

        search_tool = DuckDuckGoSearchRun()
        tools = [rag_tool_instance, search_tool]

        # LLM setup
        llm = ChatGroq(
            groq_api_key=groq_api_key, model="openai/gpt-oss-20b", temperature=0
        )

        # Agent Prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are Murugan Bot, an expert on Lord Murugan (முருகன்). "
                    "Use the Murugan Knowledge Base for specific queries about Murugan, "
                    "including Thamizh Muppattan (தமிழ் முப்பாட்டன்) and "
                    "Eezham Thamizh Muruga Valipadu (ஈழத் தமிழ் முருக வழிபாடு). "
                    "Use web search for general or real-time info. "
                    "Answer clearly, incorporating Tamil terms where appropriate.",
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        # Create Agent
        agent = create_tool_calling_agent(llm, tools, prompt)

        # Return Executor
        return AgentExecutor(agent=agent, tools=tools, verbose=True)

    except Exception as e:
        raise Exception(f"Error creating agent: {str(e)}")


if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        print("Error: GROQ_API_KEY not found in .env file.")
        exit(1)

    # Initialize agent and run a test query
    try:
        agent_executor = create_agent(groq_api_key)

        # Test query
        test_query = "How do Eelam Tamils worship Murugan?"
        print(f"Testing query: {test_query}")

        response = agent_executor.invoke({"input": test_query, "chat_history": []})

        print(f"Response: {response['output']}")

    except Exception as e:
        print(f"Error running agent: {str(e)}")
