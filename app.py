import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

st.title("🚗 Car Price Prediction App")
st.write("Welcome to our Final Project App! Predict car prices using Machine Learning.")

tab1, tab2, tab3 = st.tabs(["✍️ Manual Input", "📁 Upload CSV", "📷 Camera Capture"])

with tab1:
    st.header("Enter Car Details Manually")
    
    col1, col2 = st.columns(2)
    
    with col1:
        brand = st.selectbox("Brand", ["Tesla", "BMW", "Audi", "Ford", "Honda", "Mercedes", "Toyota"])
        model = st.text_input("Model (e.g., Model X, 5 Series, A4, Civic)", "Model X")
        year = st.number_input("Year", min_value=1990, max_value=2026, value=2020)
        engine_size = st.number_input("Engine Size (Liters)", min_value=0.5, max_value=8.0, value=2.0, step=0.1)

    with col2:
        fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
        mileage = st.number_input("Mileage (KM)", min_value=0, max_value=500000, value=50000)
        condition = st.selectbox("Condition", ["New", "Like New", "Used"])

    if st.button("Predict Price", type="primary"):
        st.success("🎉 Prediction Success!")
        st.metric(label="Estimated Car Price", value="$25,400", delta="Confidence: 94.5%")
        st.info("💡 Note: This is a placeholder prediction until we load the trained model file.")

with tab2:
    st.header("Upload a CSV File for Bulk Prediction")
    uploaded_file = st.file_uploader("Choose a CSV file containing car data", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📋 Uploaded Data Preview:")
        st.dataframe(df.head())
        st.button("Predict All Prices from File")

with tab3:
    st.header("Capture Car Image")
    img_file = st.camera_input("Take a picture of the car")
    if img_file is not None:
        st.image(img_file, caption="Captured Car Image", use_container_width=True)