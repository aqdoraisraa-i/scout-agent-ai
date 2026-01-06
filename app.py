import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.metrics.pairwise import cosine_similarity
from src.scout_agent import get_scout_report

# Page Config
st.set_page_config(page_title="Scout-Agent Pro AI", page_icon="⚽", layout="wide")

# Load Data (Light version for efficiency)
@st.cache_data
def load_data():
    # Ensure this path matches your folder structure
    return pd.read_csv("data/players_data_light-2024_2025.csv")

df = load_data()

# --- SIDEBAR: ADVANCED FILTERS ---
st.sidebar.title("🔍 Scouting Filters")

# League Filter
all_leagues = sorted(df['Comp'].unique())
selected_leagues = st.sidebar.multiselect("Leagues", all_leagues, default=all_leagues[:3])

# Position Filter
all_pos = sorted(df['Pos'].unique())
selected_pos = st.sidebar.multiselect("Positions", all_pos, default=['FW', 'MF'])

# Age Filter
max_age = st.sidebar.slider("Max Age", 16, 42, 30)

# Filter Dataset
filtered_df = df[
    (df['Comp'].isin(selected_leagues)) & 
    (df['Pos'].isin(selected_pos)) & 
    (df['Age'] <= max_age)
]

# --- SIMILARITY LOGIC ---
def calc_similarity(p1, p2, data):
    features = ['xG', 'xAG', 'PrgC', 'PrgP', 'Gls', 'Ast', 'Tkl+Int']
    v1 = data[data['Player'] == p1][features].fillna(0).values
    v2 = data[data['Player'] == p2][features].fillna(0).values
    if len(v1) > 0 and len(v2) > 0:
        return round(cosine_similarity(v1, v2)[0][0] * 100, 1)
    return 0

# --- MAIN INTERFACE ---
tab1, tab2 = st.tabs(["👤 Player Dossier", "⚖️ Tactical Comparison"])

with tab1:
    st.title("🤖 2024-2025 Season AI Audit")
    if not filtered_df.empty:
        target_player = st.selectbox("Select Player:", filtered_df['Player'].unique())
        
        p_row = df[df['Player'] == target_player].iloc[0]
        
        # Stats Grid
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("90s Played", p_row['90s'])
        m2.metric("xG / Gls", f"{p_row['xG']} / {p_row['Gls']}")
        m3.metric("xAG / Ast", f"{p_row['xAG']} / {p_row['Ast']}")
        m4.metric("Prog. Passes", p_row['PrgP'])

        if st.button("Generate AI Scouting Report"):
            with st.spinner("Analyzing performance vectors..."):
                dossier = p_row[['Pos', 'Comp', 'Min', 'Gls', 'xG', 'Ast', 'xAG', 'Tkl+Int']].to_dict()
                report = get_scout_report(target_player, str(dossier))
                st.markdown(report)
                
                st.download_button("📩 Download Report", report, f"{target_player}_Report.txt")
    else:
        st.error("No players match your filters. Please adjust the sidebar.")

with tab2:
    st.title("📊 Strategic Comparison")
    col_l, col_r = st.columns(2)
    with col_l:
        player1 = st.selectbox("Player 1 (Target):", filtered_df['Player'].unique(), key="p1")
    with col_r:
        player2 = st.selectbox("Player 2 (Benchmark):", df['Player'].unique(), key="p2")

    sim_score = calc_similarity(player1, player2, df)
    
    st.markdown(f"""
        <div style="text-align: center; border: 2px solid #3b82f6; border-radius: 15px; padding: 20px;">
            <h2 style="margin:0;">Tactical Similarity: <span style="color:#3b82f6;">{sim_score}%</span></h2>
        </div>
    """, unsafe_allow_html=True)

    # Radar Plot
    radar_metrics = ['xG', 'xAG', 'PrgC', 'PrgP', 'Tkl+Int']
    def norm(name):
        return [df[df['Player'] == name][m].iloc[0] / df[m].max() for m in radar_metrics]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=norm(player1), theta=radar_metrics, fill='toself', name=player1, line_color='#ef4444'))
    fig.add_trace(go.Scatterpolar(r=norm(player2), theta=radar_metrics, fill='toself', name=player2, line_color='#3b82f6'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1]), gridshape='linear'), template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)