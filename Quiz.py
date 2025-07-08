from tkinter import *
from tkinter import messagebox, simpledialog
import random

# ✅ Quiz Data
quiz_data = [
    {"category": "🌍 Geography", "question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": 2},
    {"category": "🌍 Geography", "question": "Which river is known as the Ganga of the South?", "options": ["Yamuna", "Narmada", "Godavari", "Krishna"], "answer": 3},
    {"category": "🌍 Geography", "question": "Which is the largest desert in the world?", "options": ["Sahara", "Arctic", "Gobi", "Thar"], "answer": 1},
    {"category": "🌍 Geography", "question": "Mount Everest lies in which mountain range?", "options": ["Andes", "Rockies", "Himalayas", "Alps"], "answer": 3},
    {"category": "🌍 Geography", "question": "Which continent has the most countries?", "options": ["Europe", "Asia", "Africa", "South America"], "answer": 3},
    {"category": "☀️ Health & Science", "question": "Which vitamin do we get from sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": 4},
    {"category": "☀️ Health & Science", "question": "What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "NaCl"], "answer": 3},
    {"category": "☀️ Health & Science", "question": "Which organ purifies blood in the human body?", "options": ["Heart", "Kidney", "Liver", "Lungs"], "answer": 2},
    {"category": "☀️ Health & Science", "question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 2},
    {"category": "☀️ Health & Science", "question": "What part of the cell contains DNA?", "options": ["Nucleus", "Cytoplasm", "Ribosome", "Mitochondria"], "answer": 1},
    {"category": "🌐 Technology", "question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "High Tech Transfer Protocol", "Home Tool Transfer Process", "Hyperlink and Text Transmission Protocol"], "answer": 1},
    {"category": "🌐 Technology", "question": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Programming Unit"], "answer": 2},
    {"category": "🌐 Technology", "question": "Which company created the iPhone?", "options": ["Google", "Microsoft", "Samsung", "Apple"], "answer": 4},
    {"category": "🌐 Technology", "question": "What is the brain of the computer?", "options": ["RAM", "Hard Drive", "CPU", "GPU"], "answer": 3},
    {"category": "🌐 Technology", "question": "Which programming language is used to style web pages?", "options": ["HTML", "Python", "CSS", "Java"], "answer": 3},
    {"category": "💰 Finance", "question": "Which currency is widely accepted as a global currency?", "options": ["Indian Rupee", "Euro", "US Dollar", "British Pound"], "answer": 3},
    {"category": "💰 Finance", "question": "What does ATM stand for?", "options": ["Any Time Money", "Automated Teller Machine", "Auto Transaction Mode", "Authorized Transfer Money"], "answer": 2},
    {"category": "💰 Finance", "question": "What is the full form of GDP?", "options": ["Gross Domestic Product", "General Development Program", "Gross Development Percentage", "Global Domestic Potential"], "answer": 1},
    {"category": "💰 Finance", "question": "Which organization regulates stock markets in India?", "options": ["RBI", "NSE", "SEBI", "BSE"], "answer": 3},
    {"category": "💰 Finance", "question": "What is the term for profit made from selling assets like shares?", "options": ["Capital Gain", "Interest", "Bonus", "Dividend"], "answer": 1},
    {"category": "🛒 Business", "question": "Who is the founder of Amazon?", "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Larry Page"], "answer": 1},
    {"category": "🛒 Business", "question": "What is the most valuable company in the world as of 2025?", "options": ["Amazon", "Apple", "Microsoft", "Tesla"], "answer": 2},
    {"category": "🛒 Business", "question": "Which company owns YouTube?", "options": ["Meta", "Amazon", "Microsoft", "Google"], "answer": 4},
    {"category": "🛒 Business", "question": "Which Indian company is headed by Mukesh Ambani?", "options": ["Tata", "Adani", "Infosys", "Reliance"], "answer": 4},
    {"category": "🛒 Business", "question": "Which company makes the iPhone?", "options": ["Samsung", "Apple", "Sony", "Google"], "answer": 2},
]

random.shuffle(quiz_data)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Multi-Topic Quiz App")
        self.root.geometry("850x550")
        self.theme = "light"

        self.q_no = 0
        self.score = 0
        self.selected_option = IntVar()
        self.time_left = 30

        self.username = simpledialog.askstring("Login", "Enter your name:")
        if not self.username:
            self.username = "Guest"

        self.timer_label = Label(self.root, text="", font=("Arial", 14), bg="#f2f2f2")
        self.timer_label.pack()

        self.toggle_btn = Button(self.root, text="🌗 Toggle Theme", command=self.toggle_theme)
        self.toggle_btn.pack(pady=5)

        self.create_widgets()
        self.display_question()
        self.update_timer()

    def create_widgets(self):
        self.root.configure(bg="#f2f2f2")
        Label(self.root, text="🧠 Quiz Time!", font=("Helvetica", 24, "bold"), fg="#333", bg="#f2f2f2").pack(pady=20)

        self.q_category = Label(self.root, text="", font=("Arial", 14, "bold"), fg="#1a73e8", bg="#f2f2f2")
        self.q_category.pack()

        self.q_text = Label(self.root, text="", font=("Arial", 16), wraplength=750, justify="center", bg="#f2f2f2")
        self.q_text.pack(pady=(10, 5))

        self.option_frame = Frame(self.root, bg="#f2f2f2")
        self.option_frame.pack(pady=10)

        self.opts = []
        for i in range(4):
            opt = Radiobutton(self.option_frame, text="", variable=self.selected_option, value=i + 1,
                              font=("Arial", 14), bg="#f2f2f2", anchor="w", justify="left", padx=10)
            opt.pack(fill="x", padx=50, pady=5, anchor="w")
            self.opts.append(opt)

        self.next_btn = Button(self.root, text="Next ➡️", command=self.next_question,
                               font=("Arial", 14), bg="#4caf50", fg="white", padx=20, pady=5)
        self.next_btn.pack(pady=30)

    def update_timer(self):
        self.timer_label.config(text=f"⏱️ Time left: {self.time_left} sec")
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.next_question(auto=True)

    def display_question(self):
        self.selected_option.set(0)
        self.time_left = 30
        self.update_timer()

        q_data = quiz_data[self.q_no]
        self.q_category.config(text=f"Category: {q_data['category']}")
        self.q_text.config(text=f"Q{self.q_no + 1} of {len(quiz_data)}: {q_data['question']}")

        for i, option in enumerate(q_data["options"]):
            self.opts[i].config(text=option)

    def next_question(self, auto=False):
        if not auto and self.selected_option.get() == 0:
            messagebox.showwarning("Select an Option", "Please select an answer before proceeding.")
            return

        correct = quiz_data[self.q_no]["answer"]
        if self.selected_option.get() == correct:
            self.score += 1
        elif not auto:
            correct_text = quiz_data[self.q_no]["options"][correct - 1]
            messagebox.showinfo("Incorrect ❌", f"Correct Answer: {correct_text}")

        self.q_no += 1
        if self.q_no >= len(quiz_data):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        total = len(quiz_data)
        wrong = total - self.score
        percent = int((self.score / total) * 100)

        retry = messagebox.askyesno("🎯 Your Result",
                                    f"👤 {self.username}\n✅ Correct: {self.score}\n❌ Wrong: {wrong}\n🎓 Score: {percent}%\n\n🔁 Do you want to restart?")
        if retry:
            self.q_no = 0
            self.score = 0
            random.shuffle(quiz_data)
            self.display_question()
        else:
            self.root.destroy()

    def toggle_theme(self):
        if self.theme == "light":
            self.root.configure(bg="#1e1e1e")
            self.timer_label.config(bg="#1e1e1e", fg="#fff")
            self.q_category.config(bg="#1e1e1e", fg="#4fc3f7")
            self.q_text.config(bg="#1e1e1e", fg="#fff")
            self.option_frame.config(bg="#1e1e1e")
            for opt in self.opts:
                opt.config(bg="#1e1e1e", fg="#fff", selectcolor="#1e1e1e")
            self.theme = "dark"
        else:
            self.root.configure(bg="#f2f2f2")
            self.timer_label.config(bg="#f2f2f2", fg="#000")
            self.q_category.config(bg="#f2f2f2", fg="#1a73e8")
            self.q_text.config(bg="#f2f2f2", fg="#000")
            self.option_frame.config(bg="#f2f2f2")
            for opt in self.opts:
                opt.config(bg="#f2f2f2", fg="#000", selectcolor="#f2f2f2")
            self.theme = "light"

# ✅ Run App
if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()
