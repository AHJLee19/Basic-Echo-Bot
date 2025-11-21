import streamlit as st

# Setting the title of the wep app
st.title("Echo Bot")

# Initializing the chat history to keep track of messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Bot reaction to user input
if prompt := st.chat_input("What would you like to say?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

