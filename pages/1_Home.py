import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🏠 FoodLink Dashboard")

# KPI CARDS
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Food Saved", "1,250 kg", "+150")

with c2:
    st.metric("NGOs Helped", "38", "+5")

with c3:
    st.metric("Lives Impacted", "2,450", "+320")

with c4:
    st.metric("CO₂ Prevented", "850 kg", "+72")

st.divider()

left, right = st.columns([2,1])

with left:

    st.subheader("Impact Trend")

    df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Food Saved":[150,200,260,390,480,650]
    })

    fig = px.line(
        df,
        x="Month",
        y="Food Saved",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("Recent Activity")

    st.success("🍱 40kg food delivered")
    st.success("🥗 NGO accepted donation")
    st.success("🚚 Volunteer picked up food")
    st.success("🌱 New donor joined")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Quick Actions")

    st.page_link(
        "pages/2_Post_Food.py",
        label="➕ Post Surplus Food"
    )

    st.page_link(
        "pages/3_Available_Surplus.py",
        label="🗺️ Browse Food"
    )

    st.page_link(
        "pages/7_Explore_NGOs.py",
        label="🏢 Explore NGOs"
    )

with col2:

    st.subheader("Upcoming Pickups")

    st.info("12:30 PM - Care Foundation")
    st.info("2:15 PM - Helping Hands NGO")
    st.info("5:00 PM - Food For All")