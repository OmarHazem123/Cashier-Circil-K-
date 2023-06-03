from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
from datetime import datetime


class CoffeeShopMaster:
    def __init__(self):
        self.root = Tk()
        self.root.title("Circle-K Cashier System")
        self.root.withdraw()  # Hide the main window

        # Variables
        self.orders = []
        self.total_price = 0

        # Simulate loading process
        self.simulate_loading()

        # Show the main window
        self.root.title("Circle-K Cashier System")
        self.root.geometry("800x600")
        self.root.configure(bg="#F3F3F3")  # Set background color to light gray

        # Load and display the logo image
        self.image = Image.open("circle-k-logo-black-and-white.png")
        self.image = self.image.resize((400, 150))  # Adjust the size as needed
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.root, image=self.photo, bg="#F3F3F3")
        self.image_label.pack(pady=20)

        # Create a scrollable frame
        self.scrollable_frame = Frame(self.root, bg="#F3F3F3")
        self.scrollable_frame.pack(fill="both", expand=True)

        # Create a canvas
        self.canvas = Canvas(self.scrollable_frame, bg="#F3F3F3")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = Scrollbar(self.scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create a frame inside the canvas to contain the content
        self.content_frame = Frame(self.canvas, bg="#F3F3F3")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Create the coffee type selection frame
        self.coffee_frame = Frame(self.content_frame, bg="#F3F3F3")
        self.coffee_frame.pack(pady=20)

        # Create the coffee type label
        self.coffee_label = Label(self.coffee_frame, text="Select Coffee Type:", font=("Arial", 14), bg="#F3F3F3")
        self.coffee_label.grid(row=0, column=0, padx=10, pady=5)

        # Create the coffee type options
        self.coffee_type = StringVar()
        self.coffee_type.set("Espresso")

        coffee_options = ["Espresso", "Cappuccino", "Latte", "Americano"]

        for i, option in enumerate(coffee_options):
            radio_button = Radiobutton(self.coffee_frame, text=option, variable=self.coffee_type, value=option,
                                       font=("Arial", 12), bg="#F3F3F3")
            radio_button.grid(row=i + 1, column=0, padx=10, pady=5)

        # Create the calculator frame
        self.calculator_frame = Frame(self.content_frame, bg="#F3F3F3")
        self.calculator_frame.pack(pady=20)

        # Create the calculator labels and entry fields
        self.quantity_label = Label(self.calculator_frame, text="Quantity:", font=("Arial", 14), bg="#F3F3F3")
        self.quantity_label.grid(row=0, column=0, padx=10, pady=5)

        self.quantity_entry = Entry(self.calculator_frame, width=10, font=("Arial", 14))
        self.quantity_entry.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = Label(self.calculator_frame, text="Price:", font=("Arial", 14), bg="#F3F3F3")
        self.price_label.grid(row=1, column=0, padx=10, pady=5)

        self.price_entry = Entry(self.calculator_frame, width=10, font=("Arial", 14), state="readonly")
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create the calculate price button
        self.calculate_button = Button(self.calculator_frame, text="Calculate", command=self.calculate_price,
                                       font=("Arial", 14))
        self.calculate_button.grid(row=0, column=2, padx=10, pady=5)

        # Create the add to order button
        self.add_button = Button(self.calculator_frame, text="Add to Order", command=self.add_to_order,
                                 font=("Arial", 14))
        self.add_button.grid(row=1, column=2, padx=10, pady=5)

        # Create the order list
        self.order_frame = Frame(self.content_frame, bg="#F3F3F3")
        self.order_frame.pack(pady=20)

        self.order_list = Listbox(self.order_frame, width=50, height=10, font=("Arial", 12))
        self.order_list.pack(side=LEFT, fill=Y)

        # Create the scrollbar for the order list
        self.order_scrollbar = Scrollbar(self.order_frame)
        self.order_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the order list to use the scrollbar
        self.order_list.configure(yscrollcommand=self.order_scrollbar.set)
        self.order_scrollbar.configure(command=self.order_list.yview)

        # Create the delete order button
        self.delete_button = Button(self.content_frame, text="Delete Order", command=self.delete_order,
                                    font=("Arial", 14))
        self.delete_button.pack(side=RIGHT, padx=10, pady=20)

        # Create the print receipt button
        self.print_button = Button(self.content_frame, text="Print Receipt", command=self.print_receipt,
                                   font=("Arial", 14))
        self.print_button.pack(side=RIGHT, padx=10, pady=20)

        # Create the total price label
        self.total_price_label = Label(self.content_frame, text="Total Price: $0", font=("Arial", 16), bg="#F3F3F3")
        self.total_price_label.pack()

        # Create the time and date label
        self.time_date_label = Label(self.content_frame, text="", font=("Arial", 12), bg="#F3F3F3")
        self.time_date_label.pack()

        # Update the time and date label
        self.update_time_date_label()

        # Run the main loop
        self.root.mainloop()

    def simulate_loading(self):
        loading_window = Toplevel(self.root)
        loading_window.title("Loading...")
        loading_window.geometry("400x300")

        # Set the loading screen image
        loading_image = Image.open("coffee.gif")
        loading_image = loading_image.resize((200, 200))
        loading_photo = ImageTk.PhotoImage(loading_image)

        loading_label = Label(loading_window, image=loading_photo, bg="#F3F3F3")
        loading_label.image = loading_photo
        loading_label.pack(pady=50)

        # Simulate a loading process
        for _ in range(3):
            loading_label.config(text="Loading.", font=("Arial", 16))
            loading_window.update()
            time.sleep(0.5)

            loading_label.config(text="Loading..", font=("Arial", 16))
            loading_window.update()
            time.sleep(0.5)

            loading_label.config(text="Loading...", font=("Arial", 16))
            loading_window.update()
            time.sleep(0.5)

        loading_window.destroy()
        self.root.deiconify()



    def calculate_price(self):
        coffee_type = self.coffee_type.get()
        quantity = int(self.quantity_entry.get())

        if coffee_type == "Espresso":
            price = 2.5
        elif coffee_type == "Cappuccino":
            price = 3.0
        elif coffee_type == "Latte":
            price = 3.5
        elif coffee_type == "Americano":
            price = 2.0
        else:
            price = 0

        total_price = price * quantity

        self.price_entry.config(state="normal")
        self.price_entry.delete(0, END)
        self.price_entry.insert(END, f"${total_price:.2f}")
        self.price_entry.config(state="readonly")

    def add_to_order(self):
        coffee_type = self.coffee_type.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get().replace('$', ''))  # Remove the dollar sign before converting to float

        self.orders.append({"Coffee Type": coffee_type, "Quantity": quantity, "Price": price})
        self.update_order_list()

        self.total_price += price
        self.total_price_label.config(text=f"Total Price: ${self.total_price:.2f}")

        messagebox.showinfo("Success", "Order added successfully!")

    def update_order_list(self):
        self.order_list.delete(0, END)
        for order in self.orders:
            coffee_type = order["Coffee Type"]
            quantity = order["Quantity"]
            price = order["Price"]
            self.order_list.insert(END, f"{coffee_type} - Quantity: {quantity} - Price: ${price:.2f}")

    def delete_order(self):
        selected_indices = self.order_list.curselection()
        if len(selected_indices) == 0:
            messagebox.showwarning("Error", "Please select an order to delete.")
        else:
            selected_index = selected_indices[0]
            order = self.orders[selected_index]
            price = order["Price"]
            self.orders.pop(selected_index)

            self.update_order_list()

            self.total_price -= price
            self.total_price_label.config(text=f"Total Price: ${self.total_price:.2f}")

            messagebox.showinfo("Success", "Order deleted successfully!")

    def print_receipt(self):
        # Get the current time and date
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        receipt_text = f"Coffee Shop Receipt\nDate: {current_date}\nTime: {current_time}\n\n"
        for order in self.orders:
            coffee_type = order["Coffee Type"]
            quantity = order["Quantity"]
            price = order["Price"]
            receipt_text += f"{coffee_type} - Quantity: {quantity} - Price: ${price:.2f}\n"

        receipt_text += f"\nTotal Price: ${self.total_price:.2f}"

        messagebox.showinfo("Receipt", receipt_text)

    def update_time_date_label(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        self.time_date_label.config(text=f"Time: {current_time}   Date: {current_date}")
        self.root.after(1000, self.update_time_date_label)


if __name__ == "__main__":
    coffee_shop_master = CoffeeShopMaster()


