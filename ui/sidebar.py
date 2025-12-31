import streamlit as st
from state.session import reset_chat
from datetime import datetime
from memory.store import save_messages
import constants.constants as constants


def render_sidebar():
    """
    Docstring for render_sidebar
    """

    st.sidebar.title("Settings")

    personality_old = st.session_state.personality

    # Personality Selector
    selected_personality = st.sidebar.selectbox(
        "Select Personality",
        list(constants.PERSONALITIES.keys())
    )
    
    st.session_state.personality = selected_personality
    if selected_personality != personality_old:
        st.rerun()

    # Clear Chat
    if st.sidebar.button("Clear Chat"):
        reset_chat()
    
    # Export History
    if st.sidebar.button("Export Chat History"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"chat_export_{timestamp}.json"
        try:
            save_messages(file_name,st.session_state.messages)
            st.sidebar.success(f"Exported as {file_name}")
        except Exception as e:
            st.sidebar.error("Export Failed.")
            st.write(e)