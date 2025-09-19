from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model = joblib.load('crop_model.pkl')
le = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return "ML Prediction Service is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data.get(k, 0) for k in ['N', 'P', 'K', 'pH', 'temperature', 'humidity', 'rainfall']]
    df = pd.DataFrame([features], columns=['N', 'P', 'K', 'pH', 'temperature', 'humidity', 'rainfall'])
    pred_encoded = model.predict(df)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]
    return jsonify({"recommended_crop": pred_label})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
