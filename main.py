### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 2

### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1

#Package Imports
import pandas as pd
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all columns
pd.set_option('display.width', 0)  # Adjust width to fit content

df = pd.read_csv("data/poop_map.csv")

print(df)
