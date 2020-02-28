"""
Data class for cropped image.
"""
from dataclasses import dataclass
# from typing import List

@dataclass
class CroppedImage:
    """
    Data class for cropped image.
    """

    category: str
    path: str

    @staticmethod
    def deserialize(category, path):

        """
        Deserialize a row in the DataFrame
        """
        return CroppedImage(
            category=category,
            path=path
        )