# Author: Majaliwa Wilfred
# Session: Morning
# Assignment: Create a simple calculator program with a GUI Interface.
# Make the title of the calculator program window your name e.g "Wilfred Majaliwa Simple Calculator"

# Tcl/Tk version: 8.6

# import TKInter as tk
import tkinter as tk

window = tk.Tk()
# set window dimensionns
calc_height = "400"
calc_width = "304"
btn_width = 4
btn_height = 3
font_size = 16

window.geometry(f"{calc_width}x{calc_height}")
# Don't allow resizing the window
window.resizable(0, 0)

# set title of window/app
window.title("Wilfred Majaliwa Simple Calculator")

screen = tk.Text(window, width=33, height=btn_height, font=('Arial', 16), padx=2, pady=2)
screen.grid(
    row= 1,
    columnspan=6
)

# DEFINE FUNCTIONS
operation = ""

def add(symbol):
    global operation
    operation += str(symbol)
    screen.delete(1.0, tk.END)
    screen.insert(1.0, operation)

def evaluate():
    global operation
    try:
        operation = str(eval(operation))
        screen.delete(1.0, tk.END)
        screen.insert(1.0, operation)
    except Exception as err:
        clear()
        screen.insert(1.0, f"Error: {err}")
    # finally:
    #     operation = ""

def clear():
    global operation
    operation = ""
    screen.delete(1.0, tk.END)

# def clear_single():
#     global operation
#     operation[:-1]
#     screen.delete(1.0, -1)
def clear_single():
    global operation
    operation = operation[:-1]  # Remove the last character from the 'operation' variable
    screen.delete("end-2c", "end-1c")  # Delete the last character from the 'screen' widget


# MISC
# note: command=clear() woould immediately call the function
btn_clear = tk.Button(window, text="AC", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: clear())
btn_clear.grid(
    row=2,
    column=1
)

# Left bracket (
btn_left_bracket = tk.Button(window, text="(", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("("))
btn_left_bracket.grid(
    row=2,
    column=2
)

# Right bracket )
btn_right_bracket = tk.Button(window, text=")", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(")"))
btn_right_bracket.grid(
    row=2,
    column=3
)

# Number Buttons

btn_7 = tk.Button(window, text="7", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(7))
btn_7.grid(
    row=3,
    column=1
)

btn_8 = tk.Button(window, text="8", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(8))
btn_8.grid(
    row=3,
    column=2
)

btn_9 = tk.Button(window, text="9", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(9))
btn_9.grid(
    row=3,
    column=3
)

btn_4 = tk.Button(window, text="4", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(4))
btn_4.grid(
    row=4,
    column=1
)

btn_5 = tk.Button(window, text="5", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(5))
btn_5.grid(
    row=4,
    column=2
)

btn_6 = tk.Button(window, text="6", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(6))
btn_6.grid(
    row=4,
    column=3
)

btn_1 = tk.Button(window, text="1", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(1))
btn_1.grid(
    row=5,
    column=1
)

btn_2 = tk.Button(window, text="2", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(2))
btn_2.grid(
    row=5,
    column=2
)

btn_3 = tk.Button(window, text="3", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(3))
btn_3.grid(
    row=5,
    column=3
)

btn_0 = tk.Button(window, text="0", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add(0))
btn_0.grid(
    row=6,
    column=1
)

btn_dot = tk.Button(window, text=".", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("."))
btn_dot.grid(
    row=6,
    column=2
)

btn_del = tk.Button(window, text="⌫", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: clear_single())
btn_del.grid(
    row=6,
    column=3
)

# Operator Buttons

# Divide
btn_divide = tk.Button(window, text="/", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("/"))
btn_divide.grid(
    row=2,
    column=4
)
# Multiplication
btn_multiplication = tk.Button(window, text="*", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("*"))
btn_multiplication.grid(
    row=3,
    column=4
)
# Subtraction
btn_subtraction = tk.Button(window, text="-", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("-"))
btn_subtraction.grid(
    row=4,
    column=4
)
# Addition
btn_addition = tk.Button(window, text="+", width=btn_width, height=btn_height, font=("Arial", font_size), command=lambda: add("+"))
btn_addition.grid(
    row=5,
    column=4
)
# Equals
btn_equals = tk.Button(window, text="=", width=btn_width, height=btn_height, font=("Arial", font_size), command=evaluate)
btn_equals.grid(
    row=6,
    column=4
)

window.mainloop()
