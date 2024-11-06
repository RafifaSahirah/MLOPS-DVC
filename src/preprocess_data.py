from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os

data = pd.read_csv("data/breast_cancer.csv")

features = data.columns[:-1]  
target = data['target'] 

scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

os.makedirs("data", exist_ok=True)

data.to_csv("data/breast_cancer.csv", index=False)

print("Data normalization complete. Saved to 'data/breast_cancer.csv'.")
