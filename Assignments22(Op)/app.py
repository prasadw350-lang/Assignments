import streamlit as st
import pandas as pd
import joblib

# Load Saved Files
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("Diabetes Prediction System")
st.write("Enter the patient's details below and click **Predict** to check the diabetes prediction.")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

age = st.number_input("Age", min_value=1, max_value=120, value=40)

hypertension = st.selectbox(" Hypertension", [0, 1])

heart_disease = st.selectbox(" Heart Disease", [0, 1])

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "No Info", "current", "former", "ever", "not current"]
)

bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=25.0)

hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=10.0, value=5.5)

glucose = st.number_input("Blood Glucose Level", min_value=50, max_value=400, value=120)

if st.button("Predict Diabetes"):

    input_data = pd.DataFrame({

        "gender":[gender],
        "age":[age],
        "hypertension":[hypertension],
        "heart_disease":[heart_disease],
        "smoking_history":[smoking_history],
        "bmi":[bmi],
        "HbA1c_level":[hba1c],
        "blood_glucose_level":[glucose]

    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match Training Columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Scale
    input_data = pd.DataFrame(
        scaler.transform(input_data),
        columns=columns
    )

    prediction = model.predict(input_data)

    st.markdown("---")
    if prediction[0] == 1:
        st.error("**Prediction: Diabetes Detected (YES)**")
    else:
        st.success("**Prediction: No Diabetes (NO)**")


        