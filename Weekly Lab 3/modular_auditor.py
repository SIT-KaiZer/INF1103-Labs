inventory = 0
totalFailedAttempts = 0
deliveriesProcessed = 0
tax = 0

        
def get_valid_input():
    newFailedAttempts = 0
    while True:
        stockQuantity = input("Enter the inventory amount to deliver: ")

        if stockQuantity.lower() == "quit":
            return "quit", newFailedAttempts

        elif stockQuantity is None or stockQuantity.strip() == "":
            print("Invalid input. Please enter a valid number.")
            newFailedAttempts += 1
            continue

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
    return current_total

def calculate_tax(amount):
    tax_rate = 0.10 
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    print("Inventory Report")
    print("----------------")
    print(f"Total Units Delivered: {total_units}")
    print(f"Total Failed Attempts: {failed_attempts}")

while True: 
    stockQuantity, newFailedAttempts = get_valid_input()
    totalFailedAttempts += newFailedAttempts
    if stockQuantity == "quit":
        break

    elif stockQuantity is not None:
        inventory = process_delivery(inventory, stockQuantity)
        tax = calculate_tax(stockQuantity)
        print(f"Tax for this delivery: {tax:.2f}")
        deliveriesProcessed += 1


generate_report(inventory, totalFailedAttempts)
