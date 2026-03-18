import streamlit as st
import random
import time

# --- 1. PAGE CONFIG & DATA ---
st.set_page_config(page_title="Professional Quiz Portal", page_icon="🎓", layout="centered")

# Quiz Data organized by category
QUIZ_DATA = {
    "🌍 Geography": [
        {"q": "Capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "a": "Delhi"},
        {"q": "Largest desert?", "options": ["Sahara", "Arctic", "Gobi", "Thar"], "a": "Arctic"}
    ],
    "🌐 Technology": [
        {"q": "What does CPU stand for?", "options": ["Process Unit", "Processing Unit", "Personal Unit"], "a": "Processing Unit"},
        {"q": "Creator of iPhone?", "options": ["Apple", "Google", "Microsoft"], "a": "Apple"}
    ]
}

# --- 2. INITIALIZE SESSION STATE ---
# This "remembers" the user even when the script reruns
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'page' not in st.session_state:
    st.session_state.page = "login"
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = []
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- 3. HELPER FUNCTIONS ---
def logout():
    st.session_state.auth_status = False
    st.session_state.page = "login"
    st.session_state.user_name = ""
    st.rerun()

def start_quiz(category):
    questions = QUIZ_DATA[category].copy()
    random.shuffle(questions)
    st.session_state.current_quiz = questions
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.page = "quiz"
    st.rerun()

# --- 4. NAVIGATION / ROUTING ---

# PAGE: LOGIN
if st.session_state.page == "login":
    st.title("🔐 Quiz Portal Login")
    name = st.text_input("Enter your name")
    password = st.text_input("Enter password", type="password", help="Hint: password123")
    
    if st.button("Enter Portal"):
        if name and password == "password123":
            st.session_state.user_name = name
            st.session_state.auth_status = True
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Please enter a name and the correct password.")

# PAGE: DASHBOARD
elif st.session_state.page == "dashboard":
    st.title(f"👋 Welcome, {st.session_state.user_name}!")
    st.subheader("Select a Category to Start:")
    
    for category in QUIZ_DATA.keys():
        if st.button(f"Start {category}", use_container_width=True):
            start_quiz(category)
    
    st.divider()
    if st.button("Log Out"):
        logout()

# PAGE: QUIZ
elif st.session_state.page == "quiz":
    questions = st.session_state.current_quiz
    idx = st.session_state.q_idx
    
    st.progress((idx) / len(questions))
    st.write(f"### Question {idx + 1} of {len(questions)}")
    st.write(f"**{questions[idx]['q']}**")
    
    # Selection
    answer = st.radio("Choose your answer:", questions[idx]['options'], index=None, key=f"q_{idx}")
    
    if st.button("Submit Answer ➡️"):
        if answer:
            if answer == questions[idx]['a']:
                st.session_state.score += 1
                st.toast("Correct! ✨")
            else:
                st.toast("Wrong! ❌")
            
            # Move to next or finish
            if idx + 1 < len(questions):
                st.session_state.q_idx += 1
                st.rerun()
            else:
                st.session_state.page = "results"
                st.rerun()
        else:
            st.warning("Please select an option first!")

# PAGE: RESULTS
elif st.session_state.page == "results":
    st.title("🎯 Quiz Completed!")
    total = len(st.session_state.current_quiz)
    score = st.session_state.score
    percent = (score/total) * 100
    
    st.balloons()
    st.metric(label="Final Score", value=f"{score} / {total}", delta=f"{percent}%")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    
    if st.button("Log Out"):
        logout()
