import streamlit as st

st.title("🏠 Home Dashboard")

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Food Saved","2500 kg")

with c2:
    st.metric("NGOs Helped","56")

with c3:
    st.metric("Lives Impacted","8200")

st.divider()

st.subheader("Quick Actions")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.button("➕ Post Food")

with col2:
    st.button("🏢 Explore NGOs")

with col3:
    st.button("🚚 Track Donation")

with col4:
    st.button("📊 Dashboard")

st.divider()

st.subheader("Recent Activity")

st.success("Donation delivered")
st.info("NGO accepted request")
st.success("Food pickup completed")