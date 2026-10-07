import os
import json


def display_all():
    print("Current Inventory:")
    print("------------------------------------------------------")
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(f"ProductID: {item['ProductID']}, Name: {item['Name']}, Price: {item['Price']}, Stock: {item['Stock']}\n")
    print("------------------------------------------------------")

def add_product():
    global nothingToSave
    if len(inventory) == 0:
        print("Add a new product")
        newProductID = int(1)
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
                                newOrder = {"ProductID":"P"+newProductID,"Name":newProductName,"Price":float(newPrice),"Stock":int(newStockQuantity)}
                                nothingToSave = False
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
                                            newOrder = {"ProductID":"P"+newProductID,"Name":newProductName,"Price":float(newPrice),"Stock":int(newStockQuantity)}
                                            nothingToSave = False
                                            return newOrder


    

def update_stock():
    global nothingToSave
    print("Update Stock")
    updatingID = input("Enter Product ID you wish to update:")
    found = False

    for item in inventory:
        if item["ProductID"] == updatingID:
            print("Product Found")
            found = True
            print("Name:" + item["Name"])
            print("Current Stock:" + str(item["Stock"]))
            while True:
                newStockValue = input("Please enter new stock value:")
                
                if newStockValue is None:
                        print("Invalid input. Please enter a valid Stock.")
                        continue
                elif not newStockValue.isdigit():
                    print("Invalid input. Stock quantity must be a number. Please enter a valid stock quantity")
                    continue
                
                elif newStockValue == str(item["Stock"]):
                    print("Invalid Input. New stock value can't be the same as previous stock value")
                    continue
                else:
                    item["Stock"] = int(newStockValue)
                    nothingToSave = False
                    print("Stock updated successfully!")
                    return
    if found == False:
        print("Product not found")
        print("Returning to Main Menu")
        return
        

def search_product():
    print("Search for product")
    searchingID = input("ProductID:")
    found = False
    for item in inventory:
        if item["ProductID"] == searchingID:
            print("Product Found")
            found = True
            print("ID:" + item["ProductID"])
            print("Name:" + item["Name"])
            print("Price:" + str(item["Price"]))
            print("Current Stock:" + str(item["Stock"]))
            
    if found == False:
        print("Product not found")
        print("Returning to Main Menu")
        return

def save_inventory():
    global nothingToSave
    with open("inventory.json", "w") as file:
        file.write("[\n")

        for i, item in enumerate(inventory):
            file.write(json.dumps(item))

            if i < len(inventory) - 1:
                file.write(",")

            file.write("\n")

        file.write("]")
        print("Inventory has been saved!")
        nothingToSave = True



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
            for item in inventory:
                print(f"ProductID: {item['ProductID']}, Name: {item['Name']}, Price: {item['Price']}, Stock: {item['Stock']}\n")
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            if nothingToSave == False:
                print("Saving inventory before exit...")
                save_inventory()
                break
            else:
                print("Exiting the program.")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


print("==========================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==========================")
inventory = load_inventory()
nothingToSave = True
main_menu()