import tkinter as tk

def on_button_click(event):
    # Get the button clicked
    clicked_button = event.widget
    button_text = clicked_button.cget("text")

    if button_text == "=":
        try:
            # Evaluate the expression
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        # Append the button text to the input field
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the input and result
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Define the button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place the buttons
row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", on_button_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main event loop
root.mainloop()
