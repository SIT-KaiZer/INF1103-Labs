
from suppliers import Suppliers
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from inventory import Inventory

supplier = Suppliers(
    "S001",
    "Apple",
    "support@apple.com"
)

inventory = Inventory()

iphone = PhysicalProduct(
    "P001",
    "iPhone",
    1200.00,
    10,
    "physical",
    supplier,
    0.5
)

steam_game = DigitalProduct(
    "P002",
    "Steam Game",
    60.00,
    20,
    "digital",
    supplier,
    1000.0
)

inventory.add_product(iphone)
inventory.add_product(steam_game)

print("\n========== PRODUCT INFORMATION ==========")


products = inventory.get_all_products()

for product in products:
    
    product.display_information()
    print("Fulfilment Information:")
    print(product.get_fulfilment_info())
