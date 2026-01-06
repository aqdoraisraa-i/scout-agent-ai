import streamlit as st
import pandas as pd
import joblib
import os
from src.scout_agent import get_scout_report

st.set_page_config(page_title="Scout-Agent AI", page_icon="⚽", layout="wide")

@st.cache_resource
def load_assets():
    model = joblib.load("models/scout_model.pkl")
    data = pd.read_csv("data/players_data_light-2024_2025.csv")
    return model, data

if not os.path.exists("models/scout_model.pkl"):
    st.error("🚨 Run 'python src/train.py' first!")
    st.stop()

model, df = load_assets()

st.title("⚽ Scout-Agent AI: Technical Director")

# Sidebar Filters
selected_pos = st.sidebar.multiselect("Position", df['Pos'].unique(), default=["FW"])
max_age = st.sidebar.slider("Max Age", 16, 45, 28)

# FILTER ALL PLAYERS
filtered_df = df[(df['Pos'].isin(selected_pos)) & (df['Age'] <= max_age)]
top_players = filtered_df.sort_values(by="xG", ascending=False)

st.subheader(f"Matching Prospects ({len(top_players)} found)")
st.dataframe(top_players[['Player', 'Squad', 'Age', 'xG', 'Min']], use_container_width=True)

st.divider()

st.subheader("🤖 AI Scouting Analysis")
player_to_analyze = st.selectbox("Select Player:", top_players['Player'])

if st.button("Generate AI Report"):
    # Pass player specific stats to the AI
    stats_str = top_players[top_players['Player'] == player_to_analyze].to_string()
    with st.spinner("AI is analyzing performance..."):
        report = get_scout_report(player_to_analyze, stats_str)
        st.markdown(report)