"""
---------------------------------------------------------
Iris Flower Prediction - Model Training
Author : Harsh Singh Gaur
Description:
This script trains a Random Forest model using the
Iris dataset, performs simple feature engineering,
evaluates the model, and saves it as model.pkl.
---------------------------------------------------------
"""

import joblib
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

iris = load_iris()

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

target = iris.target


# -------------------------------------------------------
# Feature Engineering
# -------------------------------------------------------

# New Feature 1
data["petal_area"] = (
    data["petal length (cm)"] *
    data["petal width (cm)"]
)

# New Feature 2
data["sepal_area"] = (
    data["sepal length (cm)"] *
    data["sepal width (cm)"]
)


# -------------------------------------------------------
# Train Test Split
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    data,
    target,
    test_size=0.20,
    random_state=42
)


# -------------------------------------------------------
# Train Model
# -------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# -------------------------------------------------------
# Model Evaluation
# -------------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("=" * 50)
print("Model Trained Successfully")
print(f"Accuracy : {accuracy:.2%}")
print("=" * 50)


# -------------------------------------------------------
# Save Model
# -------------------------------------------------------

joblib.dump(
    model,
    "model.pkl"
)

print("model.pkl saved successfully.")