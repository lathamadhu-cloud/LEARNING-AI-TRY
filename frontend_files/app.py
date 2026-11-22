
import streamlit as st
import requests
import json
import pandas as pd

#Base url for backend
BACKEND_URL = "http://localhost:7860"

#Page Title
st.title("SuperKart Sales Prediction")

st.write("Enter the product details to predict sales:")


#Input fields for product and store data
product_weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
product_sugar_content = st.selectbox("Product Sugar Content", ["Low Sugar", "Medium Sugar", "High Sugar"])
product_allocated_area = st.number_input("Product Allocated Area", min_value=0.0, value=0.027)
product_mrp = st.number_input("Product MRP", min_value=0.0, value=117.08)
store_size = st.selectbox("Store Size", ["Small", "Medium", "Large"])
store_location_city_type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
store_type = st.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2"])
product_id_char = st.selectbox("Product ID Character", ["FD", "NC"])
store_age_years = st.number_input("Store Age (Years)", min_value=0, value=16)
product_type_category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])



# create JSON payload
payload = {
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar_content,
    "Product_Allocated_Area": product_allocated_area,
    "Product_MRP": product_mrp,
    "Store_Size": store_size,
    "Store_Location_City_Type": store_location_city_type,
    "Store_Type": store_type,
    "Product_Id_char": product_id_char,
    "Store_Age_Years": store_age_years,
    "Product_Type_Category": product_type_category
}


# Single prediction
if st.button("Predict", type='primary'):
  response = requests.post(f"{BACKEND_URL}/v1/predict", json=payload)

  if response.status_code == 200:
    result = response.json()
    st.success(f"Predicted Sales: {result['prediction'][0]}")
  else:
    st.error("Error in prediction")



#Batch predction 
st.subheader("Batch Prediction")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
  if st.button("Predict Batch", type='primary'):
    files = {"file": uploaded_file}
    response = requests.post(f"{BACKEND_URL}/v1/predictbatch", files=files)
    if response.status_code == 200:
      result = response.json()
      df = pd.DataFrame(list(result.items()), columns=["Row_Index", "Predicted_Sales"])
      st.dataframe(df)
      st.success("Batch prediction completed")
    else:
      st.error("Error in batch prediction")
      
