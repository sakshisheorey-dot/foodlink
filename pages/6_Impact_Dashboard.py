import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

if "user" not in st.session_state:
    st.stop()

st.set_page_config(layout="wide")

st.title("📈 Impact Dashboard")

# KPI SECTION
c1, c2, c3, c4 = st.columns(4)

c1.metric("Food Saved", "1,250 kg", "+150")
c2.metric("Lives Impacted", "2,450", "+320")
c3.metric("NGOs Supported", "38", "+4")
c4.metric("CO₂ Reduced", "850 kg", "+72")

st.divider()

# FOOD SAVED TREND

col1, col2 = st.columns(2)

with col1:

    st.subheader("Food Saved Trend")

    df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Food Saved":[120,180,250,320,470,650]
    })

    fig = px.area(
        df,
        x="Month",
        y="Food Saved"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Lives Impacted")

    df2 = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Lives":[350,520,760,950,1450,2450]
    })

    fig2 = px.line(
        df2,
        x="Month",
        y="Lives",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# NGO DISTRIBUTION

col1, col2 = st.columns(2)

with col1:

    ngo = pd.DataFrame({
        "NGO":["Helping Hands",
               "Care Foundation",
               "Food For All",
               "Smile Trust"],
        "Donations":[35,25,22,18]
    })

    fig3 = px.bar(
        ngo,
        x="NGO",
        y="Donations"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col2:

    pie = px.pie(
        values=[40,30,20,10],
        names=[
            "Cooked Food",
            "Vegetables",
            "Bakery",
            "Others"
        ]
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )