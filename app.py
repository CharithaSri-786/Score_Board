import streamlit as st
import pandas as pd

st.title("🏏 College Sports Meet Scoreboard")

st.write("Live score tracking for sports events")

# create storage
if "teams" not in st.session_state:
    st.session_state.teams = []

# sidebar menu
menu = st.sidebar.selectbox(
    "Menu",
    ["Add Score", "View Scoreboard", "Score Chart"]
)

# Add Score

if menu == "Add Score":

    st.header("Add Team Score")

    team = st.text_input("Team Name")
    event = st.text_input("Event Name")
    score = st.number_input("Score", min_value=0)

    if st.button("Add Score"):

        data = {
            "Team": team,
            "Event": event,
            "Score": score
        }

        st.session_state.teams.append(data)

        st.success("Score added successfully")



# View Scoreboard

elif menu == "View Scoreboard":

    st.header("Scoreboard")

    if st.session_state.teams:

        df = pd.DataFrame(st.session_state.teams)

        st.table(df)

        leaderboard = df.groupby("Team")["Score"].sum().reset_index()

        leaderboard = leaderboard.sort_values(
            by="Score",
            ascending=False
        )

        st.subheader("Leaderboard")

        st.table(leaderboard)

    else:
        st.write("No scores added yet")



# Score Chart

elif menu == "Score Chart":

    st.header("Team Score Chart")

    if st.session_state.teams:

        df = pd.DataFrame(st.session_state.teams)

        chart_data = df.groupby("Team")["Score"].sum()

        st.bar_chart(chart_data)

    else:
        st.write("No data to show")