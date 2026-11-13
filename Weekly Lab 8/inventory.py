
from product import Product

class Inventory:

    def __init__(self):
        # Collection stores Product objects
        self.products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to inventory.")

        if self.find_product(product.product_id) is not None:
            print("A product with this ID already exists.")
            return False

        self.products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return False

        self.products.remove(product)
        print(f"Product {product_id} removed successfully.")
        return True

    def find_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().upper()

        for product in self.products:
            if product.product_id.upper() == product_id:
                return product

        return None

    def search_product(self, product_id: str, show_message: bool=True) -> Product | None:
        product = self.find_product(product_id)

        if product is not None:
            if show_message:
                print("Product found:")
                # product.display_information()
                self.show_product_details(product)
        else:
            if show_message:
                print("Product not found.")
                print("Returning to Main Menu.")

        return product

    def display_all(self)-> None:
        print("\nCurrent Inventory:")
        print("-" * 60)

        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                product.display_information()

        print("-" * 60)

    def get_all_products(self) -> list[Product]:
        return self.products

    def update_stock(self, product_id: str, new_stock: int) -> bool:
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return False

        if new_stock == product.stock:
            print("Invalid input. New stock cannot be the same as the previous stock.")
            return False

        product.update_stock(new_stock)
        print("Stock updated successfully!")
        return True

    def show_product_details(self, product: Product) -> None:
        product.display_information() 
        print(product.get_fulfilment_info())

    def to_list(self) -> list[dict[str, str, float, int, str, float]]:
        return [product.to_dict() for product in self.products]
