import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("heart_model.pkl")
columns = joblib.load("columns.pkl")

st.title(" Heart Disease Prediction")

age = st.number_input("Age",18,100,45)

sex = st.selectbox("Sex",["M","F"])

chest = st.selectbox("Chest Pain Type",
                     ["ATA","NAP","ASY","TA"])

bp = st.number_input("Resting Blood Pressure",80,250,120)

chol = st.number_input("Cholesterol",0,700,200)

fbs = st.selectbox("Fasting Blood Sugar",[0,1])

ecg = st.selectbox("Resting ECG",
                   ["Normal","ST","LVH"])

hr = st.number_input("Maximum Heart Rate",60,220,150)

angina = st.selectbox("Exercise Angina",
                      ["Y","N"])

oldpeak = st.number_input("Old Peak",
                          0.0,10.0,1.0)

slope = st.selectbox("ST Slope",
                     ["Up","Flat","Down"])

predict = st.button("Predict")

if predict:

    input_data = pd.DataFrame({

        "Age":[age],
        "Sex":[sex],
        "ChestPainType":[chest],
        "RestingBP":[bp],
        "Cholesterol":[chol],
        "FastingBS":[fbs],
        "RestingECG":[ecg],
        "MaxHR":[hr],
        "ExerciseAngina":[angina],
        "Oldpeak":[oldpeak],
        "ST_Slope":[slope]

    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match Training Columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Heart Disease: YES")
    else:
        st.success("Heart Disease: NO")


        