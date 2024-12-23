import tkinter as tk
from tkinter import ttk, messagebox
import heapq

# Backend classes
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.shipment_history = None

class ShipmentNode:
    def __init__(self, shipment_id, date, status, delivery_time):
        self.shipment_id = shipment_id
        self.date = date
        self.status = status
        self.delivery_time = delivery_time
        self.next = None

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer_id, name):
        if any(c.customer_id == customer_id for c in self.customers):
            return False
        self.customers.append(Customer(customer_id, name))
        return True

    def add_shipment(self, customer_id, shipment_id, date, status, delivery_time):
        customer = next((c for c in self.customers if c.customer_id == customer_id), None)
        if not customer:
            return False

        new_shipment = ShipmentNode(shipment_id, date, status, delivery_time)
        if not customer.shipment_history:
            customer.shipment_history = new_shipment
        else:
            current = customer.shipment_history
            prev = None
            while current and current.date < date:
                prev = current
                current = current.next

            if prev is None:
                new_shipment.next = customer.shipment_history
                customer.shipment_history = new_shipment
            else:
                prev.next = new_shipment
                new_shipment.next = current

        return True

    def get_shipment_history(self, customer_id):
        customer = next((c for c in self.customers if c.customer_id == customer_id), None)
        if not customer:
            return None

        history = []
        current = customer.shipment_history
        while current:
            history.append((current.shipment_id, current.date, current.status, current.delivery_time))
            current = current.next

        return history

    def get_customers(self):
        return [(c.customer_id, c.name) for c in self.customers]

# Priority Queue for shipments
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, shipment_id, priority):
        heapq.heappush(self.heap, (priority, shipment_id))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def get_all(self):
        return sorted(self.heap)

priority_queue = PriorityQueue()

# Initialize Customer Manager
customer_manager = CustomerManager()

# Mock data for shipment locations
class ShipmentLocations:
    def __init__(self):
        self.locations = {
            "CityA": {"CityB": 2, "CityC": 4, "CityD": 1},
            "CityB": {"CityA": 2, "CityC": 3, "CityE": 5},
            "CityC": {"CityA": 4, "CityB": 3, "CityF": 6},
            "CityD": {"CityA": 1, "CityE": 2},
            "CityE": {"CityB": 5, "CityD": 2, "CityF": 3},
            "CityF": {"CityC": 6, "CityE": 3}
        }

    def get_delivery_time(self, start, destination):
        return self.locations.get(start, {}).get(destination, "Unknown")

shipment_locations = ShipmentLocations()

# GUI Setup
def main_gui():
    root = tk.Tk()
    root.title("Logistics Management System")
    root.geometry("1920x1080")

    tab_control = ttk.Notebook(root)

    # Customer Management Tab
    customer_tab = ttk.Frame(tab_control)
    tab_control.add(customer_tab, text="Customer Management")

    tk.Label(customer_tab, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(customer_tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)

    customer_id_entry = tk.Entry(customer_tab)
    customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_entry = tk.Entry(customer_tab)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    def add_customer():
        customer_id = customer_id_entry.get()
        name = name_entry.get()

        if not customer_id or not name:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not customer_id.isdigit():
            messagebox.showerror("Error", "Customer ID must be a number.")
            return

        if customer_manager.add_customer(int(customer_id), name):
            messagebox.showinfo("Success", "Customer added successfully.")
            update_customer_list()
        else:
            messagebox.showerror("Error", "Customer ID already exists.")

    def update_customer_list():
        for row in customer_tree.get_children():
            customer_tree.delete(row)

        for customer in customer_manager.get_customers():
            customer_tree.insert("", "end", values=customer)

    add_button = tk.Button(customer_tab, text="Add Customer", command=add_customer)
    add_button.grid(row=2, column=0, columnspan=2, pady=10)

    customer_tree = ttk.Treeview(customer_tab, columns=("Customer ID", "Name"), show="headings")
    customer_tree.heading("Customer ID", text="Customer ID")
    customer_tree.heading("Name", text="Name")
    customer_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    update_customer_list()

    def view_shipment_history():
        customer_id = shipment_customer_id_entry.get()
        if not customer_id.isdigit():
            messagebox.showerror("Error", "Customer ID must be a number.")
            return

        shipment_history = customer_manager.get_shipment_history(int(customer_id))
        if not shipment_history:
            messagebox.showinfo("Info", f"No shipment history found for customer ID: {customer_id}. Make sure to add shipments first.")
            return

        shipment_tree.delete(*shipment_tree.get_children())  # Clear previous entries

        for shipment in shipment_history:
            shipment_tree.insert("", "end", values=shipment)
        messagebox.showinfo("Success", f"Shipment history for Customer ID {customer_id} loaded.")


    def add_shipment():
        customer_id = shipment_customer_id_entry.get()
        shipment_id = shipment_id_entry.get()
        date = date_entry.get()
        status = status_entry.get()
        location = shipment_location_combo.get()
        destination = shipment_destination_combo.get()

        if not all([customer_id, shipment_id, date, status, location, destination]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if not customer_id.isdigit() or not shipment_id.isdigit():
            messagebox.showerror("Error", "Customer ID and Shipment ID must be numbers.")
            return

        delivery_time = shipment_locations.get_delivery_time(location, destination)
        if delivery_time == "Unknown":
            messagebox.showerror("Error", "Invalid location or destination.")
            return

        if customer_manager.add_shipment(int(customer_id), int(shipment_id), date, status, delivery_time):
            messagebox.showinfo("Success", "Shipment added successfully.")
            view_shipment_history()
        else:
            messagebox.showerror("Error", "Failed to add shipment. Ensure the customer ID exists.")
    


    # Shipment History Tab
    shipment_tab = ttk.Frame(tab_control)
    tab_control.add(shipment_tab, text="Shipment History")

    tk.Label(shipment_tab, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(shipment_tab, text="Shipment ID:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(shipment_tab, text="Date:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(shipment_tab, text="Status:").grid(row=3, column=0, padx=5, pady=5)

    shipment_customer_id_entry = tk.Entry(shipment_tab)
    shipment_customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

    shipment_id_entry = tk.Entry(shipment_tab)
    shipment_id_entry.grid(row=1, column=1, padx=5, pady=5)

    date_entry = tk.Entry(shipment_tab)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    status_entry = tk.Entry(shipment_tab)
    status_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(shipment_tab, text="Shipment Location:").grid(row=4, column=0, padx=5, pady=5)
    shipment_location_combo = ttk.Combobox(shipment_tab, values=list(shipment_locations.locations.keys()))
    shipment_location_combo.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(shipment_tab, text="Destination:").grid(row=5, column=0, padx=5, pady=5)
    shipment_destination_combo = ttk.Combobox(shipment_tab, values=list(shipment_locations.locations.keys()))
    shipment_destination_combo.grid(row=5, column=1, padx=5, pady=5)

    add_shipment_button = tk.Button(shipment_tab, text="Add Shipment", command=add_shipment)
    add_shipment_button.grid(row=6, column=0, columnspan=2, pady=10)
    view_history_button = tk.Button(shipment_tab, text="View Shipment History", command=view_shipment_history)
    view_history_button.grid(row=6, column=1, columnspan=2, pady=5)
    

    shipment_tree = ttk.Treeview(shipment_tab, columns=("Shipment ID", "Date", "Status", "Delivery Time"), show="headings")
    shipment_tree.heading("Shipment ID", text="Shipment ID")
    shipment_tree.heading("Date", text="Date")
    shipment_tree.heading("Status", text="Status")
    shipment_tree.heading("Delivery Time", text="Delivery Time")
    shipment_tree.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    tab_control.pack(expand=1, fill="both")
    root.mainloop()




if __name__ == "__main__":
    main_gui()