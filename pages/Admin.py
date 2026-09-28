import sqlite3
import pandas as pd
import streamlit as st

st.title("Admin panel")

# Simple password gate. Put ADMIN_PASSWORD in .streamlit/secrets.toml
if not st.session_state.get("is_admin"):
    pw = st.text_input("Password", type="password")
    if st.button("Log in"):
        if pw == st.secrets["ADMIN_PASSWORD"]:
            st.session_state["is_admin"] = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()

with sqlite3.connect("responses.db") as con:
    df = pd.read_sql("SELECT * FROM visits ORDER BY ts DESC", con)

st.metric("Total responses", len(df))
st.bar_chart(df["role"].value_counts())
st.dataframe(df)
