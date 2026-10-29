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



def load_inventory():
     if not os.path.exists("inventory.json"):
         print("inventory.json file does not exist. Creating a new file.")
         with open("inventory.json", "w", encoding="utf-8") as file:
             json.dump([], file)
         return
     else:
         with open("inventory.json", "r", encoding="utf-8") as file:
             try:
                 inventory = json.load(file)
                 if not inventory:
                     print("inventory.json is empty. No products to load.")
                     return(inventory)
                 else:
                     print("Inventory.json found")
                     print("Inventory loaded successfully.")
                     return(inventory)
             except json.JSONDecodeError:
                 print("Error decoding JSON from inventory.json. The file may be corrupted.")
                 inventory = []
                 return(inventory)
