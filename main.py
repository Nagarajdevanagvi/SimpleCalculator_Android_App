import customtkinter as ctk

# Initialize the app
ctk.set_appearance_mode("dark")  # Dark theme
ctk.set_default_color_theme("blue")  # Button color

app = ctk.CTk()
app.title("Simple Calculator")
app.geometry("300x450")

# Entry Field
entry = ctk.CTkEntry(app, width=280, height=40, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# History Display
history_label = ctk.CTkLabel(app, text="History:", font=("Arial", 14))
history_label.grid(row=5, column=0, columnspan=4)
history_text = ctk.CTkTextbox(app, height=80, width=280)
history_text.grid(row=6, column=0, columnspan=4, padx=10, pady=5)

# Function to update entry field
def button_click(value):
    current_text = entry.get()
    if current_text == "Error":
        entry.delete(0, "end")  # Clear previous error
    entry.insert("end", value)

# Function to clear entry
def clear():
    entry.delete(0, "end")

# Function to clear history
def clear_history():
    history_text.delete("1.0", "end")

# Function to evaluate expression
def calculate():
    try:
        expression = entry.get()
        if "/0" in expression:
            raise ZeroDivisionError  # Prevent division by zero
        result = eval(expression)  # Calculate result
        entry.delete(0, "end")
        entry.insert("end", str(result))
        
        # Update history
        history_text.insert("end", f"{expression} = {result}\n")
        history_text.see("end")  # Auto-scroll to latest
    except ZeroDivisionError:
        entry.delete(0, "end")
        entry.insert("end", "Error (Div by 0)")
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# Button Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for text, row, col in buttons:
    if text == "=":
        btn = ctk.CTkButton(app, text=text, width=60, height=40, command=calculate)
    elif text == "C":
        btn = ctk.CTkButton(app, text=text, width=60, height=40, command=clear)
    else:
        btn = ctk.CTkButton(app, text=text, width=60, height=40, command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear History Button
clear_history_btn = ctk.CTkButton(app, text="Clear History", width=280, height=30, command=clear_history)
clear_history_btn.grid(row=7, column=0, columnspan=4, pady=5)

app.mainloop()




