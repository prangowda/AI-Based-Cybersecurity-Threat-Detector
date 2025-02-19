
# 🔒 AI-Based Cybersecurity Threat Detector  

## 📌 Overview  
The **AI-Based Cybersecurity Threat Detector** is an Intrusion Detection System (IDS) that analyzes network traffic and classifies activities as **normal or suspicious** using **Machine Learning (ML) and Deep Learning (DL)**. The system can detect potential cybersecurity threats and send real-time alerts.

## 🛠️ Technologies Used  
| **Technology** | **Purpose** |
|--------------|------------|
| **Python** | Core programming language |
| **Scikit-learn** | Machine learning model training |
| **Keras & TensorFlow** | Deep Learning framework |
| **Pandas** | Data manipulation and preprocessing |
| **NetworkX** | Network traffic analysis |
| **Flask** | API for real-time threat detection |

---

## 📂 **Project Structure**  
```
/Cybersecurity_Threat_Detector
│── dataset/                     # Network traffic dataset
│── train_threat_model.py         # Model training script
│── threat_detector.py            # Threat detection script
│── app.py                        # Flask API for real-time detection
│── model.h5                      # Trained machine learning model
│── scaler.pkl                    # Data scaler for preprocessing
│── README.md                     # Documentation
```

---

## 🚀 **Installation & Setup**  

### 1️⃣ Install Dependencies  
```sh
pip install pandas scikit-learn keras tensorflow networkx flask
```

### 2️⃣ Download Dataset  
You can use the **NSL-KDD Dataset** for training the model:  
🔗 [Download NSL-KDD Dataset](https://www.kaggle.com/competitions/nsl-kdd/data)  

Extract and place it inside the `dataset/` directory.

### 3️⃣ Train the Model  
Run the following command to train the AI model:  
```sh
python train_threat_model.py
```
This will generate a trained model file **model.h5** and a **scaler.pkl** file.

### 4️⃣ Test Threat Detection  
Run the script to check if a network event is suspicious or normal:  
```sh
python threat_detector.py
```
It will analyze a sample network event and return whether it's a **threat or normal**.

### 5️⃣ Start the Flask API  
To run the API for real-time detection, execute:  
```sh
python app.py
```
The API will be available at **http://127.0.0.1:5000/**.

---

## 🌐 **API Usage**  

### **1️⃣ Test API (Check If Threat is Detected)**
Send a **POST request** with network data:

#### **Request:**
```json
{
  "features": [0.1, 0.5, 0.2, 0.3, 0.7, 0.9]
}
```

#### **Response:**
```json
{
  "prediction": "Threat Detected 🚨"
}
```
or  
```json
{
  "prediction": "No Threat ✅"
}
```

---

## 📊 **Example Output**  

| **Network Event Data** | **Prediction** |
|------------------------|--------------|
| `[0.1, 0.2, 0.3, 0.4, 0.5, 0.6]` | ✅ **No Threat** |
| `[0.8, 0.9, 0.95, 0.99, 0.85, 0.9]` | 🚨 **Threat Detected** |

---

## 🎯 **Future Enhancements**  
✅ **Real-time monitoring with dashboards**  
✅ **Firewall integration for automatic blocking**  
✅ **AI-based anomaly detection for new types of attacks**  
✅ **Alert notifications via Email/SMS**  

---

## 🔒 **Conclusion**  
This **AI-based Cybersecurity Threat Detector** provides an **intelligent way to analyze and detect suspicious network traffic**. It can be extended for **enterprise security monitoring, real-time analysis, and automated response mechanisms**.

🚀 **Stay Secure, Stay Ahead!** 🚀
