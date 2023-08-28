import tkinter as tk
import random
# creating the actual program window
window = tk.Tk()

# creating the opening label
greeting = tk.Label(text="Welcome")
greeting.pack()
# -----------------------------------
# def for the hello world button
def HelloWorld():
    print("hello world")

# creating the button icon
button = tk.Button(text="generate hello world", command=HelloWorld)
button.pack()
# ----------------------------------
# def for the randomizer button
def randomizer():
    num = random.randint(1, 10)
    print(num)


# this button will generate a random number
ranButton = tk.Button(text="Click to Generate a Random Numver 1 - 10", command=randomizer)
ranButton.pack()

# -----------------------------------

# this is required in order for it to work
window.mainloop()