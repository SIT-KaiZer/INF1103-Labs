import os
import json

from inventory import Inventory
from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct

def add_product(inventory):
    print("\nAdd a new product")
    product_id = generate_product_id(inventory)
    name = get_valid_name()
    price = get_valid_price()
    stock = get_valid_stock()
    productType = get_valid_product_type()
    if productType == "physical":
        weight = get_valid_weight()
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif productType == "digital":
        download_size = get_valid_download_size()
        product = DigitalProduct(product_id, name, price, stock, download_size)

    if inventory.add_product(product):
        print(f"Product {product_id} added successfully.")
        product.display_information()
        product.get_fulfilment_info()
        if isinstance(product, PhysicalProduct):
            shipping_cost = product.calculate_shipping_cost()
            print(f"Shipping Cost: ${shipping_cost:.2f}")



def generate_product_id(inventory):
    highest_number = 0
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

def load_inventory():
    """Load inventory from a JSON file."""
    inventory = Inventory()

    if not os.path.exists("inventory.json"):
        print("inventory.json file does not exist. Creating a new file.")
        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump([], file)
            return inventory

    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            data = json.load(file)
            for item in data:
                product = Product(
                    item["ProductID"],
                    item["Name"],
                    item["Price"],
                    item["Stock"],
                )
                inventory.add_product(product)
    return inventory

def save_inventory(inventory):
    """Save Product objects to inventory.json as a JSON list."""
    try:
        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump(inventory.to_list(), file, indent=4)
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
            new_stock = get_valid_stock("Please enter new stock value: ")
        
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