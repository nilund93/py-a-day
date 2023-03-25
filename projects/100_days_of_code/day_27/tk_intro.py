import tkinter

def button_clicked():
    print("I got clicked.")
    #my_label.config(text="Button Got Clicked")
    my_label.config(text=user_input.get())

window = tkinter.Tk()
window.title("Example")
window.minsize(width = 500, height = 300)
window.config(padx=20, pady=20)



# REMEMBER - PACK or GRID, not both
# Label
my_label = tkinter.Label(text="I am a label.", font = ("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100, y=0)

# my_label.pack(side="left", expand=True)
# my_label.pack(side="right")
# my_label.pack(side="top")
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
new_button = tkinter.Button(text="Click me too", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)

user_input = tkinter.Entry(width=10)
# user_input.pack(side="left")
user_input.grid(column=3, row=2)

window.mainloop()
