import streamlit as st
import time

# --- 1. CONFIG & GATE DATA ---
st.set_page_config(page_title="GATE 2026 Mock Portal", page_icon="📝", layout="wide")

# (Data truncated for brevity - use the 10 subjects from previous code here)
GATE_DATA = {
    "🖥️ Operating Systems": [
        {"q": "Which is NOT shared by threads of the same process?", "options": ["Stack", "Address Space", "File Descriptors", "Global Variables"], "a": "Stack"},
        # ... add other 4 questions here
    ],
    # ... add all other 9 subjects here
}

# --- 2. SESSION STATE ---
if 'users' not in st.session_state: st.session_state.users = {}
if 'page' not in st.session_state: st.session_state.page = "auth"
if 'answers' not in st.session_state: st.session_state.answers = {}

def navigate(p):
    st.session_state.page = p
    st.rerun()

# --- 3. MOCK TEST MODULES ---

# AUTHENTICATION
if st.session_state.page == "auth":
    st.title("🛡️ GATE Mock Test Portal")
    t1, t2 = st.tabs(["Login", "Register"])
    with t1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.user = u
                navigate("dash")
            else: st.error("Invalid credentials")
    with t2:
        nu = st.text_input("New User")
        np = st.text_input("New Pass", type="password")
        if st.button("Create Account"):
            st.session_state.users[nu] = np
            st.success("Registered! Go to Login.")

# DASHBOARD
elif st.session_state.page == "dash":
    st.title(f"Welcome, {st.session_state.user}")
    st.info("Select a subject. You will have 5 minutes (300s) to complete 5 questions.")
    for subj in GATE_DATA.keys():
        if st.button(subj, use_container_width=True):
            st.session_state.subj = subj
            st.session_state.start_time = time.time() # Start the clock
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.session_state.user_answers = [None] * 5
            navigate("exam")

# EXAM MODE (Timed)
elif st.session_state.page == "exam":
    subj = st.session_state.subj
    idx = st.session_state.q_idx
    q_set = GATE_DATA[subj]
    
    # --- TIMER LOGIC ---
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 300 - int(elapsed))
    
    col1, col2 = st.columns([4, 1])
    with col2:
        st.metric("⏳ Time Left", f"{remaining//60}:{remaining%60:02d}")
    
    if remaining <= 0:
        st.warning("Time's up!")
        time.sleep(2)
        navigate("results")

    # --- QUESTION UI ---
    st.subheader(f"Question {idx+1}")
    st.write(f"### {q_set[idx]['q']}")
    
    # We use index to "remember" the user's choice if they go back/forth
    current_choice = st.session_state.user_answers[idx]
    choice = st.radio("Select Option:", q_set[idx]['options'], 
                      index=q_set[idx]['options'].index(current_choice) if current_choice else None)
    
    st.session_state.user_answers[idx] = choice

    c1, c2, c3 = st.columns(3)
    with c1:
        if idx > 0 and st.button("⬅️ Previous"):
            st.session_state.q_idx -= 1
            st.rerun()
    with c3:
        if idx < 4:
            if st.button("Next ➡️"):
                st.session_state.q_idx += 1
                st.rerun()
        else:
            if st.button("🏁 Submit Test"):
                navigate("results")

# RESULTS & REVIEW
elif st.session_state.page == "results":
    st.title("🎯 Performance Analysis")
    subj = st.session_state.subj
    q_set = GATE_DATA[subj]
    user_ans = st.session_state.user_answers
    
    score = sum(1 for i in range(5) if user_ans[i] == q_set[i]['a'])
    st.metric("Final Score", f"{score}/5")

    st.write("### 📝 Review Your Answers")
    for i in range(5):
        with st.expander(f"Question {i+1}: {q_set[i]['q']}"):
            st.write(f"Your Answer: {user_ans[i]}")
            st.write(f"Correct Answer: {q_set[i]['a']}")
            if user_ans[i] == q_set[i]['a']:
                st.success("Correct")
            else:
                st.error("Incorrect")

    if st.button("Return to Dashboard"):
        navigate("dash")
