import tkinter as tk

# Function to handle calculations
def calculate():
    try:
        # Get values and operation
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation_var.get()
        
        # Perform calculation
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": 
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
            
        # Display result (convert to int if it's a whole number)
        result = int(result) if result == int(result) else round(result, 2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("250x150")

# Create input fields and dropdown
entry1 = tk.Entry(window, width=5)
entry1.grid(row=0, column=0, padx=5, pady=10)

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(window, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0, column=1, padx=5, pady=10)

entry2 = tk.Entry(window, width=5)
entry2.grid(row=0, column=2, padx=5, pady=10)

# Calculate button
tk.Button(window, text="=", command=calculate).grid(row=1, column=0, columnspan=3, pady=5)

# Result display
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=5)

# Start application
window.mainloop()