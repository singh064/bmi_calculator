import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get user input from entry fields
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate input (must be positive values)
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive values.")
            return

        # BMI formula
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        result_label.config(text=f"BMI: {bmi} | Category: {category}")

    except ValueError:
        # Handle non-numeric input
        messagebox.showerror("Invalid Input", "Please enter numeric values")


# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x350")

# Title label
title_label = tk.Label(window, text="BMI Calculator", font=("Arial", 18))
title_label.pack(pady=10)

# Weight input
weight_label = tk.Label(window, text="Enter Weight (kg)")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

# Height input
height_label = tk.Label(window, text="Enter Height (metre):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Button to trigger BMI calculation
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Label to display result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the application
window.mainloop()