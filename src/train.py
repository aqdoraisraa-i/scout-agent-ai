import pandas as pd
import xgboost as xgb
import joblib
import os

def train_scout_model():
    data_path = "data/players_data_light-2024_2025.csv"
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found!")
        return

    df = pd.read_csv(data_path)
    # Using key features for scouting prediction
    features = ['Age', 'MP', 'Starts', 'Min', '90s']
    X = df[features].fillna(0)
    y = df['xG'].fillna(0) 

    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    model.fit(X, y)

    if not os.path.exists('models'):
        os.makedirs('models')
        
    joblib.dump(model, "models/scout_model.pkl")
    print("✅ Model trained successfully: models/scout_model.pkl")

if __name__ == "__main__":
    train_scout_model()