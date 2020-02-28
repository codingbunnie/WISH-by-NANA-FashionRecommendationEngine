from .data_classes import Product
import pandas as pd
import numpy as np

def list_products(data):
    """
    Helper function for listing products.

    Parameters:
       Input DataFrame

    Output:
       A list of Product objects.
    """
 
    return [Product.deserialize(product) for _, product in data.iterrows()]


def random_products(data, n):

   """
   Helper function for listing random products.

   Parameters:
      Input DataFrame

   Output:
      A list of random Product objects.
   """

   indices = np.random.randint(0, len(data), n)
   
   sample = data.iloc[indices]

   return list_products(sample)