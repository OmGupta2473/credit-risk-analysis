
# 🏦 AI Financial Risk Assessment

A machine‑learning powered financial risk prediction system built with **Streamlit**, **Random Forest Classifier**, and the **German Credit Dataset**.  
This app analyzes user‑provided financial details and predicts whether the applicant is **Low Risk (Approved)** or **High Risk (Rejected)** with confidence scores.

---

## ⭐ Features
- 🔐 User‑friendly Streamlit UI  
- 📊 Predict loan repayment likelihood  
- 🤖 Trained ML model using Random Forest  
- 📈 Confidence‑based approval system (65% threshold)  
- 🛠 Smart insights (e.g., high monthly payment warning)  
- 🔄 Encoded categorical features for accurate prediction  
- 📉 Displays probability scores for decision clarity  

---

## 📂 Folder Structure
```
├── app.py                     # Streamlit main app
├── analysis.ipynb            # Model training & EDA
├── german_credit_data.csv     # Dataset
├── financial_risk_model.pkl   # Trained ML model
└── README.md                  # Documentation
```

---

## 🧰 Technologies Used
- **Frontend/UI:** Streamlit  
- **Model:** Random Forest Classifier  
- **Language:** Python  
- **Libraries:** pandas, numpy, joblib, scikit-learn  

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.8+
- pip installed

---

## 🛠 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/financial-risk-predictor.git
cd financial-risk-predictor
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App
Start the Streamlit server:
```bash
streamlit run app.py
```

Your app will open at:
```
http://localhost:8501/
```

---

## ⚙️ Environment Notes
- Model is loaded from `financial_risk_model.pkl`
- Feature encoding must match training pipeline
- Monthly payment is auto‑engineered (`amount / duration`)

---

## 📈 Prediction Logic
- Model predicts probability of **Good (Low‑Risk)**  
- If probability > **65% → Approved**  
- Otherwise → Rejected  
- Shows confidence score & warnings

---

## 🧪 Example Features Used
- Age  
- Gender  
- Job Skill Level  
- Housing Status  
- Savings Balance  
- Checking Account Balance  
- Loan Amount  
- Duration  
- Purpose  
- Monthly Payment *(engineered)*  

---

## 🤝 Contributing
1. Fork the repo  
2. Create a branch `feature/your-feature`  
3. Commit your changes  
4. Open a Pull Request  

---

## 📜 License
This project is for **educational purposes only** and not intended for real‑world financial decisions.
