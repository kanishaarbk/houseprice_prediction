import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

# User Inputs
area = st.number_input("Area (sq.ft)", min_value=100, value=1000, step=100)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2, step=1)

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")
