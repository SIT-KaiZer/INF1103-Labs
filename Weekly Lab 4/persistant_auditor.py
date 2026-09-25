def get_valid_input():
    print("get valid input called")
    while True:
        newOrder = input("Enter Product Name (or type 'quit' to exit): ")

        if newOrder.lower() == "quit":
            return "quit"
        
        elif newOrder is None or newOrder.strip() == "":
            print("Invalid input. Please enter a valid product name.")
            continue

        elif newOrder.isdigit():
            print("Invalid input. Product name cannot be a number. Please enter a valid product name.")
            continue

        elif not newOrder.strip() == "".isalpha():
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

        


def load_orders():
    print("load orders called")
    with open(".\Weekly Lab 4\inventory.txt", "r") as file:
        orders = file.read()
        print(f"Current orders:\n{orders}")
    
def save_orders():
    print("save orders called")

def generate_report():
    print("generate report called")

while True:
    load_orders()
    get_valid_input()
    
    print("test")
    break
