import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="Luma 🌙",
    page_icon="🌙",
    layout="centered"
)

# -------------------- CSS (Aesthetic Layer) --------------------

st.markdown("""
<style>

/* 🌌 FULL PAGE GRADIENT */
            
            
html, body, [class*="css"]  {
    background: radial-gradient(circle at top, #1e3a8a 100%, #0f172a 0%, #020617 100%) !important;
    color: #f8fafc !important;
}
    

/* Remove white app background */
.stApp {
    background: transparent !important;
}

  /* Assistant text */
[data-testid="stChatMessage"][aria-label="assistant"] {
    color: #f3e8ff !important;
}

/* User text */
[data-testid="stChatMessage"][aria-label="user"] {
    color: #3b0764 !important;
}
/* Force readable assistant text */
[data-testid="stChatMessage"][aria-label="assistant"] p {
    color: #3b0764 !important;
    opacity: 1 !important;
}

/* Force readable user text */
[data-testid="stChatMessage"][aria-label="user"] p {
    color: #000000 !important;
    opacity: 1 !important;
}

/* Also fix small faded text */
[data-testid="stChatMessage"] {
    color: #3b0764 !important;
}
       

/* Main container */
.block-container {
    max-width: 850px;
    margin: auto;
    padding: 40px;
    background: rgba(15, 23, 42, 0.9);
    border-radius: 28px;
    backdrop-filter: blur(18px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

/* Title styling */
h1 {
    color: #a21caf !important;   /* pinkish dark purple */
    text-shadow: 0 0 20px rgba(162,28,175,0.35);
}


/* Caption text */
.small-text {
    color: #f472b6 !important;
    opacity: 0.9;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    border-radius: 22px;
    padding: 16px;
    margin-bottom: 14px;
    font-size: 15px;
}

/* User bubble */
[data-testid="stChatMessage"][aria-label="user"] {
    background: linear-gradient(135deg, #ec4899, #f472b6);
    color: black !important;
    box-shadow: 0 6px 20px rgba(244,114,182,0.4);
}

/* Assistant bubble */
[data-testid="stChatMessage"][aria-label="assistant"] {
    background: rgba(255,255,255,0.08);
    color: #3b0764 !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
}

/* Input box */
div[data-baseweb="textarea"] {
    border-radius: 28px !important;
    background-color: rgba(15,23,42,0.9) !important;
}

textarea {
    color: #f8fafc !important;
}

/* Input focus */
textarea:focus {
    outline: none !important;
    box-shadow: 0 0 0 2px #f472b6 !important;
}

/* Remove white footer space */
footer {
    visibility: hidden;
}
            /* ===== GLOBAL TEXT RECOLOR SYSTEM ===== */

/* Base text (replaces black text) → Light Blue */
html, body, div, p, span, label {
    color: #7dd3fc !important;   /* light blue */
}

/* Assistant text (replaces white text) → Purple */
[data-testid="stChatMessage"][aria-label="assistant"] p {
    color: #3b0764 !important;   /* soft purple */
    opacity: 1 !important;
}

/* User text → Light Blue */
[data-testid="stChatMessage"][aria-label="user"] p {
    color: #7dd3fc !important;
    opacity: 1 !important;
}

/* Subtitle / faded / grey text → Pink */
.small-text,
.caption,
small,
[data-testid="stMarkdownContainer"] small {
    color: #f472b6 !important;   /* soft pink */
}

/* Input text */
textarea {
    color: #3b0764 !important;
}


</style>
""", unsafe_allow_html=True)



# -------------------- Header --------------------

st.markdown("""
<h1 style='
color:#f9a8d4;
font-weight:600;
letter-spacing:1px;
'>
🌙 Luma
</h1>
""", unsafe_allow_html=True)

st.markdown("<p class='small-text'>Your virtual friend  here. No judgments. how are you feeling today?. </p>", unsafe_allow_html=True)

# -------------------- Chat State --------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for sender, message in st.session_state.chat_history:
    if sender == "You":
        with st.chat_message("user", avatar="🌸"):
            st.markdown(message)
    else:
        with st.chat_message("assistant", avatar="🌙"):
            st.markdown(message)


# -------------------- Bottom Input --------------------

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    response = run_agent(user_input)

    st.session_state.chat_history.append(("Luma", response))
    with st.chat_message("assistant"):
        st.markdown(response)

