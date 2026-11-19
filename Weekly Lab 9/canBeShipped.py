from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self)-> float:
        """Calculate and return the shipping cost for the product."""
        pass