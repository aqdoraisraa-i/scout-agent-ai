from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def get_scout_report(player_name, stats):
    # In 2026, 2.5-flash is the stable free-tier model
    # Switching to this removes the 404 error
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )
    
    template = """
    You are an expert Football Scout. Analyze this player: {player_name}
    Stats context: {stats}
    
    Provide a professional scouting report including:
    1. Tactical Fit and Playing Style.
    2. Predicted Potential based on performance.
    3. Final Recommendation (Sign, Scout further, or Pass).
    """
    
    prompt = PromptTemplate(input_variables=["player_name", "stats"], template=template)
    chain = prompt | llm
    
    try:
        response = chain.invoke({"player_name": player_name, "stats": stats})
        return response.content
    except Exception as e:
        # This will catch if there are still regional or key issues
        return f"⚠️ AI Service Error: {str(e)}"