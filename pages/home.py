import streamlit as st

# If someone lands here directly, send them back to choose first
if "role" not in st.session_state:
    st.switch_page("app.py")

st.title(f"Welcome, {st.session_state['role']}!")

if st.session_state["role"] == "Software developer":
    st.write("Here's my code and projects...")
elif st.session_state["role"] == "Web developer":
    st.write("Here's my front-end work...")
else:
    st.write("Feel free to look around!")
