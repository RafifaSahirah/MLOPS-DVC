# MLOps-DVC
## Setup and Version Control with Git and DVC

This guide demonstrates how to use Git and DVC (Data Version Control) for managing a dataset and machine learning model for breast cancer classification.

```bash
# 1. Clone the Repository
git clone https://github.com/RafifaSahirah/MLOps-DVC.git
cd MLOps-DVC

# 2. Initialize Git and DVC
git init
dvc init

# 3. Prepare the Data
python3 src/prepare_data.py

# 4. Add the Raw Dataset to DVC
dvc add data/breast_cancer.csv

# 5. Create the .gitignore file for data
touch data/.gitignore

# 6. Add the necessary files to Git
git add data/breast_cancer.csv.dvc data/.gitignore
git commit -m "Add raw dataset"

# 7. Train the Model with Raw Dataset
python3 src/train.py

# 8. Add the Trained Model to DVC
dvc add models/model.pkl

# 9. Create the .gitignore file for models
touch models/.gitignore

# 10. Add the trained model to Git
git add models/model.pkl.dvc models/.gitignore
git commit -m "Add trained model with raw dataset"

# 11. Preprocess the Data
python3 src/preprocess_data.py

# 12. Add the Preprocessed Dataset to DVC
dvc add data/breast_cancer.csv

# 13. Add the preprocessed dataset to Git
git add data/breast_cancer.csv.dvc
git commit -m "Add preprocessed dataset"

# 14. Retrain the Model with Preprocessed Dataset
python3 src/train.py

# 15. Add the Updated Model to DVC
dvc add models/model.pkl

# 16. Add the updated model to Git
git add models/model.pkl.dvc
git commit -m "Add trained model with preprocessed dataset"

# 17. View Commit History
git log -- data/breast_cancer.csv.dvc
git log -- models/model.pkl.dvc