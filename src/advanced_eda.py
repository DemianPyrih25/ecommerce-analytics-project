import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('data/raw/data.csv', encoding='latin = 1')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Month'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

print("Data loaded for advanced EDA!")

plt.figure(figsize=(12, 6))
top_products = df.groupby('StockCode')['TotalAmount'].sum().nlargest(10)
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Products by Total Sales')
plt.xlabel('Product Code (StockCode)')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/top_products.png')
print("Top products chart saved!")

plt.figure(figsize=(12, 6))
top_customers = df.groupby('CustomerID')['TotalAmount'].sum().nlargest(10)
top_customers.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Customers by Total Spending')
plt.xlabel('Customer ID')
plt.ylabel('Total Amount Spent')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/top_customers.png')
print("Top customers chart saved!")

plt.figure(figsize=(12, 6))
clean_prices = df[(df['UnitPrice'] > 0.01) & (df['UnitPrice'] < 100)]['UnitPrice']
plt.hist(clean_prices, bins=50, color='gold', edgecolor='black')
plt.title('Distribution of Unit Prices (0.01 - $100)')
plt.xlabel('Price ($)')
plt.ylabel('Number of Products')
plt.tight_layout()
plt.savefig('visualizations/price_distribution.png')
print("Price distribution chart saved!")