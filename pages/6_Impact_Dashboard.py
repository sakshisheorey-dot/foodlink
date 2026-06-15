def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_impact_metrics

st.set_page_config(
    layout="wide"
)

st.title("📊 Impact Dashboard")

df = get_impact_metrics()

if df.empty:

    st.warning(
        "No donation data available."
    )

    st.stop()

total_food = df["quantity"].sum()

estimated_meals = (
    total_food * 2
)

lives_impacted = (
    estimated_meals
)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Food Saved",
        f"{total_food} kg"
    )

with c2:
    st.metric(
        "Meals Generated",
        int(estimated_meals)
    )

with c3:
    st.metric(
        "Lives Impacted",
        int(lives_impacted)
    )

st.divider()

col1,col2 = st.columns(2)

# -------------------------
# Food Category Pie Chart
# -------------------------

with col1:

    fig = px.pie(
        df,
        names="category",
        values="quantity",
        title="Food Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# Quantity Bar Chart
# -------------------------

with col2:

    category_df = (
        df.groupby("category")
        ["quantity"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_df,
        x="category",
        y="quantity",
        title="Food by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader(
    "Donation Dataset"
)

st.dataframe(
    df,
    use_container_width=True
)