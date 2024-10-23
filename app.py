import streamlit as st

spending_page = st.Page("ui/page_spending.py", title="Spending", icon=':material/payments:')

pg = st.navigation([spending_page])
st.set_page_config(page_title="Spending Page", layout="wide")

pg.run()