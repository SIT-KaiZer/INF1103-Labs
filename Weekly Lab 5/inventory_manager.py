import os
import json


def display_all():
    with open("inventory.json", "r", encoding="utf-8") as file:
        try:
            inventory = json.load(file)
            if not inventory:
                print("No products in the inventory.")
                return
            print("\n\n-----Current Inventory-----")
            for product in inventory:
                print(f"Product ID: {product['ProductID']}, Name: {product['Name']}, Price: ${product['Price']:.2f}, Stock: {product['Stock']}")
            print("--------------------\n")
        except json.JSONDecodeError:
            print("Error decoding JSON from inventory.json. The file may be corrupted.")

def add_product():
    if len(inventory) == 0:
        print("Add a new product")
        latestProductID = inventory[-1]["ProductID"]
        latestProductID = latestProductID.replace('P', "")
        newProductID = int(latestProductID) + 1
        while True:
            newProductName = input("Product Name:")
            if newProductName is None:
                print("Invalid input. Please enter a valid product name.")
                continue
            elif not newProductName.replace(" ","").isalpha():
                print("Invalid input. Please enter a valid product name.")
                continue
            else:
                while True:
                    newPrice = input("Price:")
                    if newPrice is None:
                        print("Invalid input. Please enter a valid price.")
                        continue
                    elif not newPrice.replace(".","").isdigit():
                        print("Invalid input. Price must be a number. Please enter a valid price")
                        continue
                    else:
                        while True:
                            newStockQuantity = input("Stock:")
                            if newStockQuantity is None:
                                    print("Invalid input. Please enter a valid Stock.")
                                    continue
                            elif not newStockQuantity.isdigit():
                                print("Invalid input. Stock quantity must be a number. Please enter a valid stock quantity")
                                continue
                            else:
                                newProductID = str(newProductID).zfill(3)
                                newOrder = {"ProductID":"P"+newProductID,"Name":newProductName,"Price":newPrice,"Stock":newStockQuantity}
                                return newOrder
            
            
    elif not len(inventory) == 0:
        latestProductID = inventory[-1]["ProductID"]
        latestProductID = latestProductID.replace('P', "")
        newProductID = int(latestProductID) + 1
        while True:
                        newProductName = input("Product Name:")
                        if newProductName is None:
                            print("Invalid input. Please enter a valid product name.")
                            continue
                        elif not newProductName.replace(" ","").isalpha():
                            print("Invalid input. Please enter a valid product name.")
                            continue
                        else:
                            while True:
                                newPrice = input("Price:")
                                if newPrice is None:
                                    print("Invalid input. Please enter a valid price.")
                                    continue
                                elif not newPrice.replace(".","").isdigit():
                                    print("Invalid input. Price must be a number. Please enter a valid price")
                                    continue
                                else:
                                    while True:
                                        newStockQuantity = input("Stock:")
                                        if newStockQuantity is None:
                                             print("Invalid input. Please enter a valid Stock.")
                                             continue
                                        elif not newStockQuantity.isdigit():
                                            print("Invalid input. Stock quantity must be a number. Please enter a valid stock quantity")
                                            continue
                                        else:
                                            newProductID = str(newProductID).zfill(3)
                                            newOrder = {"ProductID":"P"+newProductID,"Name":newProductName,"Price":newPrice,"Stock":newStockQuantity}
                                            return newOrder


    

def update_stock():
    print("Update Stock")
    updatingID = input("Enter Product ID you wish to update:")
    for item in inventory:
        if item["Product ID"] == updatingID:
            print("Product Found")
            print("Name:" + item["Name"])
            print("Current Stock:" + item["Stock"])
            while True:
                newStockValue = input("Please enter new stock value:")
                if newStockValue is None:
                        print("Invalid input. Please enter a valid Stock.")
                        continue
                elif not newStockValue.isdigit():
                    print("Invalid input. Stock quantity must be a number. Please enter a valid stock quantity")
                    continue
                elif newStockValue == item["Stock"]:
                    print("Invalid Input. New stock value can't be the same as previous stock value")
                    continue
                else:
                    item["Stock"] = newStockValue
                    return
        else:
            print("Product not found, Returning to main menu")
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
                    print(inventory)
                    return(inventory)
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
            newOrder = add_product()
            inventory.append(newOrder)
            print("Here are the following new orders that have yet to be saved to the database:")
            print(inventory)
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
inventory = load_inventory()
main_menu()