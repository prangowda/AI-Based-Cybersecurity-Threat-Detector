import pickle
import numpy as np
from keras.models import load_model

# Load model and scaler
model = load_model("model.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))

def detect_threat(features):
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)[0][0]
    return "Threat Detected 🚨" if prediction > 0.5 else "No Threat ✅"

# Example usage
if __name__ == "__main__":
    sample_data = [0.1, 0.5, 0.2, 0.3, 0.7, 0.9]  # Example network data
    print("Detection Result:", detect_threat(sample_data))
