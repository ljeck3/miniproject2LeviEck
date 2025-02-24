### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 2

#Package Imports
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True) #CREATES CHARTS DIRECTORY

df = pd.read_csv("data/obesity.csv") #READS CSV FILE

states = ['47', '25', '0', '12', '41']

for i in states:
    cell_value = df.at[int(i), "Obesity"]
    state_name = df.at[int(i), "NAME"]

    labels = ['Obese', 'Not Obese']
    sizes = [cell_value, 100-cell_value]
    plt.clf()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=0.5)
    plt.title("Obesity Percentage in " + state_name)
    plt.savefig(f"charts/{state_name}.png") #SAVES CHARTS



