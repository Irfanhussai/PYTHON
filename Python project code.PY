import tkinter as tk

class RestaurantBillManagement:
    def __init__(self):
        self.menu = {
            "Pizza": 10,
            "Burger": 5,
            "Pasta": 8,
            "Salad": 6,
            "Soft Drink": 2
        }

        self.order_items = {}
        self.total_amount = 0

        self.root = tk.Tk()
        self.root.title("Restaurant Bill Management System")
        
        self.create_gui()

    def create_gui(self):
        # Labels
        tk.Label(self.root, text="Menu").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Price").grid(row=0, column=2, padx=10, pady=5)
        
        # Menu items
        row = 1
        for item, price in self.menu.items():
            tk.Label(self.root, text=item).grid(row=row, column=0)
            quantity_entry = tk.Entry(self.root)
            quantity_entry.grid(row=row, column=1)
            price_label = tk.Label(self.root, text=f"${price}")
            price_label.grid(row=row, column=2)
            self.order_items[item] = {"quantity": quantity_entry, "price": price_label}
            row += 1

        # Calculate total button
        tk.Button(self.root, text="Calculate Total", command=self.calculate_total).grid(row=row, column=0, columnspan=3, pady=10)

        # Reset button
        tk.Button(self.root, text="Reset", command=self.reset_order).grid(row=row+1, column=0, pady=5)

        # Print button
        tk.Button(self.root, text="Print Bill", command=self.print_bill).grid(row=row+1, column=1, columnspan=2, pady=5)

        # Total amount label
        row += 2
        tk.Label(self.root, text="Total Amount: ").grid(row=row, column=0, padx=10, pady=5)
        self.total_amount_label = tk.Label(self.root, text="")
        self.total_amount_label.grid(row=row, column=1, columnspan=2, padx=10, pady=5)

    def calculate_total(self):
        self.total_amount = 0
        for item, data in self.order_items.items():
            quantity = data["quantity"].get()
            if quantity.isdigit():
                price = int(quantity) * self.menu[item]
                self.total_amount += price

        self.total_amount_label.config(text=f"${self.total_amount}")

    def reset_order(self):
        for data in self.order_items.values():
            data["quantity"].delete(0, tk.END)
        self.total_amount = 0
        self.total_amount_label.config(text="")

    def print_bill(self):
        bill_text = "Restaurant Bill\n"
        bill_text += "-----------------------------\n"
        for item, data in self.order_items.items():
            quantity = data["quantity"].get()
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    price = quantity * self.menu[item]
                    bill_text += f"{item} x {quantity} = ${price}\n"
        bill_text += "-----------------------------\n"
        bill_text += f"Total Amount: ${self.total_amount}\n"

        print(bill_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RestaurantBillManagement()
    app.run()
