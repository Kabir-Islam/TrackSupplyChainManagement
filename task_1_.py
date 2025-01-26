"""task 1  .ipynb

Original file is located at
    https://colab.research.google.com/drive/1hETjKKiecqGy_jD34l4XXbNfrE7Z_epl
"""

# Task.....1 (Kabirul_Islam_Supplier_and_Shipment_Management_System)

# Import necessary libraries
import pandas as pd
import sqlite3
from datetime import datetime

# --- Introduction ---
# This program is designed to manage suppliers and shipments by storing data in an SQLite database.
# It provides functionalities to:
# - Manage supplier information (add, update, and query suppliers)
# - Track shipments (record and update shipments)
# - Analyze supply chain data (generate reports and summaries)

# --- Load the CSV File ---
file_name = "SPM.csv"  # Input data file containing supplier and shipment details
data = pd.read_csv(file_name)  # Read the CSV file into a pandas DataFrame

# --- Connect to SQLite Database ---
conn = sqlite3.connect('supplier_shipment_management.db')  # Create or connect to the SQLite database
cursor = conn.cursor()

# --- Create Tables ---
# Define the Suppliers table to store supplier information
cursor.execute('''
CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID TEXT PRIMARY KEY,
    SupplierName TEXT NOT NULL,
    ContactPerson TEXT,
    ContactNumber TEXT,
    Address TEXT
)
''')

# Define the Shipments table to store shipment information
cursor.execute('''
CREATE TABLE IF NOT EXISTS Shipments (
    ShipmentID TEXT PRIMARY KEY,
    SupplierID TEXT,
    ItemID TEXT,
    ItemName TEXT,
    Quantity INTEGER,
    ShipmentDate DATE,
    DeliveryDate DATE,
    ShipmentStatus TEXT,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
)
''')

# --- Populate Tables from CSV ---
# Loop through the DataFrame and insert data into the Suppliers and Shipments tables
for _, row in data.iterrows():
    cursor.execute('''
    INSERT OR IGNORE INTO Suppliers (SupplierID, SupplierName, ContactPerson, ContactNumber, Address)
    VALUES (?, ?, ?, ?, ?)
    ''', (row['Supplier ID'], row['Supplier Name'], row['Contact Person'], row['Contact Number'], row['Address']))

    cursor.execute('''
    INSERT OR IGNORE INTO Shipments (ShipmentID, SupplierID, ItemID, ItemName, Quantity, ShipmentDate, DeliveryDate, ShipmentStatus)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row['Shipment ID'], row['Supplier ID'], row['Item ID'], row['Item Name'], row['Quantity'], row['Shipment Date'], row['Delivery Date'], row['Shipment Status']))

conn.commit()  # Save changes to the database

# --- Task 1: Supplier Management ---
def supplier_management():
    """Manage supplier-related operations, such as adding, updating, or listing suppliers."""
    while True:
        print("\nSupplier Management:")
        print("1. Add New Supplier")
        print("2. Update Supplier Details")
        print("3. List Suppliers Providing Specific Items")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new supplier to the database
            supplier_id = input("Supplier ID: ")
            supplier_name = input("Supplier Name: ")
            contact_person = input("Contact Person: ")
            contact_number = input("Contact Number: ")
            address = input("Address: ")
            cursor.execute('''
            INSERT OR IGNORE INTO Suppliers (SupplierID, SupplierName, ContactPerson, ContactNumber, Address)
            VALUES (?, ?, ?, ?, ?)
            ''', (supplier_id, supplier_name, contact_person, contact_number, address))
            conn.commit()
            print("Supplier added successfully.")
        elif choice == '2':
            # Update details of an existing supplier
            supplier_id = input("Supplier ID: ")
            field = input("Field to update (SupplierName, ContactPerson, ContactNumber, Address): ")
            new_value = input("New Value: ")
            cursor.execute(f'''
            UPDATE Suppliers SET {field} = ? WHERE SupplierID = ?
            ''', (new_value, supplier_id))
            conn.commit()
            print("Supplier updated successfully.")
        elif choice == '3':
            # List suppliers providing a specific item
            item_id = input("Item ID: ")
            cursor.execute('''
            SELECT DISTINCT Suppliers.SupplierName
            FROM Suppliers
            JOIN Shipments ON Suppliers.SupplierID = Shipments.SupplierID
            WHERE Shipments.ItemID = ?
            ''', (item_id,))
            suppliers = cursor.fetchall()
            print("Suppliers providing the specified item:")
            for supplier in suppliers:
                print(supplier[0])
        elif choice == '4':
            # Return to the main menu
            break
        else:
            print("Invalid choice. Please try again.")

# --- Task 2: Shipment Tracking ---
def shipment_tracking():
    """Track and manage shipment-related operations, such as adding or updating shipments."""
    while True:
        print("\nShipment Tracking:")
        print("1. Record New Shipment")
        print("2. Update Shipment Status")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new shipment to the database
            shipment_id = input("Shipment ID: ")
            supplier_id = input("Supplier ID: ")
            item_id = input("Item ID: ")
            item_name = input("Item Name: ")
            quantity = int(input("Quantity: "))
            shipment_date = input("Shipment Date (YYYY-MM-DD): ")
            delivery_date = input("Delivery Date (YYYY-MM-DD): ")
            status = input("Shipment Status (In Transit/Delivered): ")
            cursor.execute('''
            INSERT OR IGNORE INTO Shipments (ShipmentID, SupplierID, ItemID, ItemName, Quantity, ShipmentDate, DeliveryDate, ShipmentStatus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (shipment_id, supplier_id, item_id, item_name, quantity, shipment_date, delivery_date, status))
            conn.commit()
            print("Shipment recorded successfully.")
        elif choice == '2':
            # Update the status of an existing shipment
            shipment_id = input("Shipment ID: ")
            new_status = input("New Status: ")
            cursor.execute('''
            UPDATE Shipments SET ShipmentStatus = ? WHERE ShipmentID = ?
            ''', (new_status, shipment_id))
            conn.commit()
            print("Shipment status updated successfully.")
        elif choice == '3':
            # Return to the main menu
            break
        else:
            print("Invalid choice. Please try again.")

# --- Task 3: Analyze Supply Chain Data ---
def analyze_supply_chain_data():
    """Perform analysis tasks on the supply chain data, such as generating reports and summaries."""
    while True:
        print("\nAnalyze Supply Chain Data:")
        print("1. Report Delayed Shipments")
        print("2. Summarize Shipments by Supplier")
        print("3. Identify Top Suppliers")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Generate a report of delayed shipments
            today = datetime.now().date()
            cursor.execute('''
            SELECT ShipmentID, DeliveryDate FROM Shipments
            WHERE DeliveryDate < ? AND ShipmentStatus != 'Delivered'
            ''', (today,))
            delayed = cursor.fetchall()
            print("Delayed Shipments:")
            for shipment in delayed:
                print(f"Shipment ID: {shipment[0]}, Delivery Date: {shipment[1]}")
        elif choice == '2':
            # Summarize shipments by supplier
            cursor.execute('''
            SELECT Suppliers.SupplierName, COUNT(Shipments.ShipmentID) as TotalShipments
            FROM Suppliers
            JOIN Shipments ON Suppliers.SupplierID = Shipments.SupplierID
            GROUP BY Suppliers.SupplierName
            ''')
            summary = cursor.fetchall()
            print("Shipments by Supplier:")
            for supplier in summary:
                print(f"Supplier: {supplier[0]}, Total Shipments: {supplier[1]}")
        elif choice == '3':
            # Identify top suppliers based on total items supplied
            cursor.execute('''
            SELECT Suppliers.SupplierName, SUM(Shipments.Quantity) as TotalItems
            FROM Suppliers
            JOIN Shipments ON Suppliers.SupplierID = Shipments.SupplierID
            GROUP BY Suppliers.SupplierName
            ORDER BY TotalItems DESC
            ''')
            top_suppliers = cursor.fetchall()
            print("Top Suppliers:")
            for supplier in top_suppliers:
                print(f"Supplier: {supplier[0]}, Total Items Supplied: {supplier[1]}")
        elif choice == '4':
            # Return to the main menu
            break
        else:
            print("Invalid choice. Please try again.")

# --- Main Menu ---
def main():
    """Main menu to navigate between different tasks of the program."""
    while True:
        print("\nMain Menu:")
        print("1. Supplier Management")
        print("2. Shipment Tracking")
        print("3. Analyze Supply Chain Data")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            supplier_management()
        elif choice == '2':
            shipment_tracking()
        elif choice == '3':
            analyze_supply_chain_data()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
