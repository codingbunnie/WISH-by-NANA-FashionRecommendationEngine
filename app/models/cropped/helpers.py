from .data_classes import CroppedImage
import pandas as pd

def list_object(data):
    """
    Helper function for listing Cropped Images

    Parameters:
       Input DataFrame

    Output:
       A list of CroppedImage objects.
    """
 
    return [CroppedImage.deserialize(category, path) for category, path in data]