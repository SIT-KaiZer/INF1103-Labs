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
            return
        elif choice == "3":
            return
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