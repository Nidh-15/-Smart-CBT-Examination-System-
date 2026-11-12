
import tkinter as tk
from tkinter import messagebox
import random

# ==============================
# 1. SAMPLE MCQ QUESTIONS
# ==============================

questions = [
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "list"],
        "answer": "bool"
    },
    {
        "question": "Which function displays output?",
        "options": ["input()", "print()", "show()", "display()"],
        "answer": "print()"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["//", "#", "@", "$"],
        "answer": "#"
    }
]

# ==============================
# 2. GLOBAL VARIABLES
# ==============================

student_name = ""
current_question = 0
score = 0
answers = []
time_left = 60
exam_active = False
timer_job = None
results_history = []

# ==============================
# 3. MAIN WINDOW
# ==============================

root = tk.Tk()
root.title("Smart CBT Examination System")
root.geometry("750x550")
root.configure(bg="#eaf2f8")

# Create StringVar AFTER root
selected_answer = tk.StringVar(master=root)


# ==============================
# 4. CLEAR SCREEN
# ==============================

def clear_screen():

    for widget in root.winfo_children():
        widget.destroy()


# ==============================
# 5. LOGIN PAGE
# ==============================

def login_page():

    global selected_answer

    clear_screen()

    selected_answer = tk.StringVar(master=root)

    tk.Label(
        root,
        text="SMART CBT EXAMINATION SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#eaf2f8",
        fg="#154360"
    ).pack(pady=25)

    tk.Label(root, text="Username", bg="#eaf2f8").pack()

    username = tk.Entry(root, font=("Arial", 12))
    username.pack(pady=5)

    tk.Label(root, text="Password", bg="#eaf2f8").pack()

    password = tk.Entry(root, show="*", font=("Arial", 12))
    password.pack(pady=5)

    def login():

        global student_name

        user = username.get()
        pwd = password.get()

        if user == "admin" and pwd == "admin123":

            admin_dashboard()

        elif user == "student" and pwd == "1234":

            student_name = "Student"
            student_dashboard()

        else:

            messagebox.showerror(
                "Login Error",
                "Invalid Username or Password"
            )

    tk.Button(
        root,
        text="Login",
        command=login,
        bg="#2874a6",
        fg="white",
        width=18
    ).pack(pady=20)

    tk.Label(
        root,
        text="Admin: admin / admin123\nStudent: student / 1234",
        bg="#eaf2f8",
        fg="gray"
    ).pack()


# ==============================
# 6. ADMIN DASHBOARD
# ==============================

def admin_dashboard():

    clear_screen()

    tk.Label(
        root,
        text="ADMIN DASHBOARD",
        font=("Arial", 20, "bold"),
        bg="#eaf2f8"
    ).pack(pady=25)

    tk.Label(
        root,
        text="Welcome Administrator",
        bg="#eaf2f8"
    ).pack(pady=10)

    tk.Label(
        root,
        text=f"Total Questions: {len(questions)}",
        bg="#eaf2f8"
    ).pack(pady=10)

    tk.Button(
        root,
        text="View Results",
        command=admin_results
    ).pack(pady=10)

    tk.Button(
        root,
        text="Logout",
        command=login_page
    ).pack(pady=10)


# ==============================
# 7. ADMIN RESULTS
# ==============================

def admin_results():

    clear_screen()

    tk.Label(
        root,
        text="STUDENT RESULTS",
        font=("Arial", 18, "bold"),
        bg="#eaf2f8"
    ).pack(pady=20)

    if not results_history:

        tk.Label(
            root,
            text="No Results Available",
            bg="#eaf2f8"
        ).pack()

    for result in results_history:

        tk.Label(
            root,
            text=result,
            bg="#eaf2f8"
        ).pack(pady=5)

    tk.Button(
        root,
        text="Back",
        command=admin_dashboard
    ).pack(pady=20)


# ==============================
# 8. STUDENT DASHBOARD
# ==============================

def student_dashboard():

    clear_screen()

    tk.Label(
        root,
        text="STUDENT DASHBOARD",
        font=("Arial", 20, "bold"),
        bg="#eaf2f8"
    ).pack(pady=25)

    tk.Label(
        root,
        text=f"Welcome {student_name}",
        bg="#eaf2f8"
    ).pack(pady=10)

    tk.Button(
        root,
        text="Start Examination",
        command=start_exam,
        bg="#2874a6",
        fg="white",
        width=20
    ).pack(pady=15)

    tk.Button(
        root,
        text="Performance Analysis",
        command=performance_analysis
    ).pack(pady=10)

    tk.Button(
        root,
        text="Logout",
        command=login_page
    ).pack(pady=10)


# ==============================
# 9. START EXAMINATION
# ==============================

def start_exam():

    global current_question
    global score
    global answers
    global time_left
    global exam_active

    if not questions:
        messagebox.showerror("Error", "No questions available.")
        return

    current_question = 0
    score = 0

    exam_questions = random.sample(
        questions,
        min(5, len(questions))
    )

    global active_questions
    active_questions = exam_questions

    answers = [""] * len(active_questions)

    time_left = 60
    exam_active = True

    show_question()

    update_timer()


# ==============================
# 10. DISPLAY MCQ QUESTIONS
# ==============================

def show_question():

    global selected_answer

    clear_screen()

    selected_answer = tk.StringVar(master=root)

    q = active_questions[current_question]

    tk.Label(
        root,
        text="EXAMINATION PANEL",
        font=("Arial", 18, "bold"),
        bg="#eaf2f8"
    ).pack(pady=15)

    global timer_label

    timer_label = tk.Label(
        root,
        text="Time: 60 seconds",
        font=("Arial", 13, "bold"),
        fg="red",
        bg="#eaf2f8"
    )

    timer_label.pack(pady=5)

    tk.Label(
        root,
        text=f"Question {current_question + 1} of {len(active_questions)}",
        bg="#eaf2f8"
    ).pack(pady=10)

    tk.Label(
        root,
        text=q["question"],
        font=("Arial", 14, "bold"),
        bg="#eaf2f8",
        wraplength=650
    ).pack(pady=15)

    selected_answer.set(answers[current_question])

    for option in q["options"]:

        tk.Radiobutton(
            root,
            text=option,
            variable=selected_answer,
            value=option,
            bg="#eaf2f8",
            font=("Arial", 12)
        ).pack(anchor="w", padx=180, pady=4)

    nav = tk.Frame(root, bg="#eaf2f8")
    nav.pack(pady=20)

    if current_question > 0:

        tk.Button(
            nav,
            text="Previous",
            command=previous_question
        ).pack(side="left", padx=5)

    tk.Button(
        nav,
        text="Next",
        command=next_question,
        bg="#2874a6",
        fg="white"
    ).pack(side="left", padx=5)

    tk.Button(
        nav,
        text="Submit Exam",
        command=confirm_submit,
        bg="#23845b",
        fg="white"
    ).pack(side="left", padx=5)

    update_timer_display()


# ==============================
# 11. SAVE ANSWER
# ==============================

def save_answer():

    answers[current_question] = selected_answer.get()


# ==============================
# 12. NEXT QUESTION
# ==============================

def next_question():

    global current_question

    save_answer()

    if current_question < len(active_questions) - 1:

        current_question += 1
        show_question()

    else:

        messagebox.showinfo(
            "Exam",
            "This is the last question. Submit your exam when ready."
        )


# ==============================
# 13. PREVIOUS QUESTION
# ==============================

def previous_question():

    global current_question

    save_answer()

    if current_question > 0:

        current_question -= 1
        show_question()


# ==============================
# 14. EXAM TIMER
# ==============================

def update_timer_display():

    mins, secs = divmod(time_left, 60)

    timer_label.config(
        text=f"Time Remaining: {mins:02d}:{secs:02d}"
    )


def update_timer():

    global time_left
    global timer_job

    if not exam_active:
        return

    update_timer_display()

    if time_left <= 0:

        submit_exam(auto=True)
        return

    time_left -= 1

    timer_job = root.after(1000, update_timer)


# ==============================
# 15. SUBMIT EXAM
# ==============================

def confirm_submit():

    save_answer()

    if messagebox.askyesno(
        "Submit Exam",
        "Are you sure you want to submit?"
    ):

        submit_exam()


def submit_exam(auto=False):

    global score
    global exam_active
    global timer_job

    if not exam_active:
        return

    save_answer()

    exam_active = False

    if timer_job is not None:

        root.after_cancel(timer_job)
        timer_job = None

    score = 0

    for i in range(len(active_questions)):

        if answers[i] == active_questions[i]["answer"]:

            score += 1

    total = len(active_questions)

    percentage = (score / total) * 100

    results_history.append({
        "name": student_name,
        "score": score,
        "total": total,
        "percentage": percentage
    })

    show_result(score, total, percentage, auto)


# ==============================
# 16. RESULT CALCULATION
# ==============================

def show_result(score, total, percentage, auto):

    clear_screen()

    tk.Label(
        root,
        text="EXAMINATION RESULT",
        font=("Arial", 20, "bold"),
        bg="#eaf2f8"
    ).pack(pady=25)

    tk.Label(
        root,
        text=f"Student: {student_name}",
        bg="#eaf2f8"
    ).pack(pady=5)

    tk.Label(
        root,
        text=f"Your Score: {score}/{total}",
        font=("Arial", 16, "bold"),
        bg="#eaf2f8"
    ).pack(pady=10)

    tk.Label(
        root,
        text=f"Percentage: {percentage:.1f}%",
        font=("Arial", 14),
        bg="#eaf2f8"
    ).pack(pady=10)

    if auto:

        tk.Label(
            root,
            text="Time is over. Your exam was submitted automatically.",
            fg="red",
            bg="#eaf2f8"
        ).pack(pady=5)

    tk.Button(
        root,
        text="Performance Analysis",
        command=performance_analysis
    ).pack(pady=15)

    tk.Button(
        root,
        text="Dashboard",
        command=student_dashboard
    ).pack(pady=5)


# ==============================
# 17. PERFORMANCE ANALYSIS
# ==============================

def performance_analysis():

    clear_screen()

    tk.Label(
        root,
        text="PERFORMANCE ANALYSIS",
        font=("Arial", 18, "bold"),
        bg="#eaf2f8"
    ).pack(pady=20)

    student_results = [
        r for r in results_history
        if r["name"] == student_name
    ]

    if not student_results:

        tk.Label(
            root,
            text="No exam history available",
            bg="#eaf2f8"
        ).pack(pady=15)

    else:

        scores = [
            r["percentage"] for r in student_results
        ]

        average = sum(scores) / len(scores)

        prediction = average

        if len(scores) >= 2:

            prediction = max(
                0,
                min(100, scores[-1] + scores[-1] - scores[-2])
            )

        tk.Label(
            root,
            text=f"Exams Taken: {len(scores)}",
            bg="#eaf2f8"
        ).pack(pady=8)

        tk.Label(
            root,
            text=f"Average Score: {average:.1f}%",
            bg="#eaf2f8"
        ).pack(pady=8)

        tk.Label(
            root,
            text=f"Best Score: {max(scores):.1f}%",
            bg="#eaf2f8"
        ).pack(pady=8)

        tk.Label(
            root,
            text=f"Predicted Next Score: {prediction:.1f}%",
            fg="green",
            bg="#eaf2f8",
            font=("Arial", 13, "bold")
        ).pack(pady=12)

        tk.Label(
            root,
            text="Score History:",
            bg="#eaf2f8"
        ).pack(pady=5)

        for i, value in enumerate(scores, start=1):

            tk.Label(
                root,
                text=f"Exam {i}: {value:.1f}%",
                bg="#eaf2f8"
            ).pack(pady=3)

        tk.Label(
            root,
            text="Prediction is an estimate based on previous scores.",
            bg="#eaf2f8",
            fg="gray"
        ).pack(pady=8)

    tk.Button(
        root,
        text="Back to Dashboard",
        command=student_dashboard
    ).pack(pady=20)


# ==============================
# 18. RUN APPLICATION
# ==============================

login_page()

root.mainloop()
