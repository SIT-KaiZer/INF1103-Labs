from abc import ABC, abstractmethod
from supplier import Suppliers

class Product(ABC):


    def __init__(self, product_id, name, price, stock, product_type, supplier : Suppliers):
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)
        self.stock = int(stock)
        self.product_type = str(product_type)
        self.supplier: Suppliers = supplier


    def update_stock(self, quantity: int):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")

        self.stock = quantity
    
    def display_information(self):
        print(
            f"ProductID: {self.product_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price:.2f}, "
            f"Stock: {self.stock}, "
            f"ProductType: {self.product_type}, "
            f"SupplierID: {self.supplier.supplier_id}, "
            f"supplierName: {self.supplier.name}, "
            f"ContactEmail: {self.supplier.contact_email}"
        )

    def to_dict(self):
        return {
            "ProductID": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Stock": self.stock,
            "ProductType": self.product_type,
            "SupplierID": self.supplier.supplier_id
        }

    def display_supplier_information(self):
        print("\nSupplier Information:")
        self.supplier.display_information()
    
    @abstractmethod
    def get_fulfilment_info(self):
        """Return a string with fulfilment information specific to the product type."""
        pass
