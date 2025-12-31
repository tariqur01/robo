import streamlit as st
from pathlib import Path
from memory.store import load_messages
import constants.constants as constants


DEFAULT_PERSONALITY = list(constants.PERSONALITIES.keys())[0]
DEFAULT_CONTEXT_FILE = f"chat_history_{DEFAULT_PERSONALITY}.json"


def init_session_state():
    """
    Docstring for init_session_state
    """

    if 'personality' not in st.session_state:
        st.session_state.personality = DEFAULT_PERSONALITY
        st.session_state.context_file = DEFAULT_CONTEXT_FILE
    else:
        st.session_state.context_file = f"chat_history_{st.session_state.personality}.json"

    st.session_state.messages = load_messages(st.session_state.context_file)
    
    if 'pending_response' not in st.session_state:
        st.session_state.pending_response = False


def reset_chat():
    """
    Docstring for reset_chat
    """

    st.session_state.messages = []
    st.session_state.pending_response = False
    path = Path(st.session_state.context_file)
    if path.exists():
        path.unlink()


def add_message(role: str, content: str):
    """
    Docstring for add_message
    """

    st.session_state.messages.append({
        'role': role,
        'content': content
    })
    