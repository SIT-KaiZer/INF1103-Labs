def load_orders():
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        orders = file.read()
        print(f"Current orders:\n{orders}")
        print("================================\n")

def get_valid_input():
    while True:
        newOrder = input("Enter Product Name (or type 'quit' to exit): ")

        if newOrder.lower() == "quit":
            return "quit"
        
        elif newOrder is None:
            print("Invalid input. Please enter a valid product name.")
            continue

        elif newOrder.isdigit():
            print("Invalid input. Product name cannot be a number. Please enter a valid product name.")
            continue

        elif not newOrder.replace(" ", "").isalpha():
            print("Invalid input. Product name must contain only letters. Please enter a valid product name.")
            continue

        else:
            while True:
                newOrderQuantity = input("Enter the quantity for the product: ")

                if not newOrderQuantity.isdigit:
                    print("Invalid input. Quantity must be a number. Please enter a valid quantity.")
                    continue
                else:
                    return newOrder, int(newOrderQuantity)


def save_orders(newOrderItem, newOrderQuantity):
    print("save orders called")
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        orders = file.readlines()
        highestOrderNumber = 0
        for order in orders:
            order = [item.strip() for item in order.strip().split(",")]

            order_number = int(order[0])

            if order_number > highestOrderNumber:
                highestOrderNumber = order_number

        newOrderNumber = highestOrderNumber + 1
        newOrder = f"\n{newOrderNumber}, {newOrderItem}, {newOrderQuantity}"
        with open("inventory.txt", "a") as file:
            file.write(newOrder)
        print("Order saved successfully.")
        


def generate_report():
    with open("inventory.txt", "r") as file:
        orders = file.readlines()
        print(f"\nInventory Report")
        print("----------------")
        for order in orders:
            order = [item.strip() for item in order.strip().split(",")]
            order_number = order[0]
            product_name = order[1]
            quantity = order[2]
            print(f"Order Number: {order_number}, Product Name: {product_name}, Quantity: {quantity}")



load_orders()
while True:
    newOrderToAdd =get_valid_input()
    if newOrderToAdd == "quit":
        break
    else: 
        newOrderItem = newOrderToAdd[0]
        newOrderQuantity = newOrderToAdd[1]
        save_orders(newOrderItem, newOrderQuantity)
        continue
generate_report()
