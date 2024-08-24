import tkinter
import pandas
import random
import time

window = tkinter.Tk()
window.minsize(width = 400, height = 300)
window.title("Text Translation ")
window.config(padx = 20, pady = 20, background= "white")

data = pandas.read_excel(r"C:\Users\Yadhnesh\Dropbox\PC\Downloads\Hindi.xlsx")

CHANCES = 5
chances_label = tkinter.Label()
chances_label.config(text = f"Chances: {CHANCES}",font = ("Ariel", 12, "bold"))
chances_label.grid(column = 2, row = 3)

ans_label = tkinter.Label()
ans_label.config(padx = 40, font = ("Open Sans", 12, "normal"))
ans_label.grid(column = 2, row = 1)

canvas = tkinter.Canvas(width = 200, height = 200)
rect_img = tkinter.PhotoImage(file = r"C:\Users\Yadhnesh\Dropbox\PC\Downloads\Rounded-Rectangle.png")
canvas.create_image(100,110,image = rect_img)
canvas.grid(column = 1, row = 1)

i = random.randint(0,99)
card_text = canvas.create_text(100,110, text = f"{data.Hindi[i]}", font = ("Ariel", 20, "normal"))

ans_text = tkinter.Entry(window)
canvas.create_window(100, 150, window = ans_text, width = 100, height = 20)

def next_card():
    global i
    ans_label.config(text = "", bg = "white")
    i = random.randint(0,99)
    canvas.itemconfig(card_text, text = f"{data.Hindi[i]}")
    ans_text.delete(0,tkinter.END)
    
def tick():
    global i
    global CHANCES
    if data.English[i] == ans_text.get().title():
        ans_label.config(text = "Correct!!", bg = "white")
        time.sleep(1)
        window.after(1000,next_card)
    else:
        ans_label.config(text = "Wrong!!", bg = "white")
        CHANCES -= 1
        chances_label.config(text = f"Chances: {CHANCES}",font = ("Ariel", 12, "bold"))
        if CHANCES < 0:
            time.sleep(2)
            window.destroy()
        window.after(1000,next_card)

img = tkinter.PhotoImage(file = r"C:\Users\Yadhnesh\Dropbox\PC\Downloads\GreenTick.png")
tick_button = tkinter.Button(width = 50, height = 50, image = img, command = tick)
tick_button.grid(column = 1, row = 2)

def ex():
    window.destroy()

exit = tkinter.Button(text = "Exit", command = ex)
exit.config(width = 5)
exit.grid(column = 2, row = 2)

window.mainloop()