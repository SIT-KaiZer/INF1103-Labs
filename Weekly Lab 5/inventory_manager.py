import os
import json


def add_product():
    return

def update_stock():
    return

def search_product():
    return

def display_all():
    return

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
                else:
                    print("Inventory.json found")
                    print("Inventory loaded successfully.")
            except json.JSONDecodeError:
                print("Error decoding JSON from inventory.json. The file may be corrupted.")

            
    return

def save_inventory():
    return

def main_menu():
    return


