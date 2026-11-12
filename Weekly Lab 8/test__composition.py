from supplier import Suppliers
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from order import Order

supplier = Suppliers(
    "S001",
    "Apple",
    "support@apple.com"
)

iphone = PhysicalProduct(
    "P001",
    "iPhone",
    1200.00,
    10,
    "physical",
    supplier,
    0.5
)

ipad = PhysicalProduct(
    "P002",
    "iPad",
    1000.00,
    5,
    "physical",
    supplier,
    1.2
)

steam_game = DigitalProduct(
    "P003",
    "Steam Game",
    60.00,
    20,
    "digital",
    supplier,
    1000.0
)

order1 = Order("O001")

order1.add_order_line(iphone, 2)
order1.add_order_line(ipad, 1)
order1.add_order_line(steam_game, 1)

order1.display_order()

print("\n\n\n")

order2 = Order("O002")
order2.add_order_line(iphone, 1)
order2.display_order()

print("\n========== OBJECT IDENTITY TEST ==========")

print(
    "Same Product object:",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Same OrderLine object:",
    order1.order_lines[0] is order2.order_lines[0]
)


print("\n========== REMOVE ORDER LINE ==========")

order1.remove_order_line(0)

print("\nOrder 1 after removing its first OrderLine:")
order1.display_order()

print("\nOrder 2 remains unchanged:")
order2.display_order()

# Check whether the original Product still exists
print("\nCan the iPhone Product still be used?")
iphone.display_information()