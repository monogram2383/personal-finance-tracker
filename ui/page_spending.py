import pandas as pd
import streamlit as st

from pipeline.charts import build_spending_chart
from utils.sql_utils import SQL_ENGINE

# init data and charts
df = pd.read_sql("card_transactions", SQL_ENGINE)
df["date"] = df["date"].dt.to_period('M').dt.start_time
fig = build_spending_chart(df)

# fill page
st.plotly_chart(fig, use_container_width=True)
