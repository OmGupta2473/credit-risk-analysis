🏦 AI Financial Risk Assessment System

A Streamlit-based machine learning web app that predicts loan default risk using a Random Forest Classifier.
Users can input applicant details and instantly receive a Low-Risk (Approved) or High-Risk (Rejected) prediction with confidence scores.

📌 Features

🔍 Interactive Web UI built with Streamlit
🤖 Random Forest ML model trained on German Credit Data
📊 Predicts probability of loan repayment
🛠️ Includes smart insights such as high monthly payment warnings
🧮 Automatic feature engineering (Monthly Payment calculation) app
🧱 Encoded categorical variables exactly as in training (Job, Housing, Saving, Checking, Purpose)app

🗂️ Project Structure
├── app.py                     # Streamlit Web App
├── analysis.ipynb            # Exploratory Data Analysis & Training Notebook
├── german_credit_data.csv     # Dataset used for training
├── financial_risk_model.pkl   # Trained RandomForest model
└── README.md                  # Project Documentation

🚀 How to Run Locally
1. Clone this repository
git clone https://github.com/your-username/financial-risk-predictor.git
cd financial-risk-predictor

2. Install dependencies
pip install -r requirements.txt


Your requirements.txt should include:

streamlit
joblib
numpy
pandas
scikit-learn

3. Run the Streamlit app
streamlit run app.py


Your application will open in the browser at:

http://localhost:8501

🧠 Model Details

Algorithm: Random Forest Classifier
Dataset: German Credit Data
Target: Predict credit risk (Good / Bad)

Key Features Used:
Age
Sex
Job Level
Housing Status
Savings Balance
Checking Account Balance
Credit Amount
Loan Duration
Purpose of Loan
Monthly Payment (Engineered feature) 
app
A strict approval threshold of 65% model confidence is applied for safer risk management. 
app

🖼️ App Preview
Main Dashboard

Displays app overview and prediction results.
Sidebar Inputs
Users enter:
Age
Gender
Job Level
Housing
Savings & Checking Account status
Loan Amount & Duration
Loan Purpose
(All mapped to encoded values for the model.) 

app

📈 Prediction Logic

The model returns probability for Good (Low-Risk).
If Probability > 65% → Approved
Else → Rejected with confidence score
Additional warnings (Example: High Monthly Payment) appear when triggered. 
app

🛡️ Disclaimer

This project is for educational purposes and not intended for real-world financial decisions.

🤝 Contributing

Pull requests are welcome!
You may improve model accuracy, add visualizations, or build an API version.

⭐ Support

If you find this project useful, give it a ⭐ on GitHub!