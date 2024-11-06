from sklearn.datasets import load_breast_cancer
import pandas as pd

# Load iris dataset
breast_cancer = load_breast_cancer()
data = pd.DataFrame(data=breast_cancer.data, columns=breast_cancer.feature_names)
data['target'] = breast_cancer.target

# Save to CSV
data.to_csv("data/breast_cancer.csv", index=False)
