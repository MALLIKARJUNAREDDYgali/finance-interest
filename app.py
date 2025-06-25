import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
from babel.numbers import format_currency

st.title("💰 Indian Flat Interest Calculator (1 Rupee = 1% Style)")

# Format ₹ in Indian comma system
def format_inr(amount):
    return format_currency(amount, 'INR', locale='en_IN')

# User Inputs
amount = st.number_input("Enter Total Amount (₹)", min_value=1.0, step=1.0, format="%.2f")
interest_rate = st.number_input("Interest Rate (₹ per ₹100 per month)", 
                               min_value=0.01, 
                               max_value=100.0,
                               step=0.5,
                               value=1.0,
                               format="%.2f",
                               help="Common practice: 1 means ₹1 interest per ₹100 per month (1% monthly)")

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Explanation of common practice
st.info("💡 In common Indian practice: '1 Rupee Interest' means ₹1 per ₹100 per month (1% monthly interest)")

# Validation
if start_date > end_date:
    st.error("❌ End date must be after start date.")
else:
    # Calculate duration
    total_days = (end_date - start_date).days
    duration = relativedelta(end_date, start_date)
    
    st.write(f"📅 Total Days: `{total_days}`")
    st.write(f"🗓️ Duration: `{duration.years}` years, `{duration.months}` months, `{duration.days}` days")

    # Core Calculation (using common practice)
    monthly_interest_rate = interest_rate / 100  # Convert ₹1 per ₹100 to decimal (1%)
    monthly_interest = amount * monthly_interest_rate
    daily_interest = monthly_interest / 30  # Assuming 30-day month
    total_interest = daily_interest * total_days
    total_payable = amount + total_interest
    
    # Calculate effective rates
    effective_monthly_rate = monthly_interest_rate * 100
    effective_annual_rate = monthly_interest_rate * 12 * 100

    # Output Results
    st.markdown("### 💸 Interest Summary")
    st.write(f"🔢 **Principal Amount**: {format_inr(amount)}")
    st.write(f"📈 **Interest Rate**: ₹{interest_rate:.2f} per ₹100 per month ({effective_monthly_rate:.2f}% monthly)")
    st.write(f"📊 **Effective Annual Rate**: {effective_annual_rate:.2f}%")
    st.write(f"💰 **Monthly Interest**: {format_inr(monthly_interest)}")
    st.write(f"📆 **Total Interest for {total_days} days**: {format_inr(total_interest)}")
    st.success(f"🧾 **Total Payable (Principal + Interest)**: {format_inr(total_payable)}")
    
    # Warning for high interest rates
    if interest_rate > 3:
        st.warning("⚠️ High interest rate! This is above normal lending rates.")