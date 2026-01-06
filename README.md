# ⚽ Scout-Agent AI: Technical Director Assistant

**Autonomous Football Scouting Agent** | Built with XGBoost & LangChain | Predictive Analytics + GenAI Technical Director

---

## 🌟 Project Overview
Scout-Agent AI is a data-driven intelligence tool designed for modern football recruitment. It bridges the gap between raw performance data and actionable scouting insights by combining **Predictive Machine Learning** with **Generative AI**.

### 🔄 The Hybrid Workflow
1.  **Predictive Brain (XGBoost)**: Analyzes historical player workloads (minutes, starts) to predict future $xG$ (Expected Goals) output.
2.  **Strategic Voice (Gemini 2.5)**: A LangChain-powered agent acts as a "Technical Director," transforming stats into professional scouting reports with tactical fit and "Sign/Pass" recommendations.

## 🛠️ Tech Stack (2026 Standard)
* **Machine Learning**: XGBoost (Regression Modeling)
* **AI Orchestration**: LangChain + Google Gemini 2.5 Flash
* **Frontend**: Streamlit (Reactive Web Dashboard)
* **Data Science**: Pandas, Scikit-learn, Joblib
* **Environment**: Dotenv (Secure API Management)

## 🚀 Installation & Setup

1. **Clone the Repo**
```bash
   git clone [https://github.com/aqdoraisraa-i/scout-agent-ai.git](https://github.com/aqdoraisraa-i/scout-agent-ai.git)
   cd scout-agent-ai
  ``` 
2. **Initialize Environment**
  ```bash
  python -m venv venv
  source venv/Scripts/activate  # Windows: .\venv\Scripts\activate
  pip install -r requirements.txt
  ```
3. **Secure Your Keys Create a .env file in the root (this is ignored by Git for security)**
 ```bash
 GOOGLE_API_KEY=your_gemini_api_key_here
 ```
 4. **Run the app**
  ```bash
  python src/train.py   # Train the XGBoost predictive model
streamlit run app.py  # Launch the scouting dashboard
  ```

## 📊 Key Features
- Predictive Filtering: Find players based on predicted performance metrics.
- Deep Tactical Reports: AI-generated analysis of playing style, strengths, and weaknesses.
- Exportable Insights: Download professional reports as .txt files for your scouting archive.

Developed by aqdoraisraa-i — Empowering football recruitment with Hybrid AI.
