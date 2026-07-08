"""
---------------------------------------------------------
Iris Flower Prediction System
Frontend : Streamlit
Author : Harsh Singh Gaur
---------------------------------------------------------
"""

import requests
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📘 Project Information")

st.sidebar.markdown("""
### AI/ML Internship Assignment

**Algorithm**
- Random Forest Classifier

**Dataset**
- Iris Dataset

**Frameworks**
- FastAPI
- Streamlit

**Database**
- SQLite

**Author**
Harsh Singh Gaur
""")

# -----------------------------
# Title
# -----------------------------

st.title("🌸 Iris Flower Prediction System")

st.markdown(
    "Predict the species of an Iris flower using Machine Learning."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        value=5.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        value=3.5
    )

with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        value=1.4
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        value=0.2
    )

st.divider()

# -----------------------------
# Predict Button
# -----------------------------

if st.button("🔍 Predict Flower"):

    user_input = {

        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width

    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=user_input
        )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Prediction Successful")

            st.subheader("Prediction")

            st.write(f"**Flower :** {result['flower']}")

            st.write(f"**Class :** {result['prediction']}")

            st.write(
                f"**Confidence :** {result['confidence']:.2%}"
            )

            st.progress(result["confidence"])

        else:

            st.error("Prediction Failed.")

    except Exception:

        st.error(
            "Cannot connect to FastAPI.\n\n"
            "Please make sure the API is running."
        )

st.divider()

st.caption(
    "Built using FastAPI • Streamlit • Scikit-Learn • SQLite"
)