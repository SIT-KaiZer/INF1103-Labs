import os
import json
class Product:

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = str(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__stock = int(stock)

    def update_stock(self, quantity: int):
            """Set the product's stock to a new non-negative quantity."""
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("Stock quantity must be a non-negative integer.")
            self.__stock = quantity

    def display_information(self):
        print(
            f"ProductID: {self.__product_id}, "
            f"Name: {self.__name}, "
            f"Price: {self.__price:.2f}, "
            f"Stock: {self.__stock}"
        )

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to inventory.")

        if self.search_product(product.product_id, show_message=False) is not None:
            print("A product with this ID already exists.")
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str, show_message=True):
        """Return the matching Product, or None if it cannot be found."""
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.product_id.upper() == product_id:
                if show_message:
                    print("Product found:")
                    product.display_information()
                return product

        if show_message:
            print("Product not found.")
            print("Returning to Main Menu.")
        return None

    def display_all(self):
        print("\nCurrent Inventory:")
        print("-" * 60)

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()

        print("-" * 60)

    def get_all_products(self):
        return self.__products

def add_product(inventory):
    print("\nAdd a new product")
    product_id = generate_product_id(inventory)
    name = get_valid_name()
    price = get_valid_price()
    stock = get_valid_stock()

    product = Product(product_id, name, price, stock)

    if inventory.add_product(product):
        print(f"Product {product_id} added successfully.")
        product.display_information()

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
            unsaved_changes = True
            add_product(inventory)
        elif choice == "2":
            product_id = input("Enter Product ID to search: ").strip()
            inventory.search_product(product_id)
        elif choice == "3":
            inventory.display_all()
        elif choice == "4":
            unsaved_changes = True
            return
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