from abc import ABC, abstractmethod


class Product(ABC):


    def __init__(self, product_id, name, price, stock, product_type):
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)
        self.stock = int(stock)
        self.product_type = str(product_type)


    def update_stock(self, quantity: int):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")

        self.stock = quantity
    
    def display_information(self):
        print(
            f"ProductID: {self.product_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price:.2f}, "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "ProductID": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Stock": self.stock,
            "ProductType": self.product_type
        }
    @abstractmethod
    def get_fulfilment_info(self):
        """Return a string with fulfilment information specific to the product type."""
        pass
