from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        """Set up GUI intererface"""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(340, 500)
        self.current_score = 0

        # Create trivia box
        self.canvas = Canvas(highlightthickness=0, height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question Text.", font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Button Functions
        def click_true():
            return "True"

        def click_false():
            return "False"

        # Create Buttons
        self.false_image = PhotoImage(file='images/false.png')
        self.true_image = PhotoImage(file='images/true.png')

        self.false_button = Button(image=self.false_image, activebackground=THEME_COLOR, bd=0, highlightthickness=0,
                                   bg=THEME_COLOR,  command=click_false)
        self.true_button = Button(image=self.true_image, activebackground=THEME_COLOR, bd=0, highlightthickness=0,
                                  bg=THEME_COLOR, command=click_true)

        self.false_button.grid(row=2, column=1, sticky='EW', pady=(20, 0))
        self.true_button.grid(row=2, column=0, sticky='EW', pady=(20, 0))

        # Score label
        self.score = Label(text=f"Score: {self.current_score}", font=("Arial", 12, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=(0, 20))



        self.window.mainloop()
