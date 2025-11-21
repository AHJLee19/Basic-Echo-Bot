import streamlit as st

# Setting the title of the wep app
st.title("Echo Bot")

# Initializing the chat history to keep track of messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun

