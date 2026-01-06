# NEW: Import from langchain_core and langchain_openai
from langchain_core.prompts import PromptTemplate 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_scout_report(player_name, stats):
    # Initialize the LLM (GenAI)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    template = """
    You are an expert Football Scout. Analyze this player: {player_name}
    Stats context: {stats}
    
    Provide a professional scouting report including:
    1. Tactical Fit and Playing Style.
    2. Predicted Potential based on xG performance.
    3. Final Recommendation (Sign, Scout further, or Pass).
    """
    
    prompt = PromptTemplate(input_variables=["player_name", "stats"], template=template)
    
    # Modern LangChain LCEL syntax
    chain = prompt | llm
    response = chain.invoke({"player_name": player_name, "stats": stats})
    return response.content