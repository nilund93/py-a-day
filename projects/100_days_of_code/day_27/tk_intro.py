import tkinter

def button_clicked():
    print("I got clicked.")
    #my_label.config(text="Button Got Clicked")
    my_label.config(text=user_input.get())

window = tkinter.Tk()
window.title("Example")
window.minsize(width = 500, height = 300)


# Label
my_label = tkinter.Label(text="I am a label.", font = ("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left", expand=True)
# my_label.pack(side="right")
# my_label.pack(side="top")
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

user_input = tkinter.Entry(width=10)
user_input.pack()
print(user_input.get())

window.mainloop()
