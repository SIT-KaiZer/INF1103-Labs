inventory = 0
status = True
failedAttempts = 0

while status:
    stock_quantity = input("Enter the inventory amount: ")

    if stock_quantity.lower() == "quit":
        break

    elif not stock_quantity.isdigit():
        failedAttempts += 1
        print("Invalid input. Please enter a valid number.")
        continue

    elif stock_quantity[0] == '-' and stock_quantity[1:].isdigit():
        failedAttempts += 1
        print("Inventory cannot be negative. Please enter a valid amount.")
        continue

    else:

        inventory += int(stock_quantity)
        if inventory > 500:
            failedAttempts += 1
            print("Inventory cannot exceed 500. Please enter a valid amount.")
            break
        
    
print("Total Units in Inventory:", inventory)
print("Failed Attempts:", failedAttempts)

    
    
