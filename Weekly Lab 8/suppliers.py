class Suppliers():
    def __init__(self,supplier_id: str, name: str, contact_email: str) -> None:
        self.supplier_id:str = supplier_id
        self.name:str = name
        self.contact_email:str = contact_email

    def display_information(self)-> None:
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Name: {self.name}")
        print(f"Contact Email: {self.contact_email}")

    def to_dict(self)-> dict[str, str]:
        return {
            "SupplierID": self.supplier_id,
            "Name": self.name,
            "ContactEmail": self.contact_email
        }

    