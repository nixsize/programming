from tkinter import *

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        result_label.config(text="Введены некорректные данные")

window = Tk()

label1 = Label(window, text="Первое число")
label1.pack()
entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Второе число")
label2.pack()
entry2 = Entry(window)
entry2.pack()

button = Button(window, text="Сложить", command=add_numbers)
button.pack()

result_label = Label(window, text="Результат:")
result_label.pack()

window.mainloop()