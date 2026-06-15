import streamlit as st
import plotly.express as px
import pandas as pd

from components import load_css

load_css()

st.title("📊 Impact Dashboard")

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Food Saved",
        "1250 kg"
    )

with c2:
    st.metric(
        "NGOs Helped",
        "28"
    )

with c3:
    st.metric(
        "Lives Impacted",
        "3500"
    )

data = pd.DataFrame({
    "Month":[
        "Jan","Feb","Mar",
        "Apr","May"
    ],
    "Food Saved":[
        100,200,350,
        500,700
    ]
})

fig = px.line(
    data,
    x="Month",
    y="Food Saved"
)

st.plotly_chart(
    fig,
    use_container_width=True
)