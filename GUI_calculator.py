from tkinter import *

computation = []


def display_result():
    number = 0
    numbers = []
    sign = ""
    aid = 0
    for i in range(1, len(computation) + 1):
        power = 10**aid
        if computation[-i] == "*" or computation[-i] == "+" or computation[-i] == "-":
            numbers.append(number)
            sign = computation[-i]
            number = 0
            aid = 0
        else:
            number += computation[-i] * power
            aid += 1

        if i == len(computation):
            numbers.append(number)

            if sign == "+":
                result = numbers[0] + numbers[1]
            elif sign == "*":
                result = numbers[0] * numbers[1]
            elif sign == "-":
                result = numbers[1] - numbers[0]
            else:
                result = numbers[0]

            label_result.config(text=str(result))
            computation.clear()
            computation.append(result)
            break


def add_sign(sign):
    computation.append(sign)
    if len(computation) == 0:
        label_computations.config(text="0")
    else:
        text = ""
        for i in computation:
            text = text + str(i)

        label_computations.config(text=f"{text}")


def clear_content():
    computation.clear()
    label_computations.config(text="")
    label_result.config(text="0")


root = Tk()
root.title("")
root.geometry("700x300")

upper_frame = Frame(root)
lower_frame = Frame(root)

upper_frame.grid(row=0, column=0, sticky=N)
lower_frame.grid(row=1, column=0, sticky=S)

label_computations = Label(
    upper_frame, width=18, height=4, bg="lightgrey", text="", anchor=E
)
label_result = Label(upper_frame, width=18, height=4, bg="white", text="0", anchor=E)


label_computations.grid(row=0, column=0)
label_result.grid(row=1, column=0)

button_seven = Button(lower_frame, text="7", width=3, command=lambda: add_sign(7))
button_eight = Button(lower_frame, text="8", width=3, command=lambda: add_sign(8))
button_nine = Button(lower_frame, text="9", width=3, command=lambda: add_sign(9))
button_multiplication = Button(
    lower_frame, text="*", width=3, command=lambda: add_sign("*")
)
button_four = Button(lower_frame, text="4", width=3, command=lambda: add_sign(4))
button_five = Button(lower_frame, text="5", width=3, command=lambda: add_sign(5))
button_six = Button(lower_frame, text="6", width=3, command=lambda: add_sign(6))
button_subtraction = Button(
    lower_frame, text="-", width=3, command=lambda: add_sign("-")
)
button_one = Button(lower_frame, text="1", width=3, command=lambda: add_sign(1))
button_two = Button(lower_frame, text="2", width=3, command=lambda: add_sign(2))
button_three = Button(lower_frame, text="3", width=3, command=lambda: add_sign(3))
button_addition = Button(lower_frame, text="+", width=3, command=lambda: add_sign("+"))
button_zero = Button(lower_frame, text="0", width=3, command=lambda: add_sign(0))
button_rs = Button(lower_frame, text="=", width=6, command=display_result)
button_clear_content = Button(lower_frame, text="R", width=3, command=clear_content)

button_seven.grid(row=0, column=0)
button_eight.grid(row=0, column=1)
button_nine.grid(row=0, column=2)
button_multiplication.grid(row=0, column=3)
button_four.grid(row=1, column=0)
button_five.grid(row=1, column=1)
button_six.grid(row=1, column=2)
button_subtraction.grid(row=1, column=3)
button_one.grid(row=2, column=0)
button_two.grid(row=2, column=1)
button_three.grid(row=2, column=2)
button_addition.grid(row=2, column=3)
button_zero.grid(row=3, column=0)
button_rs.grid(row=3, column=1, columnspan=2)
button_clear_content.grid(row=3, column=3)


root.mainloop()
