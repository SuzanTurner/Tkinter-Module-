import smtplib
import tkinter
from tkinter import messagebox
import pandas # type: ignore
import random
import math

window = tkinter.Tk()
window.minsize(width = 300, height = 200)
window.title("There's Hopes!!")
window.config(bg = "pink")

canvas = tkinter.Canvas(window, width = 350, height = 250, bg = "pink", highlightthickness=5)
canvas.grid(column = 1, row = 1, rowspan = 5, columnspan = 3)

def create_heart_points(scale):
    points = []
    for t in range(0, 360):
        angle = math.radians(t)
        x = 16 * math.sin(angle)**3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        points.append((scale * x, -scale * y))  
    return points

def move_heart(heart, x_velocity, y_velocity):
    canvas.move(heart, x_velocity, y_velocity)
    pos = canvas.coords(heart)
    window.after(20, move_heart, heart, x_velocity, y_velocity)
    

def draw_heart(scale):
    points = create_heart_points(scale)
    points = [(x + 320/2, y + 220/2) for x, y in points]
    return canvas.create_polygon(points, outline="red", fill="red", smooth=True)

def randomize_velocity():
    global x_velocity, y_velocity
    x_velocity = random.choice([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1, 1, 2, 3 ,4 ,5,6,7,8,9])
    y_velocity = random.choice([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1, 2, 3,4 ,5,6,7,8,9])
    return x_velocity, y_velocity

def spawn_heart():
    scale = random.choice([1,2,0.5,0.75])
    heart = draw_heart(scale)
    x_velocity, y_velocity = randomize_velocity()
    move_heart(heart, x_velocity, y_velocity)
    window.after(50, spawn_heart)

spawn_heart()
x_velocity
y_velocity

data = pandas.read_excel(r"D:\Yadh Documents\100 Days of Code Python\Sarcastic.xlsx")

email_text = tkinter.Text(width=30, height = 1)
email_text.focus()
email_text.grid(row = 2, column = 2, padx = 0, pady = 5)

email_label = tkinter.Label()
email_label.config(text = "Email:", bg = "pink",  font = ("Courier", 12, "normal"))
email_label.grid(row = 2, column = 1, padx =  0, pady = 5)

pwd = "xewr ldvh xkvy wclw"

text_label2 = tkinter.Label()

def send():
    to = email_text.get("1.0", tkinter.END)
    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user = "silvervoid3.14@gmail.com", password = pwd)
        message = data["Quotes"][random.randint(0,49)]
        m = f"Subject:Hope your day gets better!!\n\n{message}"
        body = m.encode('utf-8')
        con.sendmail(from_addr = "silvervoid3.14@gmail.com", 
                     to_addrs = to, 
                     msg = body)
    messagebox.showinfo(title = "Alert!", message="Mail has been sent succesfully!")
    text_label2.config(text = "Check your inbox!! 😎", bg = "pink",  font = ("Courier", 12, "normal"))
    text_label2.grid(row = 4, column = 1, columnspan=2)

send_button = tkinter.Button(text = "Send", command = send)
send_button.config(bg = "white", font =("Courier", 12, "bold") )
send_button.grid(column = 1, row = 3, columnspan = 2)

text_label = tkinter.Label()
text_label.config(text = "Making World Depression Rate 0 🥹🥹", bg = "pink",  font = ("Courier", 12, "normal"), highlightthickness=2, )
text_label.grid(row = 1, column = 1, columnspan = 2, padx =  5, pady = 5)

window.mainloop()
