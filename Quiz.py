import streamlit as st
import random

# --- 1. CONFIG & GATE DATA (10 Subjects x 5 Questions) ---
st.set_page_config(page_title="GATE 2026 Mock Test Portal", page_icon="🛡️", layout="wide")

GATE_DATA = {
    "🖥️ Operating Systems": [
        {"q": "Which of the following is NOT shared by threads of the same process?", "options": ["Stack", "Address Space", "File Descriptors", "Global Variables"], "a": "Stack"},
        {"q": "A system has 3 processes each needing 2 resources. Minimum resources to prevent deadlock?", "options": ["3", "4", "6", "2"], "a": "4"},
        {"q": "Which scheduling policy can cause starvation?", "options": ["FIFO", "Round Robin", "Priority Scheduling", "SJF"], "a": "Priority Scheduling"},
        {"q": "Belady's Anomaly occurs in which page replacement algorithm?", "options": ["LRU", "Optimal", "FIFO", "MRU"], "a": "FIFO"},
        {"q": "The size of the Virtual Address space is determined by?", "options": ["RAM size", "Data Bus size", "Address Bus size", "Disk size"], "a": "Address Bus size"}
    ],
    "🏗️ Computer Architecture": [
        {"q": "Which addressing mode is most suitable for program relocation at runtime?", "options": ["Absolute", "Immediate", "Base Register", "Direct"], "a": "Base Register"},
        {"q": "What is the primary purpose of Cache Memory?", "options": ["Increase Capacity", "Speed up access", "Permanent Storage", "Backup"], "a": "Speed up access"},
        {"q": "Which is a core characteristic of RISC architecture?", "options": ["Large instruction set", "Variable length", "Single cycle execution", "Complex addressing"], "a": "Single cycle execution"},
        {"q": "Pipeline hazards can be caused by which of the following?", "options": ["Data dependency", "Branching", "Resource conflict", "All of the above"], "a": "All of the above"},
        {"q": "Write-through policy is commonly used in?", "options": ["Virtual memory", "Cache memory", "Registers", "Hard Disks"], "a": "Cache memory"}
    ],
    "📊 Data Structures": [
        {"q": "Worst case search time in a Binary Search Tree (BST) is?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "a": "O(n)"},
        {"q": "Which data structure is used to implement Depth First Search (DFS)?", "options": ["Queue", "Stack", "Priority Queue", "Linked List"], "a": "Stack"},
        {"q": "Number of edges in a complete graph with 'n' vertices is?", "options": ["n", "n-1", "n(n-1)/2", "n^2"], "a": "n(n-1)/2"},
        {"q": "Min-Heaps are primarily used to implement?", "options": ["Sorting", "Priority Queues", "Graph traversal", "Hashing"], "a": "Priority Queues"},
        {"q": "The prefix form of the expression A+B*C is?", "options": ["+A*BC", "+*ABC", "ABC*+", "A+BC*"], "a": "+A*BC"}
    ],
    "🧮 Algorithms": [
        {"q": "What is the time complexity of Merge Sort?", "options": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"], "a": "O(n log n)"},
        {"q": "Huffman coding is an example of which algorithmic strategy?", "options": ["Dynamic Programming", "Divide & Conquer", "Greedy", "Backtracking"], "a": "Greedy"},
        {"q": "The Bellman-Ford algorithm is used to find?", "options": ["Shortest path", "MST", "Sorting", "Max flow"], "a": "Shortest path"},
        {"q": "Floyd-Warshall algorithm is used for?", "options": ["Single source shortest path", "All pairs shortest path", "Sorting", "Searching"], "a": "All pairs shortest path"},
        {"q": "Which of the following is NOT a P-class problem?", "options": ["Sorting", "Searching", "Matrix Multiplication", "TSP"], "a": "TSP"}
    ],
    "🗄️ DBMS": [
        {"q": "Which normal form deals specifically with BCNF?", "options": ["1NF", "2NF", "3NF", "Strict 3NF"], "a": "Strict 3NF"},
        {"q": "In ACID properties, 'A' stands for?", "options": ["Availability", "Atomicity", "Accuracy", "Authority"], "a": "Atomicity"},
        {"q": "TRUNCATE is categorized as what type of SQL command?", "options": ["DDL", "DML", "DCL", "TCL"], "a": "DDL"},
        {"q": "A Primary key must satisfy which condition?", "options": ["Unique", "Not Null", "Both Unique & Not Null", "None"], "a": "Both Unique & Not Null"},
        {"q": "Foreign keys are used to ensure?", "options": ["Data integrity", "Query speed", "Referential integrity", "Indexing"], "a": "Referential integrity"}
    ],
    "🌐 Computer Networks": [
        {"q": "Which layer is responsible for end-to-end communication?", "options": ["Network", "Transport", "Session", "Physical"], "a": "Transport"},
        {"q": "Which address is used at the Data Link Layer?", "options": ["IP", "MAC", "Port", "Socket"], "a": "MAC"},
        {"q": "DNS primarily uses which transport protocol?", "options": ["TCP", "UDP", "HTTP", "FTP"], "a": "UDP"},
        {"q": "The size of an IPv4 address is?", "options": ["16 bit", "32 bit", "64 bit", "128 bit"], "a": "32 bit"},
        {"q": "Which of these is a Routing protocol?", "options": ["BGP", "HTTP", "SMTP", "ARP"], "a": "BGP"}
    ],
    "🧠 Theory of Computation": [
        {"q": "Which machine accepts Context-Free Languages?", "options": ["DFA", "PDA", "Turing Machine", "NFA"], "a": "PDA"},
        {"q": "The language {a^n b^n | n >= 0} is classified as?", "options": ["Regular", "Context-Free", "Recursive", "Non-recursive"], "a": "Context-Free"},
        {"q": "Which of the following problems is undecidable?", "options": ["DFA emptiness", "Halting Problem", "CFG membership", "None"], "a": "Halting Problem"},
        {"q": "Number of states in a DFA accepting strings ending with '00'?", "options": ["2", "3", "4", "5"], "a": "3"},
        {"q": "The power of an NFA compared to a DFA is?", "options": ["NFA > DFA", "DFA > NFA", "Equal", "Depends"], "a": "Equal"}
    ],
    "🛠️ Compiler Design": [
        {"q": "Lexical analyzer is implemented using?", "options": ["DFA", "PDA", "Turing Machine", "Graph"], "a": "DFA"},
        {"q": "The output of the Lexical Analyzer phase is?", "options": ["Parse Tree", "Tokens", "Object code", "Intermediate code"], "a": "Tokens"},
        {"q": "Intermediate code generation is used for?", "options": ["Speed", "Portability", "Security", "Debugging"], "a": "Portability"},
        {"q": "Left factoring is necessary for which parsing?", "options": ["Removing ambiguity", "Top-down parsing", "Code optimization", "Linker"], "a": "Top-down parsing"},
        {"q": "The Symbol table is utilized for?", "options": ["Storing Identifiers", "Type checking", "Scope management", "All of above"], "a": "All of above"}
    ],
    "📐 Discrete Mathematics": [
        {"q": "The proposition P -> Q is false ONLY when?", "options": ["P=T, Q=T", "P=T, Q=F", "P=F, Q=T", "P=F, Q=F"], "a": "P=T, Q=F"},
        {"q": "The chromatic number of a K4 graph is?", "options": ["2", "3", "4", "5"], "a": "4"},
        {"q": "Number of subsets for a set with 5 elements is?", "options": ["10", "25", "32", "64"], "a": "32"},
        {"q": "P v ~P is technically called a?", "options": ["Tautology", "Contradiction", "Contingency", "Fallacy"], "a": "Tautology"},
        {"q": "Which of the following is a cyclic group?", "options": ["Z4", "V4", "Matrix group", "None"], "a": "Z4"}
    ],
    "📉 Digital Logic": [
        {"q": "Minimum number of NAND gates required for XOR?", "options": ["3", "4", "5", "6"], "a": "4"},
        {"q": "The Gray code for decimal 4 is?", "options": ["100", "110", "111", "101"], "a": "110"},
        {"q": "Which flip-flop acts as a simple buffer?", "options": ["JK", "T", "D", "SR"], "a": "D"},
        {"q": "2's complement of the binary 1010 is?", "options": ["0101", "0110", "1100", "1011"], "a": "0110"},
        {"q": "A Multiplexer is also known as a?", "options": ["Data Selector", "Data Distributor", "Encoder", "Decoder"], "a": "Data Selector"}
    ]
}

# --- 2. SESSION STATE (The Backend Data) ---
if 'users' not in st.session_state:
    st.session_state.users = {} # Simulated User Database
if 'page' not in st.session_state:
    st.session_state.page = "auth"
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- 3. THE PORTAL SCREENS ---

# AUTHENTICATION (Sign Up & Login)
if st.session_state.page == "auth":
    st.title("🛡️ GATE 2026 Entrance Portal")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔑 Login")
        u_in = st.text_input("Username", key="login_u")
        p_in = st.text_input("Password", type="password", key="login_p")
        if st.button("Login"):
            if u_in in st.session_state.users and st.session_state.users[u_in] == p_in:
                st.session_state.current_user = u_in
                change_page("dashboard")
            else:
                st.error("Invalid Username or Password.")

    with col2:
        st.subheader("📝 New Account")
        nu_in = st.text_input("Choose Username", key="reg_u")
        np_in = st.text_input("Choose Password", type="password", key="reg_p")
        if st.button("Create Account"):
            if nu_in and np_in:
                st.session_state.users[nu_in] = np_in
                st.success("Account created! Now login on the left.")
            else:
                st.warning("Please fill out both fields.")

# DASHBOARD (Subject Selection)
elif st.session_state.page == "dashboard":
    st.title(f"🚀 Candidate Dashboard: {st.session_state.current_user}")
    st.write("Please select a subject to start your mock examination.")
    st.markdown("---")
    
    # Grid of subjects
    cols = st.columns(2)
    for i, subject in enumerate(GATE_DATA.keys()):
        with cols[i % 2]:
            if st.button(subject, use_container_width=True):
                st.session_state.selected_subject = subject
                st.session_state.q_idx = 0
                st.session_state.score = 0
                change_page("quiz")
    
    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.current_user = None
        change_page("auth")

# QUIZ (Exam Mode)
elif st.session_state.page == "quiz":
    subj = st.session_state.selected_subject
    idx = st.session_state.q_idx
    q_set = GATE_DATA[subj]
    
    st.sidebar.title("Exam Info")
    st.sidebar.write(f"**Subject:** {subj}")
    st.sidebar.write(f"**Progress:** {idx+1} / {len(q_set)}")
    
    st.subheader(f"Question {idx+1}")
    st.markdown(f"#### {q_set[idx]['q']}")
    
    choice = st.radio("Choose the correct option:", q_set[idx]['options'], index=None, key=f"q{idx}")
    
    if st.button("Submit & Next ➡️"):
        if choice:
            if choice == q_set[idx]['a']:
                st.session_state.score += 1
            
            if idx + 1 < len(q_set):
                st.session_state.q_idx += 1
                st.rerun()
            else:
                change_page("results")
        else:
            st.warning("Please select an answer to continue.")

# RESULTS (Performance Report)
elif st.session_state.page == "results":
    st.title("🎯 Mock Test Results")
    score = st.session_state.score
    total = 5
    percent = (score / total) * 100
    
    st.markdown(f"**Candidate:** {st.session_state.current_user}")
    st.markdown(f"**Subject:** {st.session_state.selected_subject}")
    
    st.metric("Final Score", f"{score} / {total}", f"{percent}%")
    
    if percent >= 80:
        st.balloons()
        st.success("Excellent Rank Potential!")
    elif percent >= 40:
        st.info("Qualified. Needs more revision.")
    else:
        st.error("Did not qualify. Focus on core concepts.")

    if st.button("Return to Dashboard"):
        change_page("dashboard")
