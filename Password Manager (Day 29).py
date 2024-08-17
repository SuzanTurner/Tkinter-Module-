import tkinter
import random
from tkinter import messagebox

window = tkinter.Tk()
window.minsize(width = 200, height = 150)
window.config(padx = 15, pady = 20)

canvas = tkinter.Canvas()
img = tkinter.PhotoImage(file = r"D:\Yadh Documents\100 Days of Code Python\logo.png")
canvas.create_image(190,100, image = img)
canvas.grid(column = 1, row = 1, columnspan = 3)

site_label = tkinter.Label(padx = -40, pady = 5, text = "Site:", anchor = "w")
site_label.grid(column = 1, row = 2)

site_text = tkinter.Text(width = 40, height = 1)
site_text.grid(column = 2, row = 2, columnspan = 2)

mail_label = tkinter.Label( pady = 5, text = "Email/Username:",  anchor = "w", width = 18)
mail_label.grid(column = 1, row = 3)

mail_text = tkinter.Text(width = 40, height = 1)
mail_text.grid(column = 2, row = 3, columnspan = 2)

password_label = tkinter.Label(pady = 5, text = "Password:",  anchor = "w")
password_label.grid(column = 1, row = 4)

password_text = tkinter.Text(width = 25, height = 1)
password_text.grid(column = 2, row = 4)

def genpass():
    smolchars = [chr(i) for i in range(97, 123)]
    capchars = [chr(i) for i in range(65, 91)]
    numbers = [i for i in range(0,10)]
    splchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-']
    chars = smolchars + capchars + numbers + splchars
    password = ""
    password_text.delete("1.0", tkinter.END)
    while len(password) < 16:
        c = str(random.choice(chars))
        password += c
    password_text.insert("1.0", password)
    
genpass_button = tkinter.Button(text = "Generate Password", command = genpass, width = 15)
genpass_button.grid(column = 3, row = 4)


def add():
    site = site_text.get("1.0", tkinter.END)
    mail = mail_text.get("1.0", tkinter.END)
    password = password_text.get("1.0", tkinter.END)
    if (len(site) == 1 or len(mail) == 1 or len(password) == 1):
        messagebox.showinfo(title = "alert!", message = "Do not leave anything empty")
    else:
        ok = messagebox.askokcancel(title = "Alert!", message = f"These are the details you have entered \n Site: {site} \n Username\Email: {mail} \n Password: {password}")

    if ok:
        with open(r"D:\Yadh Documents\100 Days of Code Python\Password_Data.txt", 'a') as file:
            file.write ("Site: "+ site + "Email/Username: " + mail + "Password" + password + "\n")
        site_text.delete("1.0", tkinter.END)
        mail_text.delete("1.0", tkinter.END)
        password_text.delete("1.0", tkinter.END)
        messagebox.showinfo(title = "Task Complete", message = "Your information has been saved succesfully!")


add_button = tkinter.Button(text = "Add", command = add, width = 40)
add_button.grid(column = 2, row = 5, columnspan = 2)



window.mainloop()