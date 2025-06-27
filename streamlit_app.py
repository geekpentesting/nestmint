import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="India Savings Planner", layout="centered")
st.title("🇮🇳 India Savings Planner - Real Use for Every Family")

st.header("🏦 Retirement Planning")
age = st.number_input("Your Current Age", min_value=18, max_value=65, value=33)
retirement_age = st.slider("Target Retirement Age", min_value=40, max_value=70, value=42)
desired_income = st.number_input("Desired Monthly Passive Income (₹) post retirement", min_value=1000, value=70000)

st.header("🎓 Education Planning for Children")
total_children = st.number_input("How many children do you want to plan for?", min_value=0, max_value=5, value=2, step=1)
inflation_toggle = st.toggle("Enable 5% annual inflation on education cost", value=False)

children = []
for i in range(total_children):
    st.subheader(f"Child {i+1}")
    child_age = st.number_input(f"→ Age of Child {i+1}", min_value=0, max_value=25, value=6, key=f"age{i}")
    goal_amount = st.number_input(f"→ Education Fund for Child {i+1} (₹)", min_value=100000, step=50000, value=5000000, key=f"goal{i}")
    children.append({
        "child_age": child_age,
        "goal_amount": goal_amount,
        "inflation": inflation_toggle
    })

if st.button("Calculate Savings Plan"):
    try:
        with st.spinner("Calculating realistic SIP plan for your future..."):
            #res = requests.post("http://localhost:8000/calculate", json={
            res = requests.post("https://nestmint-api.onrender.com/calculate", json={
                "current_age": age,
                "retirement_age": retirement_age,
                "desired_income": desired_income,
                "children": children
            })

        if res.status_code == 200:
            result = res.json()
            st.success("✅ Plan calculated successfully!")

            st.subheader("📊 Per Child Education Plan")
            df_child = pd.DataFrame(result["children"])
            st.dataframe(df_child)

            st.subheader("🏖️ Retirement Plan")
            st.write(f"**Corpus Required:** ₹{result['retirement']['required_corpus']:,}")
            st.write(f"**Monthly SIP:** ₹{result['retirement']['monthly_sip']:,}")
            st.write(f"**Income Period:** {result['retirement']['retirement_years']} years")

            st.subheader("🧾 Summary")
            st.write(f"**Total Corpus Needed:** ₹{result['summary']['total_corpus']:,}")
            st.write(f"**Estimated Total Monthly SIP:** ₹{result['summary']['total_sip']:,}")

            if st.download_button("📥 Download Summary (Excel)", df_child.to_csv(index=False).encode('utf-8'), file_name="education_plan.csv"):
                st.info("Excel downloaded with per-child education plan.")
        else:
            st.error(f"❌ Error from backend: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"🚨 Could not reach the backend. Is FastAPI running?\nError: {e}")
