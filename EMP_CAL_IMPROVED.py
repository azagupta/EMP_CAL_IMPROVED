import streamlit as st

# Function to calculate EMI
def calculate_emi(p, n, r):
    r = r / 100 / 12  # Convert annual rate to monthly rate
    emi = p * r * (1 + r)**n / ((1 + r)**n - 1)
    return emi

# Function to calculate Outstanding Loan Balance
def calculate_outstanding_balance(p, n, r, m):
    r = r / 100 / 12  # Convert annual rate to monthly rate
    outstanding_balance = p * ((1 + r)**n - (1 + r)**m) / ((1 + r)**n - 1)
    return outstanding_balance

# Streamlit App
def main():
    st.title("Improved EMI Calculator")

    # Sliders for inputs
    principal = st.slider("Principal Loan Amount", min_value=1000, max_value=100000, step=1000)
    tenure = st.slider("Loan Tenure (in years)", min_value=1, max_value=30)
    roi = st.slider("Rate of Interest (%)", min_value=1.0, max_value=20.0, step=0.1)
    period = st.slider("Period for Outstanding Balance (in months)", min_value=1, max_value=tenure * 12)

    # Calculate EMI and Outstanding Balance
    if st.button("Calculate EMI"):
        n = tenure * 12  # Convert tenure to months
        emi = calculate_emi(principal, n, roi)
        st.write(f"Monthly EMI: {emi:.3f}")

    if st.button("Calculate Outstanding Balance"):
        n = tenure * 12  # Convert tenure to months
        balance = calculate_outstanding_balance(principal, n, roi, period)
        st.write(f"Outstanding Loan Balance: {balance:.3f}")

if __name__ == "__main__":
    main()
