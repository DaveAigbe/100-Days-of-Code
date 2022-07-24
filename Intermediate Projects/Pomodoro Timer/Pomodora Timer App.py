from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(fg=GREEN)
    timer_label.config(text='Timer')
    timer_label.place(x=175, y=80)
    checkmark_label.config(text='')
    canvas.itemconfig(timer_text, text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # each time the timer is called again, add one to the amount of sessions completed
    work_time = WORK_MIN * 60
    sb_time = SHORT_BREAK_MIN * 60
    lb_time = LONG_BREAK_MIN * 60
    if reps == 9:
        timer_label.config(text='Session Complete')
        reset_timer()
    elif reps == 8:  # if user is at the last session, give them long break
        # Changing Colors
        timer_label.config(fg=RED)

        # Center Text
        timer_label.place(x=105, y=80)

        timer_label.config(text='Long Break')
        count_down(lb_time)
    elif reps % 2 == 0:  # if user is at any even numbered session, give them short break
        # Changing Colors
        timer_label.config(fg=PINK)

        # Center Text
        timer_label.place(x=170, y=80)

        timer_label.config(text='Break')
        count_down(sb_time)
    else:  # All odd sessions will be work periods
        # Changing Colors
        timer_label.config(fg=GREEN)

        # Center Text
        timer_label.place(x=190, y=80)

        timer_label.config(text='Work')
        count_down(work_time)  # pass through the amount of time for each session to the count_down function


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = int(count / 60)  # count is the amount of seconds
    count_sec = count % 60  # remainder from 60 will be seconds left
    if count_sec < 10:  # if the seconds are under 10 format it as 00 instead of just 0
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # changing the canvas text, to 00:00 format
    if count > 0:  # as long as the seconds are over 0
        timer = window.after(1000, count_down,
                             count - 1)  # continue to call this function after 1 second and replace the count variable with count-1
    else:  # if timer has reached 0
        start_timer()  # call the timer again to figure out what action will be taken next
        sessions = int(reps / 2)  # the amount of work sessions in the timer
        checks = f"{sessions}"  # in between the start and reset button, display the amount of work sessions created
        checkmark_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')

canvas = Canvas(width=500, height=524, bg=YELLOW, highlightthickness=0)  # Canvas module that holds pictures
tomato_img = PhotoImage(file="tomato.png")  # Store the image
canvas.create_image(250, 262, image=tomato_img)  # Create the image on the canvas at the specified coordinates
timer_text = canvas.create_text(250, 282, fill='white', font=(FONT_NAME, 35, "bold"))  # Create text for the image
canvas.pack()  # Place all of it on the screen

timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.place(x=175, y=80)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.place(x=240, y=410)

start_button = Button(text='►', bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=0, bd=0,
                      command=start_timer)
start_button.place(x=120, y=405)

reset_button = Button(text='⭮', bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=0, bd=0,
                      command=reset_timer)
reset_button.place(x=358, y=407)

window.mainloop()
