from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from suppliers import Suppliers

supplier = Suppliers("S001", "Apple", "support@apple.com")

physical = PhysicalProduct(
    "P001", "iPhone", 1200.00, 10, "physical", supplier, 0.5
)

digital = DigitalProduct(
    "P002", "App", 10.00, 5, "digital", supplier, 100
)

del supplier

physical.display_supplier_information()
digital.display_supplier_information()