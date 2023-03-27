from tkinter import *
from tkinter import messagebox
from string import ascii_letters, digits
from random import choice 

DEFAULT_EMAIL = "lundniclas@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    generated_pwd = ""
    characters = ascii_letters + digits + "!#$%&()*+"
    for _ in range(16): generated_pwd += choice(characters)
    password_entry.insert(0,generated_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    name = name_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:    
        # messagebox.showinfo(title="Title", message="Message")
        output = messagebox.askokcancel(title=website, message=f"These are the details entered: \nName/Email:{name}\nPassword:{password}\nIs it ok to save?")
        if output:
            with open("data.txt", "a", encoding="utf-8") as f:
                f.write(f"{website} | {name} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
name_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
name_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Textboxes
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
name_entry = Entry(width=35)
name_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
name_entry.insert(0, DEFAULT_EMAIL)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")



# Buttons
generate_button = Button(text="Generate Password", command=generate)
add_button = Radiobutton(text="Add", width=36, command=save)
generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, sticky="EW")


window.mainloop()