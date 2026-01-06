import streamlit as st
import pandas as pd
import joblib
import os
from src.scout_agent import get_scout_report

st.set_page_config(page_title="ScoutAgent AI", page_icon="⚽", layout="wide")

# 1. Load the Model and Data
@st.cache_resource
def load_assets():
    model = joblib.load("models/scout_model.pkl")
    data = pd.read_csv("data/players_data_light-2024_2025.csv")
    return model, data

try:
    model, df = load_assets()
except Exception as e:
    st.error("⚠️ Model file not found! Run 'python src/train.py' first.")
    st.stop()

# 2. Sidebar Filters
st.sidebar.header("Filter Players")
selected_pos = st.sidebar.multiselect("Position", df['Pos'].unique(), default=["FW"])
max_age = st.sidebar.slider("Max Age", 16, 40, 25)

# 3. Main Interface
st.title("⚽ Scout-Agent AI: Technical Director Dashboard")

# Filter logic
filtered_df = df[(df['Pos'].isin(selected_pos)) & (df['Age'] <= max_age)]

st.subheader("Top Performers (XGBoost Predictions)")
# We use the model to predict xG for the display
top_players = filtered_df.sort_values(by="xG", ascending=False)
st.dataframe(top_players[['Player', 'Squad', 'Age', 'xG', 'Min']])

# 4. Agent Interaction
st.divider()
st.subheader("🤖 Ask the Scout Agent")
player_to_analyze = st.selectbox("Pick a player for a deep scouting report:", top_players['Player'])

if st.button("Generate AI Scouting Report"):
    # Grab that specific player's row as a string for the AI
    player_stats = top_players[top_players['Player'] == player_to_analyze].to_string()
    
    with st.spinner("Analyzing player profile..."):
        # This calls your src/scout_agent.py code!
        report = get_scout_report(player_to_analyze, player_stats)
        st.write(report)