from product import Product
from orderLine import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
    
    def display_order(self) -> None:
        print(f"\nOrder ID: {self.order_id}")
        print("-" * 60)

        for order_line in self.order_lines:
            print(f"Product: {order_line.product.name}")
            print(f"Product ID: {order_line.product.product_id}")
            print(f"Quantity: {order_line.quantity}")
            print(f"Unit Price: ${order_line.product.price:.2f}")
            print(f"Subtotal: ${order_line.calculate_subtotal():.2f}")
            print("-" * 60)

        print(f"Order Total: ${self.calculate_total():.2f}")

    def remove_order_line(self, index: int) -> bool:
        if not isinstance(index, int) or isinstance(index, bool):
            return False

        if index < 0 or index >= len(self.order_lines):
            print("Invalid order line index.")
            return False

        self.order_lines.pop(index)
        return True