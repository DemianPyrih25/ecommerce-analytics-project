import pandas as pd
import numpy as np

df = pd.read_csv('data/raw/data.csv', encoding='latin-1')

print("First 5 rows:")
print(df.head())

print("/nDataset information:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())

print(f"\nDataset shape: {df.shape}")