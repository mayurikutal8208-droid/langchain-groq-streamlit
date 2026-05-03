import streamlit as st
from app.chains import get_chain
# import json
import os
from app.chains import get_chain

# Page config
st.set_page_config(page_title="Tech Chatbot", page_icon="🤖")

st.title("🤖 Alex - Tech AI Assistant")

# Initialize chain
@st.cache_resource
def load_chain():
    return get_chain()

chain = load_chain()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your tech question...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from chain
    response = chain.invoke({"input": user_input})

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": response})