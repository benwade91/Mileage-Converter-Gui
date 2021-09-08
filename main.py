import tkinter


def calculate():
    m = int(mileage_input.get())
    km = round(m * 1.6)
    kilometers['text'] = km


window = tkinter.Tk()
window.title("Miles to Km Conversion")
window.config(padx=120, pady=100)
window.minsize(500, 300)


mileage_input = tkinter.Entry(width=10)
mileage_input.grid(column=1, row=0)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal = tkinter.Label(text="is equal to")
is_equal.grid(column=0, row=1)


kilometers = tkinter.Label(text=0)
kilometers.grid(column=1, row=1)


km_label = tkinter.Label(text="Kilometers")
km_label.grid(column=2, row=1)


button = tkinter.Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)


window.mainloop()

