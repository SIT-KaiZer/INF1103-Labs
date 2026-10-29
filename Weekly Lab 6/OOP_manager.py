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
                    Product.display_information()
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
                Product.display_information(product)

        print("-" * 60)



def load_inventory():
    return


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
            return
        elif choice == "2":
            product_id = input("Enter Product ID to search: ").strip()
            inventory.search_product(product_id)
        elif choice == "3":
            inventory.display_all()
        elif choice == "4":
            return
        elif choice == "5":
            return
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


print("==========================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==========================")
inventory = load_inventory()
main_menu(inventory)