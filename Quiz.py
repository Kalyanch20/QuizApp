import streamlit as st
import random

# --- 1. CONFIG & DATA ---
st.set_page_config(page_title="Quiz Portal", page_icon="🎓")

# Sample Data
QUIZ_DATA = {
    "🌍 Geography": [
        {"q": "Capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "a": "Delhi"},
        {"q": "Largest desert?", "options": ["Sahara", "Arctic", "Gobi", "Thar"], "a": "Arctic"}
    ],
    "🌐 Technology": [
        {"q": "What does CPU stand for?", "options": ["Process Unit", "Processing Unit", "Personal Unit"], "a": "Processing Unit"}
    ]
}

# --- 2. SESSION STATE (The "Brain") ---
if 'users' not in st.session_state:
    st.session_state.users = {}  # Format: {"username": "password"}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'page' not in st.session_state:
    st.session_state.page = "auth" # Start at Login/Signup screen

# --- 3. AUTHENTICATION FUNCTIONS ---
def create_account(user, pwd):
    if user in st.session_state.users:
        st.error("User already exists!")
    elif user and pwd:
        st.session_state.users[user] = pwd
        st.success("Account created! Now please Login.")
    else:
        st.warning("Fields cannot be empty.")

def login(user, pwd):
    if user in st.session_state.users and st.session_state.users[user] == pwd:
        st.session_state.logged_in = True
        st.session_state.current_user = user
        st.session_state.page = "dashboard"
        st.rerun()
    else:
        st.error("Invalid username or password")

# --- 4. NAVIGATION ---

# PAGE: AUTHENTICATION (Login & Signup)
if st.session_state.page == "auth":
    st.title("🎓 Quiz Portal")
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    
    with tab1:
        u_log = st.text_input("Username", key="l_user")
        p_log = st.text_input("Password", type="password", key="l_pwd")
        if st.button("Login"):
            login(u_log, p_log)
            
    with tab2:
        u_reg = st.text_input("Choose Username", key="r_user")
        p_reg = st.text_input("Choose Password", type="password", key="r_pwd")
        if st.button("Register"):
            create_account(u_reg, p_reg)

# PAGE: DASHBOARD
elif st.session_state.page == "dashboard":
    st.title(f"Welcome, {st.session_state.current_user}!")
    st.subheader("Select Category")
    for cat in QUIZ_DATA.keys():
        if st.button(cat, use_container_width=True):
            st.session_state.selected_cat = cat
            st.session_state.page = "quiz"
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.rerun()
            
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "auth"
        st.rerun()

# PAGE: QUIZ 
elif st.session_state.page == "quiz":
    cat = st.session_state.selected_cat
    questions = QUIZ_DATA[cat]
    idx = st.session_state.q_idx
    
    st.write(f"### {cat}")
    st.write(f"**Question {idx+1}:** {questions[idx]['q']}")
    ans = st.radio("Pick one:", questions[idx]['options'], index=None)
    
    if st.button("Submit"):
        if ans == questions[idx]['a']:
            st.session_state.score += 1
        
        if idx + 1 < len(questions):
            st.session_state.q_idx += 1
            st.rerun()
        else:
            st.session_state.page = "results"
            st.rerun()

# PAGE: RESULTS
elif st.session_state.page == "results":
    st.title("Done!")
    st.write(f"Final Score: {st.session_state.score}")
    if st.button("Back to Home"):
        st.session_state.page = "dashboard"
        st.rerun()
