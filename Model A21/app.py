# Import Streamlit for Web Application
import streamlit as st
# Import Pandas for Data Handling
import pandas as pd
# Import Joblib to Load Saved Model
import joblib

model = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Model A21\LR_model.pkl")
scaler = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Model A21\scaler.pkl")
encoded_columns = joblib.load("C:\Industrial Training\AIML\Python\AllAssignments\Model A21\columns.pkl")

# Sets page title and keeps page centered
st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)

# Title and Description

st.title("Ford Car Price Predictor")
st.write("Enter the car details below to predict its selling price.")

# Numerical Inputs

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2035,
    value=2020
)
mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=10000
)
tax = st.number_input(
    "Road Tax",
    min_value=0,
    value=150
)

mpg = st.number_input(
    "Miles Per Gallon (MPG)",
    min_value=0.0,
    value=50.0
)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.5,
    value=1.5
)

# Dropdown Inputs

# Selectbox prevents invalid user input
transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual", "Semi-Auto"]
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)


# Text Input and Predict Button

model_name = st.text_input("Car Model")

if st.button("Predict Price"):

    # Create Input DataFrame
    input_data = pd.DataFrame({

        "model":[model_name],
        "year":[year],
        "transmission":[transmission],
        "mileage":[mileage],
        "fuelType":[fuel],
        "tax":[tax],
        "mpg":[mpg],
        "engineSize":[engine_size]

    })

# One-Hot Encoding

    input_data = pd.get_dummies(input_data)

    # Match Training Columns
    input_data = input_data.reindex(
        columns=encoded_columns,
        fill_value=0
    )

# Feature Scaling

    num_cols = [
        "year",
        "mileage",
        "tax",
        "mpg",
        "engineSize"
    ]

    input_data[num_cols] = scaler.transform(
        input_data[num_cols]
    )

# Prediction

    prediction = model.predict(input_data)
# Display Result

    st.success(
        f"Predicted Price: £{prediction[0]:,.2f}"
    )
