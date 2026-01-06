import pandas as pd
import xgboost as xgb
import joblib
import os

def train_scout_model():
    # 1. Load the data you downloaded from Kaggle
    data_path = "data/players_data_light-2024_2025.csv"
    if not os.path.exists(data_path):
        print("❌ Data file not found in /data folder!")
        return

    df = pd.read_csv(data_path)

    # 2. Select columns for the AI to study
    # Age, Matches Played, Starts, Minutes, 90s played
    features = ['Age', 'MP', 'Starts', 'Min', '90s']
    X = df[features].fillna(0)
    y = df['xG'].fillna(0) # We are predicting 'Expected Goals'

    # 3. Train the XGBoost Model
    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1)
    model.fit(X, y)

    # 4. Save the "Brain"
    if not os.path.exists('models'): os.makedirs('models')
    joblib.dump(model, "models/scout_model.pkl")
    print("✅ Predictive Brain trained and saved to models/scout_model.pkl")

if __name__ == "__main__":
    train_scout_model()