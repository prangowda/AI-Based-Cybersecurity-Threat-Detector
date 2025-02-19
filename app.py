from flask import Flask, request, jsonify
import numpy as np
import pickle
from keras.models import load_model

app = Flask(__name__)

# Load trained model
model = load_model("model.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return "Cybersecurity Threat Detection API is Running 🚀"

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)[0][0]
    result = "Threat Detected 🚨" if prediction > 0.5 else "No Threat ✅"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
