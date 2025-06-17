from tkinter import *
from tkinter import messagebox

# ✅ Final Quiz Data with 6 Updated Questions
quiz_data = {
    "question": [
        "🌍 Geography\nQ1: What is the capital of India?",
        "☀️ Health & Science\nQ2: Which vitamin do we get from sunlight?",
        "🌐 Technology\nQ3: What does HTTP stand for in a website URL?",
        "💰 Finance\nQ4: Which currency is widely accepted as a global currency?",
        "🛒 Business\nQ5: Who is the founder of Amazon?",
        "🏢 Business & Economy\nQ6: What is the most valuable company in the world as of 2025?"
    ],
    "options": [
        ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
        ["HyperText Transfer Protocol", "High Tech Transfer Protocol", "Home Tool Transfer Process", "Hyperlink and Text Transmission Protocol"],
        ["Indian Rupee", "Euro", "US Dollar", "British Pound"],
        ["Jeff Bezos", "Elon Musk", "Bill Gates", "Larry Page"],
        ["Amazon", "Apple", "Microsoft", "Tesla"]
    ],
    "answer": [2, 4, 1, 3, 1, 2]  # 1-based indexing
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Final MCQ Quiz")
        self.root.geometry("800x500")
        self.root.configure(bg="#f5f5f5")

        self.q_no = 0
        self.score = 0
        self.selected_option = IntVar()

        self.create_title()
        self.create_question()
        self.opts = self.create_options()
        self.create_buttons()
        self.display_question()

    def create_title(self):
        title = Label(self.root, text="🧠 Multi-Topic Quiz",
                      font=("Helvetica", 22, "bold"),
                      bg="#f5f5f5", fg="#1e88e5")
        title.pack(pady=20)

    def create_question(self):
        self.q_label = Label(self.root, text="", font=("Arial", 16),
                             wraplength=700, justify="left",
                             bg="#f5f5f5", anchor="w")
        self.q_label.pack(pady=15, padx=20)

    def create_options(self):
        opts = []
        for i in range(4):
            btn = Radiobutton(self.root, text="", variable=self.selected_option,
                              value=i + 1, font=("Arial", 14), bg="#f5f5f5",
                              anchor="w", padx=20)
            btn.pack(fill="x", padx=100, pady=4)
            opts.append(btn)
        return opts

    def display_question(self):
        self.selected_option.set(0)
        self.q_label.config(text=quiz_data["question"][self.q_no])
        for i, opt in enumerate(quiz_data["options"][self.q_no]):
            self.opts[i].config(text=opt)

    def create_buttons(self):
        btn_frame = Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=30)

        next_btn = Button(btn_frame, text="Next ➡️", command=self.next_question,
                          font=("Arial", 14), bg="#4caf50", fg="white",
                          padx=20, pady=5)
        next_btn.grid(row=0, column=0, padx=10)

        quit_btn = Button(btn_frame, text="Exit ❌", command=self.root.destroy,
                          font=("Arial", 14), bg="#e53935", fg="white",
                          padx=20, pady=5)
        quit_btn.grid(row=0, column=1, padx=10)

    def next_question(self):
        if self.selected_option.get() == quiz_data["answer"][self.q_no]:
            self.score += 1
        self.q_no += 1
        if self.q_no >= len(quiz_data["question"]):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        wrong = len(quiz_data["question"]) - self.score
        score_percent = int((self.score / len(quiz_data["question"])) * 100)
        messagebox.showinfo("🎯 Result",
                            f"✅ Correct: {self.score}\n❌ Wrong: {wrong}\n🎓 Score: {score_percent}%")
        self.root.destroy()

# ✅ Run the app
if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()
