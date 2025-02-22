### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 2

#Package Imports
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all columns
pd.set_option('display.width', 0)  # Adjust width to fit content

df = pd.read_csv("data/obesity.csv")

# Specify the x-axis and y-axis columns
x_column = "OBJECTID"  # Replace with the actual column name
y_column = "Obesity"  # Replace with the actual column name

# Plot the data
plt.figure(figsize=(15,5)) #Sets custom dimensions of graph
plt.plot(df[x_column], df[y_column], marker="o", linestyle="-")  # Line plot example

# Labels and title
plt.xlabel("State")
plt.ylabel("Obesity(%)")
plt.title("Obesity by State")

plt.xticks(range(1, 53, 1))  #Sets the ticks the graph counts by
# Save in a folder called charts as PNG files
plt.savefig(f"charts/Obesity.png")

print(df)


