import streamlit as st

st.set_page_config(page_title="Pinnacle", page_icon="🚀")

st.title("Pinnacle - Investment Planner 🚀")
st.write("Get personalized investment advice based on your salary and risk appetite.")

# Input
salary = st.number_input("Enter your monthly salary (₹)", min_value=1000, step=1000)
invest_percent = st.slider("What % of your salary would you like to invest?", 5, 50, 20)
risk = st.radio("Select your risk appetite:", ["Low", "Medium", "High"])

if salary > 0:
    invest_amount = (salary * invest_percent) / 100
    st.subheader(f"You can invest ₹{invest_amount:,.2f} every month.")

    st.write("### Recommended Portfolio Allocation:")

    if risk == "Low":
        st.write("- 70% Mutual Funds (Debt/Index Funds)")
        st.write("- 20% Gold (ETFs or Sovereign Bonds)")
        st.write("- 10% Fixed Deposits")
    elif risk == "Medium":
        st.write("- 50% Mutual Funds (Balanced/Equity)")
        st.write("- 20% Stocks")
        st.write("- 20% Gold")
        st.write("- 10% Crypto (optional)")
    else:  # High risk
        st.write("- 60% Stocks")
        st.write("- 30% Mutual Funds (Equity/Index)")
        st.write("- 10% Crypto")

    st.info("👉 For detailed research, visit the Research Hub in the website.")
