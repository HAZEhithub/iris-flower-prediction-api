"""
---------------------------------------------------------
Iris Flower Prediction API
Author : Harsh Singh Gaur

Framework : FastAPI
Database  : SQLite
Model     : Random Forest

This API:
✔ Loads model only once
✔ Validates input
✔ Predicts flower species
✔ Stores prediction history
✔ Logs API activity
---------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import sqlite3
import logging
import joblib
from datetime import datetime

# -----------------------------------------------------
# Logging
# -----------------------------------------------------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("API Started Successfully")

# -----------------------------------------------------
# FastAPI Application
# -----------------------------------------------------

app = FastAPI(
    title="Iris Flower Prediction API",
    description="Predict Iris Flower Species",
    version="1.0"
)

# -----------------------------------------------------
# Load Trained Model
# -----------------------------------------------------

model = joblib.load("model.pkl")

# -----------------------------------------------------
# SQLite Database
# -----------------------------------------------------

connection = sqlite3.connect(
    "predictions.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp TEXT,

sepal_length REAL,
sepal_width REAL,
petal_length REAL,
petal_width REAL,

prediction TEXT,
confidence REAL

)
""")

connection.commit()

# -----------------------------------------------------
# Flower Names
# -----------------------------------------------------

FLOWER_NAMES = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# -----------------------------------------------------
# Input Validation
# -----------------------------------------------------

class IrisInput(BaseModel):

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# -----------------------------------------------------
# Health Endpoint
# -----------------------------------------------------

@app.get("/health")
def health():

    logging.info("Health Endpoint Called")

    return {
        "status": "ok",
        "message": "API is running successfully."
    }

# -----------------------------------------------------
# Prediction Endpoint
# -----------------------------------------------------

@app.post("/predict")
def predict(input_data: IrisInput):

    try:

        logging.info("Prediction Request Received")

        # Feature Engineering

        petal_area = (
            input_data.petal_length *
            input_data.petal_width
        )

        sepal_area = (
            input_data.sepal_length *
            input_data.sepal_width
        )

        dataframe = pd.DataFrame([{

            "sepal length (cm)": input_data.sepal_length,
            "sepal width (cm)": input_data.sepal_width,
            "petal length (cm)": input_data.petal_length,
            "petal width (cm)": input_data.petal_width,

            "petal_area": petal_area,
            "sepal_area": sepal_area

        }])

        prediction = int(
            model.predict(dataframe)[0]
        )

        confidence = float(
            max(model.predict_proba(dataframe)[0])
        )

        flower_name = FLOWER_NAMES[prediction]

        # Save Prediction

        cursor.execute("""

        INSERT INTO predictions(

        timestamp,

        sepal_length,
        sepal_width,
        petal_length,
        petal_width,

        prediction,
        confidence

        )

        VALUES(?,?,?,?,?,?,?)

        """, (

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width,

            flower_name,
            confidence

        ))

        connection.commit()

        logging.info("Prediction Saved Successfully")

        return {

            "success": True,

            "flower": flower_name,

            "prediction": prediction,

            "confidence": round(confidence,3),

            "message": "Prediction completed successfully."

        }

    except Exception as error:

        logging.error(str(error))

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )