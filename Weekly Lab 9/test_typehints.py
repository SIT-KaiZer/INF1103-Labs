
import inspect
from typing import get_type_hints

from product import Product
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from suppliers import Suppliers
from inventory import Inventory
from order import Order
from orderLine import OrderLine
from canBeShipped import CanBeShipped


classes = [
    Product,
    PhysicalProduct,
    DigitalProduct,
    Suppliers,
    Inventory,
    Order,
    OrderLine,
    CanBeShipped
]



def check_class_type_hints(cls):

    print(f"\nChecking class: {cls.__name__}")
    print("-" * 50)

    constructor = cls.__init__
    constructor_hints = get_type_hints(constructor)

    if constructor_hints:
        print("Constructor type hints:")
        for parameter, hint in constructor_hints.items():
            print(f"  {parameter}: {hint}")
    else:
        print("No constructor type hints found.")

    for method_name, method in inspect.getmembers(cls, predicate=inspect.isfunction):

        
        if method.__qualname__.split(".")[0] != cls.__name__:
            continue

        method_hints = get_type_hints(method)

        if method_hints:
            print(f"\nMethod: {method_name}")

            for parameter, hint in method_hints.items():
                print(f"  {parameter}: {hint}")
        else:
            print(f"\nMethod: {method_name} - No type hints found.")




for cls in classes:
    check_class_type_hints(cls)
