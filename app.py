import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ==========================================
# 1. SETUP & LOAD MODEL
# ==========================================
st.set_page_config(page_title="Risk Predictor", page_icon="🏦", layout="wide")

try:
    model = joblib.load('financial_risk_model.pkl')
except FileNotFoundError:
    st.error("Model file not found! Please run 'train_model.py' first.")
    st.stop()

# ==========================================
# 2. UI DESIGN (SideBar & Main)
# ==========================================
st.title("🏦 AI Financial Risk Assessment")
st.markdown("""
This system uses a **Random Forest Classifier** to predict whether a loan applicant 
is likely to repay (Low Risk) or default (High Risk).
""")

st.sidebar.header("📝 Applicant Profile")

# --- INPUTS ---
# We map the text inputs back to the Numbers the model learned in train_model.py

# 1. AGE
age = st.sidebar.slider("Age", 18, 75, 30)

# 2. SEX (Mapping: female=0, male=1)
sex = st.sidebar.radio("Gender", ["Male", "Female"])
sex_val = 1 if sex == "Male" else 0

# 3. JOB (Mapping: 0-3 scale)
job = st.sidebar.selectbox("Job Skill Level", [0, 1, 2, 3], help="0=Unskilled, 3=Highly Skilled")

# 4. HOUSING (Mapping based on training output: free=0, own=1, rent=2)
housing = st.sidebar.selectbox("Housing Status", ["Own", "Rent", "Free"])
housing_dict = {"Free": 0, "Own": 1, "Rent": 2}
housing_val = housing_dict[housing]

# 5. SAVINGS (Mapping: little=0, moderate=1, quite rich=2, rich=3)
# Note: 'rich' was mapped to different ints in training, we approximate for simplicity
saving = st.sidebar.selectbox("Savings Balance", ["Little", "Moderate", "High", "Very High"])
saving_dict = {"Little": 0, "Moderate": 1, "High": 2, "Very High": 3}
saving_val = saving_dict[saving]

# 6. CHECKING ACCOUNT (Mapping: little=0, moderate=1, rich=2)
checking = st.sidebar.selectbox("Checking Account Balance", ["Little", "Moderate", "High"])
checking_dict = {"Little": 0, "Moderate": 1, "High": 2}
checking_val = checking_dict[checking]

# 7. CREDIT AMOUNT
credit_amount = st.sidebar.number_input("Loan Amount ($)", 500, 20000, 5000, step=100)

# 8. DURATION
duration = st.sidebar.slider("Loan Duration (Months)", 6, 72, 24)

# 9. PURPOSE (Mapping based on alphabetical sort in training)
purpose = st.sidebar.selectbox("Purpose", ["Business", "Car", "Education", "Furniture", "Radio/TV", "Repairs", "Vacation"])
# These values match the LabelEncoder alphabetical output
purpose_dict = {
    "Business": 0, "Car": 1, "Domestic Appliances": 2, "Education": 3, 
    "Furniture": 4, "Radio/TV": 5, "Repairs": 6, "Vacation": 7
}
# Safe fallback if key is missing
purpose_val = purpose_dict.get(purpose, 4) 

# 10. FEATURE ENGINEERING (Must match training!)
monthly_payment = credit_amount / duration

# ==========================================
# 3. PREDICTION LOGIC
# ==========================================
# Order must match X_train columns: 
# [Age, Sex, Job, Housing, Saving, Checking, Credit amount, Duration, Purpose, Monthly_Payment]

input_data = np.array([[
    age, sex_val, job, housing_val, saving_val, checking_val, 
    credit_amount, duration, purpose_val, monthly_payment
]])

st.markdown("---")
st.subheader("Prediction Result")

if st.sidebar.button("Analyze Risk"):
    with st.spinner("Calculating Risk Score..."):
        # Get the probability (Confidence score)
        # probability[0][0] is probability of BAD
        # probability[0][1] is probability of GOOD
        probs = model.predict_proba(input_data)
        prob_good = probs[0][1]
        
    st.markdown("---")
    
    # STRICTER RULE: Only approve if the model is > 65% sure
    # (Standard is 0.50, we are raising it to 0.65)
    THRESHOLD = 0.65 
    
    if prob_good > THRESHOLD:
        st.success(f"✅ **LOW RISK (Approved)**")
        st.metric("Confidence Score", f"{prob_good*100:.1f}%")
        st.write("This applicant meets the strict criteria for a loan.")
    else:
        st.error(f"🚨 **HIGH RISK (Rejected)**")
        st.metric("Confidence Score", f"{prob_good*100:.1f}%")
        st.caption(f"Note: The model was only {prob_good*100:.1f}% sure. We require {THRESHOLD*100}% confidence.")
        st.write("This applicant is too risky for our current standards.")
        
        # Smart Insights
        if monthly_payment > 300:
            st.warning(f"⚠️ Monthly Payment is too high (${monthly_payment:.0f})")