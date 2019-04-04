#!/usr/bin/env python
"""
Transform the sales data into just the important 3 columns and save it as a new output csv file.
"""

__author__ = "Shahzeb Khan"
__version__ = "0.1.0"

# Imports
import pandas as pd

# Globals
pd.options.mode.chained_assignment = None  # default='warn'
OUTPUT_DIR = 'output'

# Methods
def convert_data():
    """ Converts the data using pandas """
    data = pd.read_csv('data/sample-data.csv')
    sub_group = data[['Region', 'Country', 'Total Cost']]
    sub_group['Region'] = sub_group['Region'].apply(lambda x: x.lower())
    sub_group.to_csv('{}/converted-data.csv'.format(OUTPUT_DIR))

def main():
    """ Main entry point of the app """
    convert_data()

if __name__ == "__main__":
    main()
