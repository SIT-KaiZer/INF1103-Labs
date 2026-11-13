from product import Product
from suppliers import Suppliers

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, product_type: str, supplier: Suppliers, download_size: float)-> None:
        super().__init__(product_id, name, price, stock, product_type, supplier)
        self.download_size = float(download_size)
    def display_information(self)-> None:
        super().display_information()
        print(f"Download Size: {self.download_size:.2f} MB")
        
    def get_fulfilment_info(self)-> str:
        return f"{self.name} (ID: {self.product_id}) ({self.download_size:.2f} MB) has to be downloaded as it is a digital product."

    def to_dict(self)-> dict[str, str, float, int, str, float]:
        data = super().to_dict()
        data["DownloadSize"] = self.download_size
        return data