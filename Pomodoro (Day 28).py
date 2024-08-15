import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT  = "Courier"
WORK = 25
SHORT = 5
LONG  = 20

t = None
bra = None

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

timer = tkinter.Label()
timer.config(text = "Timer", fg = PINK, bg = YELLOW, font = (FONT, 20, "bold"))
timer.grid(column = 2, row = 1)

canvas = tkinter.Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness = 0)
tomato = tkinter.PhotoImage(file = r"D:\Yadh Documents\100 Days of Code Python\tomato.png")
canvas.create_image(100,110, image = tomato)
timer_text = canvas.create_text(100, 130, text = "00:00", font = (FONT, 30, "bold"), fill = "white")
canvas.grid(column = 2, row = 2)

br = tkinter.Label()
n = 0

check = tkinter.Label()

def st():
    countdown(1500)

start = tkinter.Button(text = "Start", command = st)
start.grid(column = 1, row = 3)


def re():
    global n
    n = 0
    if t:
        window.after_cancel(t)
    if bra:
        window.after_cancel(bra)
    canvas.itemconfig(timer_text,  text = "00:00")
    timer.config(text = "Timer")
    check.config(text = "")
    

reset = tkinter.Button(text = "Reset", command = re)
reset.grid(column = 3, row = 3)


def break_time(b):
    timer.config(text = "Break Time", fg = PINK, bg = YELLOW, font = (FONT, 20, "bold"))
    b_min = math.floor(b/60)
    b_sec = b % 60
    canvas.itemconfig(timer_text,  text = f"{b_min}:{b_sec:02d}")
    global bra
    if b > 0:
        bra = window.after(1000, break_time, b -1)
    elif b == 0:
        countdown(1500)

def end():
    timer.config(text = "", fg = PINK, bg = YELLOW, font = (FONT, 20, "bold"))
    canvas.itemconfig(timer_text,  text = "Session Complete", font = (FONT, 14, "bold"))

def countdown(count):
    global n
    timer.config(text = "Work", fg = PINK, bg = YELLOW, font = (FONT, 20, "bold"))
    br.config(text = "", bg = YELLOW)
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text,  text = f"{count_min}:{count_sec:02d}")
    global t
    if count > 0:
        t = window.after(1000, countdown, count -1)
    elif count == 0:
        if n < 5:
            global check
            check.config(text = "✅", bg = YELLOW)
            check.grid(column = 2, row = 4+n)
            break_time(300)
        else:
            end()
        n += 1

    

window.mainloop()