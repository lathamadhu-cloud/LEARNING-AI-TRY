
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import joblib


superkart_model = Flask("SuperKart")

model = joblib.load("backend_files/superkart_model.joblib")

# define route for default home page

@superkart_model.route("/")
def home():
    return "Welcome to SuperKart"

# define an endpoint to predict sales for a single product

@superkart_model.route("/v1/predict", methods=["POST"])
def predict():
    # Get the input data from the request
    data = request.get_json()

    sample = {
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_MRP': data['Product_MRP'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Product_Id_char': data['Product_Id_char'],
        'Store_Age_Years': data['Store_Age_Years'],
        'Product_Type_Category': data['Product_Type_Category']
    }

    input_data = pd.DataFrame([sample])

    prediction = model.predict(input_data)

    return jsonify({"prediction": prediction.tolist()})



  
  # define an endpoint to predict sales for a batch of products

@superkart_model.route("/v1/predictbatch", methods=["POST"])
def predictbatch():
  # Get the input data from the request
  data = request.files["file"]
  data = pd.read_csv(data)

  prediction = model.predict(data)
  predictions = prediction.tolist()

  output_dict = {str(index): value for index, value in enumerate(predictions)}

  return jsonify(output_dict)


  # Run the Flask app in debug mode

  if __name__ == "__main__":
    superkart_model.run(debug=True)
