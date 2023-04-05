from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain: QuizBrain = quiz_brain
        
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width = 300, height = 250, background="white")
        self.statement_text = self.canvas.create_text(150, 
                                                      125, 
                                                      width=280,
                                                      text="Some statement.",
                                                      font=FONT,
                                                      fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.check_answer_true)
        self.true_btn.grid(column=0, row=2)
        
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.check_answer_false)
        self.false_btn.grid(column=1, row=2)
        
        self.get_next_question()
        self.window.mainloop()
    
    def check_answer_true(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    
    def check_answer_false(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)
        
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.statement_text, text=q_text)
        else:
            self.canvas.itemconfig(self.statement_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)