from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from suppliers import Suppliers


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Suppliers,
        weight: float = 0.0,
        download_size: float = 0.0,
    ) -> Product:
        if product_type == "physical":
            return PhysicalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                product_type,
                supplier,
                weight,
            )
        elif product_type == "digital":
            return DigitalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                product_type,
                supplier,
                download_size,
            )
        else:
            raise ValueError(f"Unknown product type: {product_type}")   