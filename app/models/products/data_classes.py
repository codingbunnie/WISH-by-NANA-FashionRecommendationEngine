"""
Data class for products.
"""
from dataclasses import dataclass
# from typing import List

@dataclass
class Product:
    """
    Data class for products.
    """
    name: str
    hrefs: str
    imageURL: str
    price: str
    category: str
    brand: str

    @staticmethod
    def deserialize(row):

        """
        Deserialize a row in the DataFrame
        """
        if not row.empty:
            return Product(
                name=row['name'],
                hrefs=row['hrefs'],
                imageURL=row['imageURL'],
                price=row['price'],
                category=row['category'],
                brand=row['brand']
            )