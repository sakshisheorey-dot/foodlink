import streamlit as st
from database import get_requests
from database import (
    update_request_status
)

import streamlit as st
from database import get_requests

# Authentication Check
if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# NGO Check
if st.session_state.user["role"] != "NGO":
    st.warning("This page is only available for NGOs")
    st.stop()

st.title("📥 NGO Requests")

# Rest of your code...

if "user" not in st.session_state:
    st.stop()

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

if st.button(
    f"Accept {req[0]}"
):

    update_request_status(
        req[0],
        "Accepted"
    )

    st.rerun()

if st.button(
    f"Reject {req[0]}"
):

    update_request_status(
        req[0],
        "Rejected"
    )

    st.rerun()