import streamlit as st
from state.session import add_message
from llm.streaming import generate_streaming_response
from memory.store import load_messages
import constants.constants as constants


def render_chat():
    """
    Docstring for render_chat
    """
    # Display existing messages
    for msg in st.session_state.messages:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

    # User input box
    user_input = st.chat_input("Type your message here...")

    if user_input and not st.session_state.pending_response:
        
        #Add user message
        add_message("user",user_input)
        with st.chat_message('user'):
            st.markdown(st.session_state.messages[-1]['content'])

        #Prepare assistant placeholder message
        add_message("assistant", "")
        st.session_state.pending_response = True

        # Stream assistant response
        with st.chat_message('assistant'):
            stream_assistant_response()


def stream_assistant_response():
    """
    Docstring for stream_assistant_response
    """

    placeholder = st.empty()
    asssistant_text = ""
    for token in generate_streaming_response(
        user_prompt=st.session_state.messages[-4:-1],
        system_prompt=constants.PERSONALITIES[st.session_state.personality]
        ):

        asssistant_text += token
        st.session_state.messages[-1]['content'] = asssistant_text
        placeholder.markdown(asssistant_text)

    st.session_state.pending_response = False

