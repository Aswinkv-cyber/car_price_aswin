import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and car names
pipe = pickle.load(open('model.pkl', 'rb'))
car_names = pickle.load(open('encoder.pkl', 'rb'))

st.title('Car Price Prediction App')

# User inputs
name = st.selectbox('Car Name', car_names)  # 🛠️ Dropdown instead of text input
company = st.selectbox('Company', ['Tata', 'Maruti', 'Hyundai', 'Toyota', 'Honda', 'Ford'])  # Expand if needed
year = st.number_input('Manufacturing Year', min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input('Kilometers Driven', value=10000)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])

if st.button('Predict Price'):
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    prediction = pipe.predict(input_df)[0]
    st.success(f'Estimated Price: ₹{int(prediction):,}')
