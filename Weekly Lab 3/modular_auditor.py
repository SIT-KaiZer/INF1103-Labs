inventory = 0
failedAttempts = 0
deliveriesProcessed = 0

# while status:
#     stock_quantity = input("Enter the inventory amount: ")

#     if stock_quantity.lower() == "quit":
#         break

#     elif not stock_quantity.isdigit():
#         failedAttempts += 1
#         print("Invalid input. Please enter a valid number.")
#         continue

#     elif stock_quantity[0] == '-' and stock_quantity[1:].isdigit():
#         failedAttempts += 1
#         print("Inventory cannot be negative. Please enter a valid amount.")
#         continue

#     else:
        # inventory += int(stock_quantity)
        # if inventory > 500:
        #     failedAttempts += 1
        #     print("Inventory cannot exceed 500. Please enter a valid amount.")
        #     break
        
def get_valid_input():
    newFailedAttempts = 0
    while True:
        stockQuantity = input("Enter the inventory amount to deliver: ")

        if stockQuantity.lower() == "quit":
            return "quit", newFailedAttempts

        elif stockQuantity[0] == '-' and stockQuantity[1:].isdigit():
                    print("Inventory cannot be negative. Please enter a valid amount.")
                    newFailedAttempts += 1
                    continue

        elif not stockQuantity.isdigit():
            print("Invalid input. No words please. Please enter a valid number.")
            newFailedAttempts += 1
            continue

        else:
            return int(stockQuantity), newFailedAttempts
        
def process_delivery(current_total, new_quantity):
    current_total += new_quantity
    return current_total, True

    
while True: 
    stockQuantity, newFailedAttempts = get_valid_input()
    failedAttempts += newFailedAttempts
    if stockQuantity == "quit":
        break

    elif stockQuantity is not None:
        inventory, success = process_delivery(inventory, stockQuantity)
        print(inventory)
        if success:
            deliveriesProcessed += 1

print("test")
