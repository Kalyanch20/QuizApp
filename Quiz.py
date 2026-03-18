import streamlit as st
import random
import time

# ✅ 1. Page Configuration
st.set_page_config(page_title="Multi-Topic Quiz App", page_icon="🧠")

# ✅ 2. Quiz Data
if 'quiz_data' not in st.session_state:
    data = [
        {"category": "🌍 Geography", "question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
        {"category": "🌍 Geography", "question": "Which river is known as the Ganga of the South?", "options": ["Yamuna", "Narmada", "Godavari", "Krishna"], "answer": "Godavari"},
        {"category": "🌍 Geography", "question": "Which is the largest desert in the world?", "options": ["Sahara", "Arctic", "Gobi", "Thar"], "answer": "Arctic"},
        {"category": "🌍 Geography", "question": "Mount Everest lies in which mountain range?", "options": ["Andes", "Rockies", "Himalayas", "Alps"], "answer": "Himalayas"},
        {"category": "🌍 Geography", "question": "Which continent has the most countries?", "options": ["Europe", "Asia", "Africa", "South America"], "answer": "Africa"},
        {"category": "☀️ Health & Science", "question": "Which vitamin do we get from sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
        {"category": "☀️ Health & Science", "question": "What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "NaCl"], "answer": "H2O"},
        {"category": "☀️ Health & Science", "question": "Which organ purifies blood in the human body?", "options": ["Heart", "Kidney", "Liver", "Lungs"], "answer": "Kidney"},
        {"category": "☀️ Health & Science", "question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"category": "☀️ Health & Science", "question": "What part of the cell contains DNA?", "options": ["Nucleus", "Cytoplasm", "Ribosome", "Mitochondria"], "answer": "Nucleus"},
        {"category": "🌐 Technology", "question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "High Tech Transfer Protocol", "Home Tool Transfer Process", "Hyperlink and Text Transmission Protocol"], "answer": "HyperText Transfer Protocol"},
        {"category": "🌐 Technology", "question": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Programming Unit"], "answer": "Central Processing Unit"},
        {"category": "🌐 Technology", "question": "Which company created the iPhone?", "options": ["Google", "Microsoft", "Samsung", "Apple"], "answer": "Apple"},
        {"category": "🌐 Technology", "question": "What is the brain of the computer?", "options": ["RAM", "Hard Drive", "CPU", "GPU"], "answer": "CPU"},
        {"category": "🌐 Technology", "question": "Which programming language is used to style web pages?", "options": ["HTML", "Python", "CSS", "Java"], "answer": "CSS"},
        {"category": "💰 Finance", "question": "Which currency is widely accepted as a global currency?", "options": ["Indian Rupee", "Euro", "US Dollar", "British Pound"], "answer": "US Dollar"},
        {"category": "💰 Finance", "question": "What does ATM stand for?", "options": ["Any Time Money", "Automated Teller Machine", "Auto Transaction Mode", "Authorized Transfer Money"], "answer": "Automated Teller Machine"},
        {"category": "💰 Finance", "question": "What is the full form of GDP?", "options": ["Gross Domestic Product", "General Development Program", "Gross Development Percentage", "Global Domestic Potential"], "answer": "Gross Domestic Product"},
        {"category": "💰 Finance", "question": "Which organization regulates stock markets in India?", "options": ["RBI", "NSE", "SEBI", "BSE"], "answer": "SEBI"},
        {"category": "💰 Finance", "question": "What is the term for profit made from selling assets like shares?", "options": ["Capital Gain", "Interest", "Bonus", "Dividend"], "answer": "Capital Gain"},
        {"category": "🛒 Business", "question": "Who is the founder of Amazon?", "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Larry Page"], "answer": "Jeff Bezos"},
        {"category": "🛒 Business", "question": "What is the most valuable company in the world as of 2025?", "options": ["Amazon", "Apple", "Microsoft", "Tesla"], "answer": "Apple"},
        {"category": "🛒 Business", "question": "Which company owns YouTube?", "options": ["Meta", "Amazon", "Microsoft", "Google"], "answer": "Google"},
        {"category": "🛒 Business", "question": "Which Indian company is headed by Mukesh Ambani?", "options": ["Tata", "Adani", "Infosys", "Reliance"], "answer": "Reliance"},
        {"category": "🛒 Business", "question": "Which company makes the iPhone?", "options": ["Samsung", "Apple", "Sony", "Google"], "answer": "Apple"},
    ]
    random.shuffle(data)
    st.session_state.quiz_data = data

# ✅ 3. Initialize Session State
if 'q_no' not in st.session_state:
    st.session_state.q_no = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'quiz_over' not in st.session_state:
    st.session_state.quiz_over = False

# ✅ 4. Functions
def restart_quiz():
    st.session_state.q_no = 0
    st.session_state.score = 0
    st.session_state.quiz_over = False
    random.shuffle(st.session_state.quiz_data)

# ✅ 5. Login UI
if not st.session_state.username:
    st.title("🌟 Multi-Topic Quiz App")
    name = st.text_input("Enter your name to start:", placeholder="Guest")
    if st.button("Start Quiz"):
        st.session_state.username = name if name else "Guest"
        st.rerun()
    st.stop()

# ✅ 6. Quiz UI
if st.session_state.quiz_over:
    st.title("🎯 Your Result")
    st.write(f"### 👤 Player: {st.session_state.username}")
    total = len(st.session_state.quiz_data)
    percent = int((st.session_state.score / total) * 100)
    
    st.metric("Score", f"{st.session_state.score}/{total}", f"{percent}%")
    
    if percent >= 70:
        st.balloons()
        st.success("Great job!")
    else:
        st.warning("Keep practicing!")

    if st.button("🔁 Restart Quiz"):
        restart_quiz()
        st.rerun()

else:
    current_q = st.session_state.quiz_data[st.session_state.q_no]
    
    st.title("🧠 Quiz Time!")
    st.info(f"**Category:** {current_q['category']}")
    st.write(f"### Question {st.session_state.q_no + 1} of {len(st.session_state.quiz_data)}")
    st.write(current_q['question'])

    # Radio button for options
    answer = st.radio("Choose one:", current_q['options'], index=None)

    if st.button("Next ➡️"):
        if answer:
            if answer == current_q['answer']:
                st.session_state.score += 1
                st.toast("Correct! ✅")
            else:
                st.error(f"Incorrect ❌. The correct answer was: {current_q['answer']}")
                time.sleep(1) # Small delay so they can see the answer
            
            # Move to next question
            if st.session_state.q_no + 1 < len(st.session_state.quiz_data):
                st.session_state.q_no += 1
                st.rerun()
            else:
                st.session_state.quiz_over = True
                st.rerun()
        else:
            st.warning("Please select an option!")
