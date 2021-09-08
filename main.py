import tkinter


def button_click():
    print('i got clicked')
    header_label['text'] = new_input.get()


window = tkinter.Tk()
window.minsize(500, 500)


header_label = tkinter.Label(text='Title', font=('Arial', 24, 'bold'))
header_label.grid(column=0, row=0)


button = tkinter.Button(text='click me', command=button_click)
button.grid(column=1, row=1)

new_button = tkinter.Button(text='click me too')
new_button.grid(column=2, row=0)

new_input = tkinter.Entry(width=10)
new_input.grid(column=3, row=3)



window.mainloop()
# print(add(1, 2, 2))
#
# def add(*args):
#     x = 0
#     for i in args:
#         x += i
#     return x

