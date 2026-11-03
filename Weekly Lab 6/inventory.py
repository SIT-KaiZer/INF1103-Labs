from product import Product

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to inventory.")

        if self.search_product(product.product_id, show_message=False) is not None:
            print("A product with this ID already exists.")
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str, show_message=True):
        """Return the matching Product, or None if it cannot be found."""
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.product_id.upper() == product_id:
                if show_message:
                    print("Product found:")
                    product.display_information()
                return product

        if show_message:
            print("Product not found.")
            print("Returning to Main Menu.")
        return None

    def display_all(self):
        print("\nCurrent Inventory:")
        print("-" * 60)

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()

        print("-" * 60)

    def get_all_products(self):
        return self.__products

    def update_stock(self, product_id: str, new_stock: int):
        product = self.search_product(product_id, show_message=False)

        if product is None:
            print("Product not found.")
            print("Returning to Main Menu.")
            return False

        if new_stock == product.stock:
            print("Invalid input. New stock cannot be the same as the previous stock.")
            return False

        product.update_stock(new_stock)
        print("Stock updated successfully!")
        return True

    def to_list(self):
        return [product.to_dict() for product in self.__products]