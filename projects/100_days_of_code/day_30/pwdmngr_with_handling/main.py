from tkinter import *
from tkinter import messagebox
from string import ascii_letters, digits
from random import choice 
import json

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
    new_data = {
        website:{
            "email": name,
            "password": password,
            }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:    
        # messagebox.showinfo(title="Title", message="Message")
        output = messagebox.askokcancel(title=website, message=f"These are the details entered: \nName/Email:{name}\nPassword:{password}\nIs it ok to save?")
        if output:
            try:
                with open("data.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    print(data)
                    data.update(new_data)
            except FileNotFoundError:
                print("File does not exist. Creating file now.")
                with open("data.json", "w", encoding="utf-8") as f: json.dump(new_data, f, indent=4)
            else:    
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
            finally:     
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                
# ---------------------------- PWD SEARCH ------------------------------- #             
def search_pwd():
    search_phrase = website_entry.get()
    
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            entries = json.load(f)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Data file not found.")
    else:
        if search_phrase in entries:
            messagebox.showinfo(title="Password found!", message=f"{search_phrase}\n{entries[search_phrase]['email']}\n{entries[search_phrase]['password']}")
        else:
            messagebox.showinfo(title="Not found", message="No such users were found for that website.")
            
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
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Radiobutton(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, sticky="EW")
search_button = Button(text="Search", width=36, command=search_pwd)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()