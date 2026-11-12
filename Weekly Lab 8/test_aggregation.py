from inventory import Inventory
from supplier import Suppliers
from physicalProduct import PhysicalProduct

# Create Supplier
supplier = Suppliers("S001", "Apple", "support@apple.com")

# Create Product BEFORE creating inventories
product = PhysicalProduct(
    "P001",
    "iPhone",
    1200.00,
    10,
    "physical",
    supplier,
    0.5
)

# Create Inventory A and Inventory B
inventory_a = Inventory()
inventory_b = Inventory()

# Add Product to Inventory A
inventory_a.add_product(product)

print("Inventory A:")
inventory_a.display_all()

# Remove Product from Inventory A
inventory_a.remove_product("P001")

print("\nAfter removing from Inventory A:")
inventory_a.display_all()

# Check whether Product still exists
print("\nCan the Product still be used?")
product.display_information()

# Add the SAME Product object to Inventory B
inventory_b.add_product(product)

print("\nInventory B:")
inventory_b.display_all()

# Remove Product from Inventory B
inventory_b.remove_product("P001")

print("\nAfter removing from Inventory B:")
inventory_b.display_all()

# Check Product still exists
print("\nProduct still exists:")
product.display_information()
