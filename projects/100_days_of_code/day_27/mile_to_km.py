import tkinter

def calculate_km():
    
    mile_to_km = round(int(input_box.get()) * 1.609)
    calculation_label.config(text=str(mile_to_km))

window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width = 500, height = 300)
window.config(padx=20, pady=20)


input_box = tkinter.Entry(width=10)
input_box.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

calculation_label = tkinter.Label(text="0")
calculation_label.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)
window.mainloop()