import tkinter as tk
from tkinter import ttk

# Conversion Logic
def convert_units(value, from_unit, to_unit, unit_type):
    conversions = {
        'Length': {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254},
        'Weight': {'kg': 1, 'g': 0.001, 'mg': 0.000001, 'lb': 0.453592, 'oz': 0.0283495},
        'Area': {'sq_m': 1, 'sq_km': 1_000_000, 'sq_ft': 0.092903, 'sq_yd': 0.836127, 'sq_mi': 2_589_988.11, 'acre': 4046.86, 'hectare': 10_000},
        'Volume': {'l': 1, 'ml': 0.001, 'm3': 1000, 'gal': 3.78541, 'qt': 0.946353, 'pt': 0.473176, 'cup': 0.24, 'floz': 0.0295735},
        'Time': {'sec': 1, 'min': 60, 'hr': 3600, 'day': 86400},
        'Force': {'N': 1, 'dyn': 1e-5, 'lbf': 4.44822, 'kgf': 9.80665, 'pdl': 0.138255},
        'Power': {'W': 1, 'kW': 1000, 'hp': 745.7, 'BTU/h': 0.293071, 'cal/s': 4.184}
    }

    try:
        factor_from = conversions[unit_type][from_unit]
        factor_to = conversions[unit_type][to_unit]
        return value * factor_from / factor_to
    except:
        return "Invalid"

def convert_temperature(value, from_unit, to_unit):
    try:
        if from_unit == 'C':
            return value * 9/5 + 32 if to_unit == 'F' else value + 273.15
        elif from_unit == 'F':
            return (value - 32) * 5/9 if to_unit == 'C' else (value - 32) * 5/9 + 273.15
        elif from_unit == 'K':
            return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9/5 + 32
        else:
            return "Invalid"
    except:
        return "Invalid"

# GUI Functions
def convert():
    try:
        val = float(entry_value.get())
        from_u = combo_from.get()
        to_u = combo_to.get()
        cat = combo_category.get()

        if not from_u or not to_u or not cat:
            label_result.config(text="Error: Please select all fields.")
            return

        if cat == "Temperature":
            result = convert_temperature(val, from_u, to_u)
        else:
            result = convert_units(val, from_u, to_u, cat)

        label_result.config(text=f"Result: {round(result, 4)} {to_u}")
    except:
        label_result.config(text="Error: Invalid input")

def update_units(event):
    category = combo_category.get()
    units = {
        'Length': ['m', 'km', 'cm', 'mm', 'mi', 'yd', 'ft', 'in'],
        'Weight': ['kg', 'g', 'mg', 'lb', 'oz'],
        'Area': ['sq_m', 'sq_km', 'sq_ft', 'sq_yd', 'sq_mi', 'acre', 'hectare'],
        'Volume': ['l', 'ml', 'm3', 'gal', 'qt', 'pt', 'cup', 'floz'],
        'Time': ['sec', 'min', 'hr', 'day'],
        'Temperature': ['C', 'F', 'K'],
        'Force': ['N', 'dyn', 'lbf', 'kgf', 'pdl'],
        'Power': ['W', 'kW', 'hp', 'BTU/h', 'cal/s']
    }

    unit_list = units.get(category, [])
    combo_from['values'] = unit_list
    combo_to['values'] = unit_list
    combo_from.set('')
    combo_to.set('')

# Setup Main Window
root = tk.Tk()
root.title("Beautiful Unit Converter")
root.geometry("500x450")
root.configure(bg="#2e3f4f")  # Background color

# Title
tk.Label(root, text="🌟 UNIT CONVERTER  ", font=('Segoe UI', 22, 'bold'), bg="#2e3f4f", fg="white").pack(pady=20)

# Style ttk widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", font=('Segoe UI', 12), fieldbackground="white", background="white", padding=8)
style.configure("TButton", font=('Segoe UI', 14, 'bold'), padding=10)

# Frame for form
frame = tk.Frame(root, bg="#2e3f4f")
frame.pack(pady=15)

def styled_label(master, text, row):
    lbl = tk.Label(master, text=text, font=('Segoe UI', 12, 'bold'), bg="#2e3f4f", fg="white")
    lbl.grid(row=row, column=0, sticky="w", padx=15, pady=8)

styled_label(frame, "Category:", 0)
combo_category = ttk.Combobox(frame, width=18, state="readonly", font=('Segoe UI', 12))
combo_category['values'] = ['Length', 'Weight', 'Temperature', 'Area', 'Volume', 'Time', 'Force', 'Power']
combo_category.grid(row=0, column=1, pady=8)
combo_category.bind("<<ComboboxSelected>>", update_units)

styled_label(frame, "From:", 1)
combo_from = ttk.Combobox(frame, width=18, state="readonly", font=('Segoe UI', 12))
combo_from.grid(row=1, column=1, pady=8)

styled_label(frame, "To:", 2)
combo_to = ttk.Combobox(frame, width=18, state="readonly", font=('Segoe UI', 12))
combo_to.grid(row=2, column=1, pady=8)

styled_label(frame, "Value:", 3)
entry_value = tk.Entry(frame, width=22, font=('Segoe UI', 14), bd=2)
entry_value.grid(row=3, column=1, pady=8)

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert, bg="#4CAF50", fg="white", font=('Segoe UI', 16, 'bold'))
convert_btn.pack(pady=20)

# Result Label
label_result = tk.Label(root, text="Result: ", font=('Segoe UI', 14), bg="#2e3f4f", fg="white")
label_result.pack()

root.mainloop()
