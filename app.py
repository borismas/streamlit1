import datetime
import sqlite3
import streamlit as st

DB = "responses.db"

def save_choice(role):
    with sqlite3.connect(DB) as con:
        con.execute("CREATE TABLE IF NOT EXISTS visits (ts TEXT, role TEXT)")
        con.execute(
            "INSERT INTO visits VALUES (?, ?)",
            (datetime.datetime.now().isoformat(timespec="seconds"), role),
        )

st.title("Welcome to my website.")

# index=None + placeholder replaces your dummy "Select the option..." entry
role = st.selectbox(
    "What best describes you?",
    ["Software developer", "Web developer", "Visitor"],
    index=None,
    placeholder="Select the option that describes you best.",
)

# Button is disabled until something is chosen
if st.button("That's me!", disabled=role is None):
    st.session_state["role"] = role   # remember it for this session
    save_choice(role)                 # send it to the admin panel's data
    st.switch_page("pages/Home.py")   # go to the next page
