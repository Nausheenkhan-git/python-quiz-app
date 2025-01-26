# import tkinter as tk
# from tkinter import ttk

# questions = [
#     {"topic": "Loops", "question": "What's the output?", "code": "for i in range(3):\n  print(i)", "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"], "answer": 0},
#     {"topic": "Lists", "question": "What's the output?", "code": "my_list = [1,2,3,4,5]\nprint(my_list[1:4])", "options": ["[2, 3, 4]", "[1, 2, 3]", "[2, 3, 4, 5]", "[1, 2, 3, 4]"], "answer": 0},
#     {"topic": "Strings", "question": "What's the output?", "code": "name = 'John Doe'\nprint(name.upper())", "options": ["john doe", "JOHN DOE", "John Doe", "jOHN dOE"], "answer": 1},
#     {"topic": "Functions", "question": "What does this function do?", "code": "def square(x):\n  return x**2", "options": ["Calculates the square of a number", "Finds the square root of a number", "Raises a number to the power of 2", "Multiplies a number by itself"], "answer": 0},
#     {"topic": "Conditionals", "question": "What's the output?", "code": "x = 10\nif x > 0:\n  print('Positive')\nelif x < 0:\n  print('Negative')\nelse:\n  print('Zero')", "options": ["Positive", "Negative", "Zero", "Nothing"], "answer": 0},
#     {"topic": "Data Types", "question": "What data type is 42.5?", "options": ["Integer", "Float", "String", "Boolean"], "answer": 1},
#     {"topic": "Variables", "question": "How do you declare a variable in Python?", "options": ["var x = 5", "$x = 5", "x = 5", "let x = 5"], "answer": 2},
#     {"topic": "Modules", "question": "Which module do you import to work with math functions?", "options": ["sys", "os", "math", "datetime"], "answer": 2},
#     {"topic": "Exceptions", "question": "Which exception is raised when you divide by zero?", "options": ["IndexError", "TypeError", "ValueError", "ZeroDivisionError"], "answer": 3},
#     {"topic": "File I/O", "question": "Which mode do you use to write to a file?", "options": ["r", "w", "a", "x"], "answer": 1},
#     {"topic": "OOP", "question": "What is the purpose of the __init__ method in a class?", "options": ["To define instance variables", "To define class variables", "To define static methods", "To define the constructor"], "answer": 3},
#     {"topic": "Itertools", "question": "Which function from the itertools module generates all possible combinations?", "options": ["combinations", "permutations", "product", "accumulate"], "answer": 0}
# ]

# class QuizApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Python Quiz Generator")
#         self.setup_ui()

#     def setup_ui(self):
#         # Main content frame
#         content_frame = ttk.Frame(self, padding=(20, 20))
#         content_frame.pack(fill="both", expand=True)

#         # Title label
#         title_label = ttk.Label(content_frame, text="Welcome to the Python Quiz Generator!", font=("Arial", 18, "bold"))
#         title_label.pack(pady=(0, 20))

#         # Instructions label
#         instructions_label = ttk.Label(content_frame, text="Enter a Python topic and click 'Generate' to get a quiz question.", wraplength=400)
#         instructions_label.pack(pady=(0, 10))

#         # Topic input and generate button
#         topic_frame = ttk.Frame(content_frame)
#         topic_frame.pack(pady=(0, 20))
#         self.topic_entry = ttk.Entry(topic_frame, width=20)
#         self.topic_entry.pack(side="left", padx=(0, 10))
#         self.generate_button = ttk.Button(topic_frame, text="Generate", command=self.show_question)
#         self.generate_button.pack(side="left")

#         # Question display area
#         self.question_frame = ttk.Frame(content_frame)
#         self.question_frame.pack(pady=(0, 20))
#         self.topic_label = ttk.Label(self.question_frame, text="", font=("Arial", 14, "bold"))
#         self.topic_label.pack()
#         self.question_label = ttk.Label(self.question_frame, text="", wraplength=400)
#         self.question_label.pack(pady=(10, 0))
#         self.code_label = ttk.Label(self.question_frame, text="", font=("Courier", 12))
#         self.code_label.pack(pady=(10, 0))

#         # Answer options
#         self.answer_frame = ttk.Frame(content_frame)
#         self.answer_frame.pack(pady=(0, 20))
#         self.answer_var = tk.StringVar()
#         self.answer_buttons = [
#             ttk.Radiobutton(self.answer_frame, text="", variable=self.answer_var, value=str(i))
#             for i in range(4)
#         ]
#         for button in self.answer_buttons:
#             button.pack(side="left", padx=(0, 10))

#         # Submit button and feedback label
#         submit_frame = ttk.Frame(content_frame)
#         submit_frame.pack(pady=(0, 20))
#         self.submit_button = ttk.Button(submit_frame, text="Submit", command=self.check_answer)
#         self.submit_button.pack(side="left", padx=(0, 10))
#         self.feedback_label = ttk.Label(submit_frame, text="", font=("Arial", 14))
#         self.feedback_label.pack(side="left")

#     def show_question(self):
#         topic = self.topic_entry.get().capitalize()
#         matches = [q for q in questions if q["topic"] == topic]
#         if matches:
#             q = matches[0]
#             self.topic_label.config(text=f"Topic: {q['topic']}")
#             self.question_label.config(text=q["question"])
#             self.code_label.config(text=q["code"])
#             for i, option in enumerate(q["options"]):
#                 self.answer_buttons[i].config(text=option)
#             self.answer_var.set("")
#         else:
#             self.clear_display()
#             self.feedback_label.config(text="No questions found for the topic.", foreground="red")

#     def check_answer(self):
#         topic = self.topic_entry.get().capitalize()
#         matches = [q for q in questions if q["topic"] == topic]
#         if matches:
#             q = matches[0]
#             selected = int(self.answer_var.get())
#             if selected == q["answer"]:
#                 self.feedback_label.config(text="Correct!", foreground="green")
#             else:
#                 self.feedback_label.config(text="Incorrect. Try again.", foreground="red")
#         else:
#             self.feedback_label.config(text="")

#     def clear_display(self):
#         self.topic_label.config(text="")
#         self.question_label.config(text="")
#         self.code_label.config(text="")
#         for button in self.answer_buttons:
#             button.config(text="")

# if __name__ == "__main__":
#     app = QuizApp()
#     app.mainloop()

import tkinter as tk
from tkinter import ttk

questions = [
    {"topic": "Loops", "question": "What's the output?", "code": "for i in range(3):\n  print(i)", "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"], "answer": 0},
    {"topic": "Lists", "question": "What's the output?", "code": "my_list = [1,2,3,4,5]\nprint(my_list[1:4])", "options": ["[2, 3, 4]", "[1, 2, 3]", "[2, 3, 4, 5]", "[1, 2, 3, 4]"], "answer": 0},
    {"topic": "Strings", "question": "What's the output?", "code": "name = 'John Doe'\nprint(name.upper())", "options": ["john doe", "JOHN DOE", "John Doe", "jOHN dOE"], "answer": 1},
    {"topic": "Functions", "question": "What does this function do?", "code": "def square(x):\n  return x**2", "options": ["Calculates the square of a number", "Finds the square root of a number", "Raises a number to the power of 2", "Multiplies a number by itself"], "answer": 0},
    {"topic": "Conditionals", "question": "What's the output?", "code": "x = 10\nif x > 0:\n  print('Positive')\nelif x < 0:\n  print('Negative')\nelse:\n  print('Zero')", "options": ["Positive", "Negative", "Zero", "Nothing"], "answer": 0},
    {"topic": "Data Types", "question": "What data type is 42.5?", "options": ["Integer", "Float", "String", "Boolean"], "answer": 1},
    {"topic": "Variables", "question": "How do you declare a variable in Python?", "options": ["var x = 5", "$x = 5", "x = 5", "let x = 5"], "answer": 2},
    {"topic": "Modules", "question": "Which module do you import to work with math functions?", "options": ["sys", "os", "math", "datetime"], "answer": 2},
    {"topic": "Exceptions", "question": "Which exception is raised when you divide by zero?", "options": ["IndexError", "TypeError", "ValueError", "ZeroDivisionError"], "answer": 3},
    {"topic": "File I/O", "question": "Which mode do you use to write to a file?", "options": ["r", "w", "a", "x"], "answer": 1},
    {"topic": "OOP", "question": "What is the purpose of the __init__ method in a class?", "options": ["To define instance variables", "To define class variables", "To define static methods", "To define the constructor"], "answer": 3},
    {"topic": "Itertools", "question": "Which function from the itertools module generates all possible combinations?", "options": ["combinations", "permutations", "product", "accumulate"], "answer": 0}
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Quiz Generator")
        self.setup_ui()
        self.current_question = None

    def setup_ui(self):
        # Main content frame
        content_frame = ttk.Frame(self, padding=(20, 20))
        content_frame.pack(fill="both", expand=True)

        # Title label
        title_label = ttk.Label(content_frame, text="Welcome to the Python Quiz Generator!", font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))

        # Instructions label
        instructions_label = ttk.Label(content_frame, text="Enter a Python topic and click 'Generate' to get a quiz question.", wraplength=400)
        instructions_label.pack(pady=(0, 10))

        # Topic input and generate button
        topic_frame = ttk.Frame(content_frame)
        topic_frame.pack(pady=(0, 20))
        self.topic_entry = ttk.Entry(topic_frame, width=20)
        self.topic_entry.pack(side="left", padx=(0, 10))
        self.generate_button = ttk.Button(topic_frame, text="Generate", command=self.show_question)
        self.generate_button.pack(side="left")

        # Question display area
        self.question_frame = ttk.Frame(content_frame)
        self.question_frame.pack(pady=(0, 20))
        self.topic_label = ttk.Label(self.question_frame, text="", font=("Arial", 14, "bold"))
        self.topic_label.pack()
        self.question_label = ttk.Label(self.question_frame, text="", wraplength=400)
        self.question_label.pack(pady=(10, 0))
        self.code_label = ttk.Label(self.question_frame, text="", font=("Courier", 12))
        self.code_label.pack(pady=(10, 0))

        # Answer options
        self.answer_frame = ttk.Frame(content_frame)
        self.answer_frame.pack(pady=(0, 20))
        self.answer_var = tk.StringVar()
        self.answer_buttons = [
            ttk.Radiobutton(self.answer_frame, text="", variable=self.answer_var, value=str(i))
            for i in range(4)
        ]
        for button in self.answer_buttons:
            button.pack(side="left", padx=(0, 10))

        # Submit button and feedback label
        submit_frame = ttk.Frame(content_frame)
        submit_frame.pack(pady=(0, 20))
        self.submit_button = ttk.Button(submit_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(side="left", padx=(0, 10))
        self.feedback_label = ttk.Label(submit_frame, text="", font=("Arial", 14))
        self.feedback_label.pack(side="left")

    def show_question(self):
        topic = self.topic_entry.get().capitalize()
        matches = [q for q in questions if q["topic"] == topic]
        if matches:
            self.current_question = matches[0]
            self.topic_label.config(text=f"Topic: {self.current_question['topic']}")
            self.question_label.config(text=self.current_question["question"])
            self.code_label.config(text=self.current_question["code"])
            for i, option in enumerate(self.current_question["options"]):
                self.answer_buttons[i].config(text=option)
            self.answer_var.set("")
        else:
            self.clear_display()
            self.feedback_label.config(text="No questions found for the topic.", foreground="red")

    def check_answer(self):
        if self.current_question:
            selected = int(self.answer_var.get())
            if selected == self.current_question["answer"]:
                self.feedback_label.config(text="Correct!", foreground="green")
                self.show_question()
            else:
                self.feedback_label.config(text=f"Incorrect. The correct answer is: {self.current_question['options'][self.current_question['answer']]}", foreground="red")
                self.clear_display()
        else:
            self.feedback_label.config(text="")

    def clear_display(self):
        self.topic_label.config(text="")
        self.question_label.config(text="")
        self.code_label.config(text="")
        for button in self.answer_buttons:
            button.config(text="")
        self.current_question = None

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()