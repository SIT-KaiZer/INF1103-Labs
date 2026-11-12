import os
import json

from inventory import Inventory
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from supplier import Suppliers

suppliers = []  # List to store Supplier objects

def add_product(inventory):
    print("\nAdd a new product")
    product_id = generate_product_id(inventory)
    name = get_valid_name()
    price = get_valid_price()
    stock = get_valid_stock()
    productType = get_valid_product_type()
    supplier = get_valid_supplier_info()
    if productType == "physical":
        weight = get_valid_weight()
        product = PhysicalProduct(product_id, name, price, stock, productType, supplier, weight)
    elif productType == "digital":
        download_size = get_valid_download_size()
        product = DigitalProduct(product_id, name, price, stock, productType, supplier, download_size)

    if inventory.add_product(product):
        print(f"Product {product_id} added successfully.")
        product.display_information()
        print(product.get_fulfilment_info())
        product.display_supplier_information()
        if isinstance(product, PhysicalProduct):
            shipping_cost = product.calculate_shipping_cost()
            print(f"Shipping Cost: ${shipping_cost:.2f}")



def generate_product_id(inventory):
    highest_number = 0
    productID = "P" + str(highest_number + 1).zfill(3)
    for product in inventory.get_all_products():
        product_id = product.product_id
        if product_id.startswith("P") and product_id[1:].isdigit():
            highest_number = max(highest_number, int(product_id[1:]))
        productID = "P" + str(highest_number + 1).zfill(3)
    return productID

def get_valid_name():
    while True:
        newProductName = input("Product Name:")
        if newProductName is None:
            print("Invalid input. Please enter a valid product name.")
            continue
        elif not newProductName.replace(" ","").isalpha():
            print("Invalid input. Please enter a valid product name.")
            continue
        else:
            return newProductName

def get_valid_price():
    while True:
        newPrice = input("Price:")
        if newPrice is None:
            print("Invalid input. Please enter a valid price.")
            continue
        elif not newPrice.replace(".","").isdigit():
            print("Invalid input. Price must be a number. Please enter a valid price")
            continue
        else:
            return float(newPrice)

def get_valid_stock():
    while True:
        newStockQuantity = input("Stock:")
        if newStockQuantity is None:
                print("Invalid input. Please enter a valid Stock.")
                continue
        elif not newStockQuantity.isdigit():
            print("Invalid input. Stock quantity must be a number. Please enter a valid stock quantity")
            continue
        else:
            return int(newStockQuantity)

def get_valid_product_type():
    while True:
        productType = input("Product Type (Physical/Digital):").strip().lower()
        if productType not in ["physical", "digital"]:
            print("Invalid input. Please enter 'Physical' or 'Digital'.")
            continue
        else:
            return productType

def get_valid_weight():
    while True:
        weight = input("Weight (in kg):")
        if weight is None:
            print("Invalid input. Please enter a valid weight.")
            continue
        elif not weight.replace(".","").isdigit():
            print("Invalid input. Weight must be a number. Please enter a valid weight.")
            continue
        else:
            return float(weight)

def get_valid_download_size():
    while True:
        download_size = input("Download Size (in MB):")
        if download_size is None:
            print("Invalid input. Please enter a valid download size.")
            continue
        elif not download_size.replace(".","").isdigit():
            print("Invalid input. Download size must be a number. Please enter a valid download size.")
            continue
        else:
            return float(download_size)
def generate_supplier_id():
    highest_number = 0
    supplierID = "S" + str(highest_number + 1).zfill(3)
    for supplier in suppliers:
        supplier_id = supplier.supplier_id
        if supplier_id.startswith("S") and supplier_id[1:].isdigit():
            highest_number = max(highest_number, int(supplier_id[1:]))
        supplierID = "S" + str(highest_number + 1).zfill(3)
    return supplierID

def get_valid_supplier_info():
    while True:
        supplier_id = generate_supplier_id()
        name = input("Supplier Name:").strip()
        if not name:
            print("Invalid input. Please enter a valid Supplier Name.")
            continue

        contact_email = input("Supplier Contact Email:").strip()
        if not contact_email or "@" not in contact_email:
            print("Invalid input. Please enter a valid email address.")
            continue

        return Suppliers(supplier_id, name, contact_email)


def load_inventory():
    """Load inventory and suppliers from a JSON file."""

    inventory = Inventory()

    # Check if the JSON file exists
    if not os.path.exists("inventory.json"):
        print("inventory.json file does not exist. Creating a new file.")

        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump({"Products": [], "Suppliers": []}, file, indent=4)

        return inventory

    # Load JSON data
    with open("inventory.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # 1. Load suppliers first
    suppliers.clear()
    supplier_dict = {}

    for item in data["Suppliers"]:
        supplier = Suppliers(
            item["SupplierID"],
            item["Name"],
            item["ContactEmail"]
        )

        suppliers.append(supplier)

        # Store supplier using SupplierID as the key
        supplier_dict[supplier.supplier_id] = supplier

    # 2. Load products
    for item in data["Products"]:

        # Find the supplier associated with this product
        supplier = supplier_dict.get(item["SupplierID"])

        if supplier is None:
            print(f"Supplier not found for product {item['ProductID']}. Skipping product.")
            continue

        if item["ProductType"] == "physical":
            product = PhysicalProduct(
                item["ProductID"],
                item["Name"],
                item["Price"],
                item["Stock"],
                item["ProductType"],
                supplier,
                item["Weight"]
            )

        elif item["ProductType"] == "digital":
            product = DigitalProduct(
                item["ProductID"],
                item["Name"],
                item["Price"],
                item["Stock"],
                item["ProductType"],
                supplier,
                item["DownloadSize"]
            )

        else:
            print(f"Unknown product type for {item['ProductID']}. Skipping product.")
            continue

        inventory.add_product(product)

    return inventory


def save_inventory(inventory):
    """Save Product objects to inventory.json as a JSON list."""
    supplier_list = [
        supplier.to_dict() for supplier in suppliers
    ]
    try:
        data = {
        "Products": inventory.to_list(),
        "Suppliers": supplier_list
        }
        
        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Inventory has been saved!")
        return True
    except OSError as error:
        print(f"Could not save inventory.json: {error}")
        return False


def main_menu(inventory):
    unsaved_changes = False

    while True:
        print("\nMain Menu:")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Display All Products")
        print("4. Update Stock")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_product(inventory)
            unsaved_changes = True
        elif choice == "2":
            product_id = input("Enter Product ID to search: ").strip()
            inventory.search_product(product_id)
        elif choice == "3":
            inventory.display_all()
        elif choice == "4":
            product_id = input("Enter Product ID you wish to update: ").strip()
            product = inventory.search_product(product_id, show_message=False)

            if product is None:
                print("Product not found.")
                print("Returning to Main Menu.")
                continue

            print(f"Name: {product.name}")
            print(f"Current Stock: {product.stock}")
            new_stock = get_valid_stock()
        
            if inventory.update_stock(product_id, new_stock):
                unsaved_changes = True
        elif choice == "5":
            if save_inventory(inventory):
                unsaved_changes = False
        elif choice == "6":
            if unsaved_changes:
                    print("saving changes before exiting....")
                    if save_inventory(inventory):
                        print("Inventory saved successfully.")
                    else:
                        print("Failed to save inventory.")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


print("==========================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==========================")
inventory = load_inventory()
main_menu(inventory)