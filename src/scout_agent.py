import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Chargement des variables d'environnement
load_dotenv()

def get_scout_report(player_name, technical_dossier):
    """
    Génère un rapport de scouting ultra-précis en utilisant Llama 3.2 en local.
    Configuration optimisée pour la précision mathématique et l'analyse de données.
    """
    try:
        # Initialisation du modèle Llama 3.2 local
        llm = ChatOllama(
            model="llama3.2",
            temperature=0.0,
        )
        
        # Template haute densité avec règles de calcul strictes
        template = """
        ROLE: Senior Technical Scout & Data Scientist.
        OBJECTIVE: Clinical Audit of {player_name} for the 24/25 Season.
        RAW DATA INPUT: {technical_dossier}

        Your report must be the perfect blend of QUANTITATIVE MATH and QUALITATIVE TACTICS.

        ---

        ### 🏟️ TECHNICAL AUDIT: {player_name} 🏟️

        #### 📈 THE NUMBERS (QUANTITATIVE PILLAR)
        * **Efficiency Delta:** Calculate the difference between Goals and xG. Analyze if the player is over-performing (clinical skill) or under-performing (confidence/luck issues).
        * **Output Density:** Analyze Goals/Assists per 90 minutes based on the total minutes played.
        * **Progression Value:** Interpret Progressive Passes (PrgP) and Carries (PrgC). Is this player a "Verticality Engine" or a "Safety Passer"?

        #### 🧠 THE SCOUT'S EYE (QUALITATIVE PILLAR)
        * **Tactical Archetype:** Define their role (e.g., "False 9", "Space Interpreter", "Box-to-Box Engine") based on the statistical distribution.
        * **Defensive Work-Rate:** Interpret Tackles (Tkl) and Interceptions (Int). Is the player a "Pressing Trigger" or a "Positional Defender"?
        * **System Compatibility:** Which tactical setup (4-3-3 High Press, 3-4-3 Transition, etc.) maximizes this player's ROI?

        #### ⚖️ 2026 RECRUITMENT VERDICT
        * **Recommendation Score:** [X/10]
        * **Investment Risk:** [Low / Medium / High] - Justify based on data stability.
        * **Final Decision:** 🔥 **STRATEGIC SIGNING** / 📝 **MONITOR PROGRESS** / ❌ **PASS**.

        ---
        *Format: Use Markdown, bold headers, and professional scouting terminology.*
        """
        # Préparation du prompt
        prompt = PromptTemplate(
            input_variables=["player_name", "technical_dossier"], 
            template=template
        )
        
        # Création de la chaîne de traitement
        chain = prompt | llm
        
        # Exécution de l'analyse
        response = chain.invoke({
            "player_name": player_name, 
            "technical_dossier": technical_dossier
        })
        
        return response.content

    except Exception as e:
        return f"⚠️ Erreur Agent Local: {str(e)}. Assurez-vous qu'Ollama est lancé."