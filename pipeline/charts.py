import plotly.express as px
import pandas as pd


def build_spending_chart(df: pd.DataFrame):
    fig = px.bar(df, x="date", y="amount", title="Spending by Date", color="category")
    return fig