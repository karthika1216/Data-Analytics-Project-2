import pandas as pd

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("Mean Quantity:", df["Quantity"].mean())