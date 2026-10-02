import os
import json


def display_all():
    with open("inventory.json", "r", encoding="utf-8") as file:
        try:
            inventory = json.load(file)
            if not inventory:
                print("No products in the inventory.")
                return
            print("\n-----Current Inventory-----")
            for product in inventory:
                print(f"Product ID: {product['ProductID']}, Name: {product['Name']}, Price: ${product['Price']:.2f}, Stock: {product['Stock']}")
            print("--------------------")
        except json.JSONDecodeError:
            print("Error decoding JSON from inventory.json. The file may be corrupted.")

def add_product():
    return

def update_stock():
    return

def search_product():
    return

def save_inventory():
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



def main_menu():
    while True:
        print("\n-----MAIN MENU-----")
        print("1. Display All Stock")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


print("==========================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==========================")
load_inventory()
main_menu()