from product import Product
from canBeShipped import CanBeShipped
from suppliers import Suppliers
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, product_type: str, supplier: Suppliers, weight: float)-> None:
        super().__init__(product_id, name, price, stock, product_type, supplier)
        self.weight: float = float(weight)

    def display_information(self)-> None:
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")
        
    def get_fulfilment_info(self)-> str:
        return f"{self.name} (ID: {self.product_id}) weighing {self.weight:.2f} kg has to to be shipped to the customer as it is a physical product."
    
    def calculate_shipping_cost(self)-> float:
        """Calculate shipping cost based on weight."""
        base_cost = 5.00  # Base shipping cost
        cost_per_kg = 2.00  # Cost per kilogram
        return base_cost + (cost_per_kg * self.weight)

    def to_dict(self)-> dict[str, str, float, int, str, float]:
        data = super().to_dict()
        data["Weight"] = self.weight
        return data
    