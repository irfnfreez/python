import tkinter as tk
import tkinter.messagebox as messagebox
import parcel_calculator

class calculator:
    def __init__(self, master):
        self.master = master
        master.title("Parcel Calculator")
        master.configure(bg='light blue')

        # Create length input label and entry field
        self.length_label = tk.Label(master, text="Length (cm):", bg='light blue')
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create width input label and entry field
        self.width_label = tk.Label(master, text="Width (cm):", bg='light blue')
        self.width_label.grid(row=1, column=0, padx=10, pady=10)
        self.width_entry = tk.Entry(master)
        self.width_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create height input label and entry field
        self.height_label = tk.Label(master, text="height (cm):", bg='light blue')
        self.height_label.grid(row=2, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create weight input label and entry field
        self.weight_label = tk.Label(master, text="Weight (kg):", bg='light blue')
        self.weight_label.grid(row=3, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create calculate button
        self.calculate_button = tk.Button(master, text="Calculate", command=lambda: self.calculate_price(), bg='light green')
        self.calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calculate_price(self):
        # Get parcel dimensions and weight from entry fields
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        # Calculate parcel price using imported function
        price = parcel_calculator.calculate_price(length, width, height, weight)

        # Display price in a message box
        messagebox.showinfo("Price", "The price of your parcel is: $" + str(price))

Parcel = tk.Tk()
gui = calculator(Parcel)
Parcel.mainloop()