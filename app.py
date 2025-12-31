import streamlit as st
from ui.chat import render_chat
from state.session import init_session_state
from ui.sidebar import render_sidebar
from memory.store import save_messages


#--------------------------------------------------
# Page Configuration
#--------------------------------------------------
st.set_page_config(
    page_title="AI Assistant",
    layout="wide"
    )

# Initialize session state
init_session_state()

# Render Sidebar
render_sidebar()

# Render Chat Area
render_chat()

# Persist chat after every rerun
save_messages(st.session_state.context_file, st.session_state.messages)