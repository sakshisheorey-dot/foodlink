import streamlit as st
from database import get_requests

st.title("📥 NGO Requests")

requests = get_requests()

pending, accepted, rejected = st.columns(3)

with pending:

    st.subheader("🟡 Pending")

    for req in requests:

        if req[3] == "Pending":

            with st.container(border=True):

                st.write(
                    f"Food ID: {req[1]}"
                )

                st.write(
                    f"NGO ID: {req[2]}"
                )

                st.button(
                    f"Accept {req[0]}"
                )

                st.button(
                    f"Reject {req[0]}"
                )

with accepted:

    st.subheader("🟢 Accepted")

with rejected:

    st.subheader("🔴 Rejected")