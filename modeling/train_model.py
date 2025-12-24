# modeling/train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train_model(feature_rows, scores):
    X = pd.DataFrame(feature_rows)
    y = scores

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model
