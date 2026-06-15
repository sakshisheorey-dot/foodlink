import streamlit as st
from components import load_css

load_css()

st.title("🚚 Track Donation")

st.markdown("""
### Donation Timeline

✅ Posted

⬇️

✅ Request Accepted

⬇️

🟡 Picked Up

⬇️

⚪ Delivered
""")

st.progress(0.75)

st.info("""
NGO:
Helping Hands

Driver:
Rahul

ETA:
25 minutes
""")