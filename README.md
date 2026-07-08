# 🌸 Iris Flower Prediction System

> End-to-End Machine Learning Application using FastAPI, Streamlit and Scikit-Learn

---

# 📌 Project Overview

The Iris Flower Prediction System is an end-to-end Machine Learning project that predicts the species of an Iris flower using four flower measurements.

The application demonstrates a complete ML deployment pipeline:

- Data Preparation
- Feature Engineering
- Model Training
- Model Serialization
- REST API Development
- Database Logging
- Interactive Web Interface

The project follows a modular architecture where the Machine Learning model, API, and User Interface are separated into independent components.

---

# 🎯 Objectives

The objective of this project is to:

- Train a Machine Learning classification model
- Deploy the model using FastAPI
- Build an interactive UI using Streamlit
- Store prediction history using SQLite
- Demonstrate an end-to-end ML workflow

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | REST API |
| Streamlit | Frontend UI |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| Joblib | Save & Load Model |
| SQLite | Prediction Database |
| Requests | API Communication |

---

# 📂 Project Structure

```
AI-ML Assignment
│
├── train_model.py
├── api.py
├── app.py
├── model.pkl
├── predictions.db
├── app.log
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset Used:

**Iris Dataset**

Provided by:

Scikit-Learn

Total Records:

150

Flower Classes:

- Setosa
- Versicolor
- Virginica

Input Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

# 🧠 Machine Learning Model

Algorithm Used

Random Forest Classifier

Why Random Forest?

- High Accuracy
- Easy to Train
- Robust
- Handles Small Datasets Well
- Supports Probability Prediction

---

# ⚙ Feature Engineering

Two additional features were created to improve prediction quality.

### Feature 1

Petal Area

```
Petal Length × Petal Width
```

### Feature 2

Sepal Area

```
Sepal Length × Sepal Width
```

These engineered features provide additional information about flower size and improve model performance.

---

# 🌐 REST API

## Health Check

GET

```
/health
```

Response

```json
{
    "status":"ok",
    "message":"API is running successfully."
}
```

---

## Prediction

POST

```
/predict
```

Request

```json
{
    "sepal_length":5.1,
    "sepal_width":3.5,
    "petal_length":1.4,
    "petal_width":0.2
}
```

Response

```json
{
    "success":true,
    "flower":"Setosa",
    "prediction":0,
    "confidence":1.0,
    "message":"Prediction completed successfully."
}
```

---

# 🗄 Database

Prediction history is stored inside

```
predictions.db
```

Each record stores:

- Timestamp
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Predicted Flower
- Confidence Score

---

# 📝 Logging

All API events are recorded in

```
app.log
```

Logged Events:

- API Started
- Health Check
- Prediction Request
- Database Insert
- Errors

---

# ▶ Installation

## Step 1

Clone Repository

```bash
git clone <repository-url>
```

---

## Step 2

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3

Train Model

```bash
py train_model.py
```

---

## Step 4

Run FastAPI

```bash
py -m uvicorn api:app --reload
```

---

## Step 5

Run Streamlit

```bash
py -m streamlit run app.py
```

---

# 🧪 Testing

Health Endpoint

```
http://127.0.0.1:8000/health
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Streamlit UI

```
http://localhost:8501
```

---

# 🏗 Project Architecture

```
             User

               │

               ▼

         Streamlit UI

               │

HTTP POST Request (JSON)

               │

               ▼

          FastAPI Server

               │

               ▼

      Random Forest Model

               │

               ▼

      Predicted Flower

               │

               ▼

        SQLite Database

               │

               ▼

      Prediction Response

               │

               ▼

          Streamlit UI
```

---

# 📈 Future Improvements

- User Authentication
- Cloud Deployment
- Docker Support
- Model Versioning
- Multiple ML Algorithms
- Better Data Visualization
- Prediction History Dashboard

---

# 👨‍💻 Author

**Harsh Singh Gaur**

B.E. Computer Science Engineering (AI & ML)

Chandigarh University

---

# 📄 License

This project was developed as part of an AI/ML Internship Take-Home Assignment for educational purposes.