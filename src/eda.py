import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/raw/data.csv', encoding='latin-1')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Mouth'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.month
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

print(f"Dataset shape: {df.shape}")
print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")