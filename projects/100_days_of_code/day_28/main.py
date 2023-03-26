import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # WHY ARE WE USING GLOBALS, LIKE WTF
check_marks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, check_marks, reps
    
    window.after_cancel(timer)
    check_marks = 0
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    label.config(text="Timer", foreground=GREEN)
    check_label.config(text=f"{'✔'*check_marks}")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", foreground=GREEN) 
    
    
    
    # count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# def say_something(thing):
#     print(thing)
    
def count_down(count):
    global timer
    
    minutes = count // 60
    seconds = count % 60
    
    canvas.itemconfig(timer_text, text=f"{minutes:02.0f}:{seconds:02.0f}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks += 1 
        check_label.config(text=f"{'✔'*check_marks}")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# window.after(1000, say_something, "hello", "hi", "im the problem", "its me")


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

label = tkinter.Label(text="Timer", font=(FONT_NAME, 36, "bold"), foreground=GREEN, bg=YELLOW)
label.grid(column=1, row=0)
# 

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


check_label = tkinter.Label(text="", font=(FONT_NAME, 16, "bold"), foreground=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
window.mainloop()
