import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Assignments\Model A21(Op)\SportCar.pkl")
scaler = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Assignments\Model A21(Op)\scaler.pkl")
columns = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Assignments\Model A21(Op)\columns.pkl")

st.set_page_config(page_title="Sport Car Price Predictor", layout="centered")

st.title("Sport Car Price Prediction")
st.write("Enter the details below")

# User Input
year = st.number_input("Year", min_value=1960, max_value=2025, value=2020)

car_make = st.selectbox("Car Make", [
    "Audi","BMW","Bugatti","Chevrolet","Ferrari",
    "Lamborghini","McLaren","Mercedes-Benz","Porsche"
])
car_model = st.text_input("Car Model", value="911")

engine = st.number_input(
    "Engine Size (L)",
    min_value=1.0,
    max_value=8.5,
    value=3.0,
    step=0.1
)
horsepower = st.number_input(
    "Horsepower",
    min_value=100,
    max_value=2000,
    value=400
)
torque = st.number_input(
    "Torque (lb-ft)",
    min_value=100,
    max_value=2000,
    value=450
)
mph = st.number_input(
    "0-60 MPH Time (seconds)",
    min_value=1.5,
    max_value=15.0,
    value=4.5,
    step=0.1
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Car Make": [car_make],
        "Car Model": [car_model],
        "Year": [year],
        "Engine Size (L)": [engine],
        "Horsepower": [horsepower],
        "Torque (lb-ft)": [torque],
        "0-60 MPH Time (seconds)": [mph]
    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Scale
    input_data = pd.DataFrame(
        scaler.transform(input_data),
        columns=columns
    )
    # Prediction
    prediction = model.predict(input_data)
    st.success(f"Predicted Sport Car Price: ${prediction[0]:,.2f}")
