class Product:

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)
        self.stock = int(stock)


    def update_stock(self, quantity: int):
            """Set the product's stock to a new non-negative quantity."""
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("Stock quantity must be a non-negative integer.")
            self.__stock = quantity

    def display_information(self):
        print(
            f"ProductID: {self.product_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price:.2f}, "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        """Convert this object to a dictionary for JSON storage."""
        return {
            "ProductID": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Stock": self.stock,
        }

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.weight = float(weight)
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.download_size = float(download_size)
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size:.2f} MB")