# Car Price Prediction App

A machine learning-based web application that estimates the price of a car using key attributes such as brand, model, year, engine size, fuel type, transmission, mileage, and condition. The project combines data science and web development to create an interactive Streamlit experience for predicting vehicle prices.

## Overview

This project demonstrates a complete end-to-end machine learning workflow:

- Data exploration and preprocessing
- Model training and evaluation in a Jupyter notebook
- Deployment of a user-friendly web interface with Streamlit

## Key Features

- Manual prediction through an interactive form
- Bulk prediction from uploaded CSV files
- Image upload/capture support for car photos
- Clean and responsive user interface

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Jupyter Notebook
- Joblib

## Project Structure

- app.py — Main Streamlit application
- car-price-prediction.ipynb — Notebook for data analysis and model experimentation
- car*price_prediction*.csv — Dataset used for training and evaluation
- car_price_model.pkl — Serialized trained model

## Getting Started

### Prerequisites

Make sure Python is installed on your system.

### Installation

Install the required dependencies:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Running the Application

Start the app locally with:

```bash
streamlit run app.py
```

Then open the URL displayed in the terminal in your browser.

## How to Use

1. Open the app in your browser.
2. Choose one of the available input options:
   - Manual Input: enter car details manually
   - Upload CSV: upload a file containing multiple car records
   - Camera Capture: upload or capture a car image
3. Click the prediction button to view the estimated price.

## Current Status

The application is designed as a functional prototype. The manual input section currently displays a sample prediction while the trained model integration is being completed.

## Future Enhancements

- Connect the Streamlit app to the saved model for real predictions
- Improve model accuracy with better feature engineering
- Add robust CSV validation and error handling
- Enhance the UI with richer visualizations and prediction explanations

## License

This project is intended for educational and demonstration purposes.
