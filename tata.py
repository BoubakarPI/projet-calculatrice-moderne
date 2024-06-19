from tkinter import *

root = Tk()
fontFamily = ('monospace', 40)
btnFontSize = 50

output = Label(root, fg='#FF595E', font=('monospace', 25), width=20)
output.grid(row=0, column=0, columnspan=40)


def add_txt(char):
    output['text'] += char


def clear_txt():
    output['text'] = ''


def calcul_txt():
    output['text'] = str(eval(output['text']))


Button(root, text='1', font=fontFamily, command=lambda: add_txt('1')).grid(row=1, column=0)
Button(root, text='2', font=fontFamily, command=lambda: add_txt('2')).grid(row=1, column=1)
Button(root, text='3', font=fontFamily, command=lambda: add_txt('3')).grid(row=1, column=2)

Button(root, text='4', font=fontFamily, command=lambda: add_txt('4')).grid(row=2, column=0)
Button(root, text='5', font=fontFamily, command=lambda: add_txt('5')).grid(row=2, column=1)
Button(root, text='6', font=fontFamily, command=lambda: add_txt('6')).grid(row=2, column=2)

Button(root, text='7', font=fontFamily, command=lambda: add_txt('7')).grid(row=3, column=0)
Button(root, text='8', font=fontFamily, command=lambda: add_txt('8')).grid(row=3, column=1)
Button(root, text='9', font=fontFamily, command=lambda: add_txt('9')).grid(row=3, column=2)

Button(root, text='C', font=fontFamily, command=clear_txt).grid(row=4, column=0)
Button(root, text='0', font=fontFamily, command=lambda: add_txt('0')).grid(row=4, column=1)
Button(root, text='=', font=fontFamily, command=calcul_txt).grid(row=4, column=2)

Button(root, text='+', font=fontFamily, command=lambda: add_txt('+')).grid(row=1, column=3)
Button(root, text='-', font=fontFamily, command=lambda: add_txt('-')).grid(row=2, column=3)
Button(root, text='*', font=fontFamily, command=lambda: add_txt('*')).grid(row=3, column=3)
Button(root, text='/', font=fontFamily, command=lambda: add_txt('/')).grid(row=4, column=3)

root.mainloop()