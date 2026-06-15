import streamlit as st
from components import load_css, impact_card

st.set_page_config(
    page_title="FoodLink",
    layout="wide"
)

load_css()

st.markdown("""
<h2>Good Morning 👋</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Today's Impact
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    impact_card("120 kg","Food Saved")

with c2:
    impact_card("8","NGOs Helped")

with c3:
    impact_card("240","Lives Impacted")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Quick Actions
</div>
""", unsafe_allow_html=True)

a1,a2,a3,a4 = st.columns(4)

with a1:
    st.button("➕ Post Food", use_container_width=True)

with a2:
    st.button("🏢 NGOs", use_container_width=True)

with a3:
    st.button("🚚 Track", use_container_width=True)

with a4:
    st.button("📊 Impact", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Recent Activity
</div>
""", unsafe_allow_html=True)

activities = [
    "20kg food donated to Helping Hands NGO",
    "15kg vegetables claimed by Food For All",
    "Donation delivered successfully"
]

for item in activities:
    st.success(item)