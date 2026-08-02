import streamlit as st
import pandas as pd
import joblib

# Load Files
model = joblib.load("RF_Titanic.pkl")
scaler = joblib.load("RF_TScaler.pkl")
columns = joblib.load("RF_TColumns.pkl")

st.title("Titanic Survival Prediction")

# User Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses", 0, 10, 0)
parch = st.number_input("Parents/Children", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 50.0)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

if st.button("Predict"):

    data = {
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Sex_male": 1 if sex == "male" else 0,
        "Embarked_Q": 1 if embarked == "Q" else 0,
        "Embarked_S": 1 if embarked == "S" else 0
    }

    input_df = pd.DataFrame([data])

    # Match training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")


        