import pandas as pd

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("Median Quantity:", df["Quantity"].median())