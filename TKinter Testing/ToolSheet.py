import tkinter as tk
# Definitions
# Calculator Definition
def Calculator():
    selection = input("would you like to add, subtract, multiply, or divide? \n")
    # addition
    if selection == "add":
        print("welcome to addition calculation")
        x = int(input("first number to add: "))
        y = int(input(" second number to add: "))
        addition = x + y
        print(addition)

        # subtraction
    elif selection == "subtract":
        print("welcome to subtraction calculation")

        # multiplication
    elif selection == "multiply":
        print("welcome to multiply calculation")
        
        # division
    elif selection == "divide":
        print("welcome to divide calculation")

# charLength Definition
def charLength():
    length = input("what is the string you would like to see length of?\n")
    length2 = length.replace(" ", "")
    print(len(length2))

 

#---------------------------------------------------------------
# window setup and styling
# window form
window = tk.Tk()

greeting = tk.Label(text="Welcome to My Utility Application")
greeting.pack()

# calculator button
calc = tk.Button(text="Calculator", command=Calculator)
calc.pack()

# charLength button
length = tk.Button(text="Find Length of String", command=charLength)
length.pack()

# loop to run window form
window.mainloop()