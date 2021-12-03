import tkinter
from tkinter import Button, Canvas, Label, PhotoImage
import math
from playsound import playsound
from threading import Thread

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ----- Timer reset ----- #
def reset_timer():
    start_button.config(state='normal')
    reset_button.config(state='disabled')

    # Prevent timer jump from 'Work' to 'Break' after reset
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')


# -----  Timer mechanism ----- #
def start_timer():
    start_button.config(state='disabled')
    reset_button.config(state='normal')

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        break_bell = Thread(target=break_sound)
        break_bell.start()
        focus_window()
        countdown(long_break_sec)
        title_label.config(text='Break', fg=RED)
        write_log()
    elif reps % 2 == 0:
        break_bell = Thread(target=break_sound)
        break_bell.start()
        focus_window()
        countdown(short_break_sec)
        title_label.config(text='Break', fg=PINK)
        write_log()
    else:
        wind_up = Thread(target=wind_up_sound)
        wind_up.start()
        focus_window()
        countdown(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ----- Countdown mechanism ----- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔️'
        check_marks.config(text=marks)


# ----- Create Log ----- #
def write_log():
    from datetime import datetime
    with open('log/pomodoro_log.dat', 'a') as logfile:
        now = datetime.now()
        dt_string = now.strftime('%d/%m/%Y %H:%M\n')
        log_text = f'Study length: {WORK_MIN} minutes. Study Session time: {dt_string}'
        logfile.write(log_text)


# ----- Focus window ----- #
def focus_window():
    window.deiconify()
    window.focus_force()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# ----- Sounds ----- #
def wind_up_sound():
    playsound('sounds/wind_up.mp3')


def break_sound():
    playsound('sounds/break.mp3')


# ----- UI Setup ----- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=202, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='img/tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 140, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer, state='normal')
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer, state='disabled')
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
