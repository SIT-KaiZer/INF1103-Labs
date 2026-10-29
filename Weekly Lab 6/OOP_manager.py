class Product:

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = str(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__stock = int(stock)

    def update_stock(self, quantity: int):
            """Set the product's stock to a new non-negative quantity."""
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("Stock quantity must be a non-negative integer.")
            self.__stock = quantity

    def display_information(self):
        print(
            f"ProductID: {self.__product_id}, "
            f"Name: {self.__name}, "
            f"Price: {self.__price:.2f}, "
            f"Stock: {self.__stock}"
        )