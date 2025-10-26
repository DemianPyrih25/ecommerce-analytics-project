import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/raw/data.csv', encoding='latin-1')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Month'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

print(f"Dataset shape: {df.shape}")
print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
df.groupby('Month')['TotalAmount'].sum().plot(kind='bar')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales Amount')

plt.subplot(1, 2, 2)
df.groupby('DayOfWeek')['TotalAmount'].sum().plot(kind='bar')
plt.title('Total Sales by Day of Week')
plt.xlabel('Day (0=Monday, 6=Sunday)')
plt.ylabel('Sales Amount')

plt.tight_layout()
plt.savefig('visualizations/sales_analysis.png')
plt.show()

print("\nVisualization saved to visualizations/sales_analysis.png")