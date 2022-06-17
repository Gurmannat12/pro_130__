import pandas as pd
import csv

df = pd.read_csv("merged_dataset1.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

df = df[df['Star_name'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

print(df.shape)

df.to_csv('final.csv')

print(list(df))
