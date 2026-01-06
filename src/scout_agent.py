import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def get_scout_report(player_name, technical_dossier):
    # Initializing Gemini 2.0 Flash for high-speed technical analysis
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", 
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.1 # Strictly factual focus
    )
    
    template = """
    ROLE: Chief Technical Scout & Data Analyst.
    CONTEXT: Finalizing the 2024-2025 Season Evaluation for {player_name}.
    TECHNICAL DATA: {technical_dossier}

    Provide a high-density, professional scouting report. Avoid generic praise.

    ### 📊 Performance Efficiency (24/25)
    - Analyze the player's output relative to their minutes played.
    - Evaluate their 'Efficiency Delta' (Actual vs. Expected output). 
    - Note if their performance suggests sustainability or an overperformance streak.

    ### 🛡️ Tactical DNA
    - Identify their primary tactical function (e.g., Progressor, Destroyer, Inverted Threat).
    - Analyze their defensive contribution vs. offensive risk using Tkl, Int, and PrgP.

    ### ⚖️ 2026 Recruitment Verdict
    - **Verdict:** [IMMEDIATE SIGN / SCOUT FURTHER / DISREGARD]
    - **Reasoning:** Use specific metrics from the 24/25 season to justify the 2026 decision.
    - **System Fit:** Recommend the specific tactical setup that maximizes this data profile.
    """
    
    prompt = PromptTemplate(input_variables=["player_name", "technical_dossier"], template=template)
    chain = prompt | llm
    
    try:
        response = chain.invoke({"player_name": player_name, "technical_dossier": technical_dossier})
        return response.content
    except Exception as e:
        return f"⚠️ Analysis Engine Error: {str(e)}"