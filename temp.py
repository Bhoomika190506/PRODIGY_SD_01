import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp_input = entry_temp.get().strip()
        temp = float(temp_input)
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            result.set("Please select a valid unit.")

    except ValueError:
        result.set("")  # Clear previous result
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)
root.configure(bg="white")

# Widgets
tk.Label(root, text="Enter Temperature:", bg="white").pack(pady=(10, 2))
entry_temp = tk.Entry(root, width=20)
entry_temp.pack(pady=(0, 10))

tk.Label(root, text="Select Unit:", bg="white").pack(pady=(5, 2))
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.pack(pady=(0, 10))
combo_unit.current(0)  # Set default to "Celsius"

tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue", bg="white").pack(pady=10)

# Bind Enter key
root.bind('<Return>', lambda event: convert_temperature())

# Run the GUI
root.mainloop()

