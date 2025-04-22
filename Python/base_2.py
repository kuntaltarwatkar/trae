import pandas as pandas
import numpy as numpy
import os

os.chdir('F://99 minds//2025//99minds_Pravin//')
pandas.set_option('Display.max_rows', 10000)
pandas.set_option('Display.max_column', 10000)
pandas.set_option('Display.width', 10000)

# Set pandas display options to prevent scientific notation
pandas.set_option('display.float_format', '{:.0f}'.format)

# Read the CSV file with gift card numbers as string type
data_1 = pandas.read_csv(filepath_or_buffer = 'CMACVCARD1-USD.csv', dtype={'Gift card number': str})
print(data_1.head())