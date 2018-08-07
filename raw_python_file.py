"""
This python file generates some data and then squares the item in the array
"""

import numpy as np

def generate_data():
    "Generates some fake data"
    return np.array([1, 2, 3])

SQUARE_ME = lambda x: x ** 2

MY_ARRAY = generate_data()

print(SQUARE_ME(MY_ARRAY))
