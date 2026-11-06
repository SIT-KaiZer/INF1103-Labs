from product import Product
from canBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, product_type: str, weight: float):
        super().__init__(product_id, name, price, stock, product_type)
        self.weight = float(weight)
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")
        
    def get_fulfilment_info(self):
        return f"{self.name} (ID: {self.product_id}) weighing {self.weight:.2f} kg has to to be shipped to the customer as it is a physical product."
    
    def calculate_shipping_cost(self):
        """Calculate shipping cost based on weight."""
        base_cost = 5.00  # Base shipping cost
        cost_per_kg = 2.00  # Cost per kilogram
        return base_cost + (cost_per_kg * self.weight)

    def to_dict(self):
        data = super().to_dict()
        data["Weight"] = self.weight
        return data
    