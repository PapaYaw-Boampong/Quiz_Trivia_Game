from tkinter import *
from quiz_brain import QuizBrain
from timer import Timer
import data

BLUE = '#7EC4CF'
BACKGROUND = '#001A23'
TITLE = ("Arial", 25, "bold")
SUBTITLE = ("Arial", 20, "bold")
FONTCOLOR = "white"


class QuizInterface:
    def __init__(self, timer: Timer):
        # window setup
        self.quiz = QuizBrain(data.generate_questions())
        self.timer = Timer()
        self.window = Tk()
        self.window.title("General Trivia")
        self.window.config(padx=70, pady=60, bg=BACKGROUND)
        self.window.geometry("850x620")

        # Question and picture canvas setup
        # image canvas
        self.canvas = Canvas(
            width=300, height=385,
            bg=BACKGROUND, highlightthickness=0)
        img = PhotoImage(file="images\\brain4.png")
        self.canvas.create_image(150, 175, image=img)
        self.canvas.grid(column=1, row=2, rowspan=2)

        # question canvas
        self.question_canvas = Canvas(
            width=450,
            height=296,
            bg=BACKGROUND,
            highlightthickness=0)
        img2 = PhotoImage(file="images\\card_front.png")
        self.question_canvas.create_image(225, 148, image=img2)
        self.question_canvas.grid(column=2, row=3, columnspan=4, pady=30)

        # Labels
        self.timer_label = Label(
            text=f" Time \n 00:00",
            font=SUBTITLE, fg=FONTCOLOR,
            bg=BACKGROUND)
        self.timer_label.grid(column=1, row=4, )
        self.question_no_label = Label(
            text=f"Question: {self.quiz.question_number}    Score {self.quiz.score} / 10",
            font=TITLE,
            fg=FONTCOLOR, bg=BACKGROUND)
        self.question_no_label.grid(row=2, column=2, columnspan=3)
        self.current_question = self.question_canvas.create_text(
            220, 150,
            text=self.quiz.current_question.text,
            font=SUBTITLE, justify="center", width=320)

        # Buttons
        correct_img = PhotoImage("images/true.png")
        wrong_img = PhotoImage("images/false.png")
        self.true_button = Button(
            text="true",
            font=("Arial", 18, "bold"),
            bg="#80D39B",
            width=7,
            highlightthickness=0,
            command=lambda: self.load("true"))
        self.true_button.grid(row=4, column=2)

        self.false_button = Button(
            text="false",
            font=("Arial", 18, "bold"),
            width=7,
            highlightthickness=0, bg="#FF1053",
            command=lambda: self.load("false"))

        self.false_button.grid(row=4, column=4)

        self.restart_button = Button(
            text="Restart",
            font=("Arial", 18, "bold"),
            highlightthickness=0,
            bg="#7D70BA", bd=2,
            command=lambda: self.restart_display(data.generate_questions()))
        self.restart_button.grid(column=1, row=5)
        timer.update_clock(
            self.quiz,
            self.timer_label,
            self.window)
        self.window.mainloop()

    # Load function records a "true" or "false" response to a current_question
    def load(self, ans: str):
        if self.quiz.check_answer(ans):
            self.question_canvas.itemconfig(self.current_question, fill="#0CCE6B")
        else:
            self.question_canvas.itemconfig(self.current_question, fill="#C1292E")
        self.window.after(1000, self.update)

    # Update Function refreshes the Question display after a current_question is answered
    def update(self):
        if self.quiz.has_question:
            self.question_canvas.itemconfig(
                self.current_question,
                text=self.quiz.next_question().text,
                fill="black")
            self.question_no_label.config(
                text=f"   Question: {self.quiz.question_number}    Score {self.quiz.score}/10", )
        else:
            if self.quiz.score < 7:
                self.question_canvas.itemconfig(
                    self.current_question,
                    text=f" End of QuiZ :)\n\n Practice makes perfect",
                    fill="black")
            elif self.quiz.score < 9:
                self.question_canvas.itemconfig(
                    self.current_question,
                    text=f" End of QuiZ :) \n\n Amazing Performance",
                    fill="black")
            else:
                self.question_canvas.itemconfig(
                    self.current_question,
                    text=f" End of QuiZ :) \n\n That's Brainy  :)",
                    fill="black")
            self.quiz.has_question = False
        self.quiz.update_has_question()

    def restart_display(self, questions):
        self.quiz.reset_quiz(questions)
        self.question_canvas.itemconfig(
            self.current_question,
            text=self.quiz.current_question.text,
            fill="black")
        self.question_no_label.config(text=f"Question: {self.quiz.question_number}    Score {self.quiz.score}/10")
        self.timer.reset_timer()
        self.timer.update_clock(self.quiz,
                                self.timer_label,
                                self.window)
