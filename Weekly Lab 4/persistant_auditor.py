def get_valid_input():
    print("get valid input called")

def load_orders():
    print("load orders called")
    with open(".\Weekly Lab 4\orders.txt", "r") as file:
        orders = file.read()
        print(f"Current orders:\n{orders}")
    
def save_orders():
    print("save orders called")

def generate_report():
    print("generate report called")

while True:
    load_orders()
    
    print("test")
    break
