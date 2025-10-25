import pandas as pd
import numpy as np

df = pd.read_csv('data/raw/data.csv', encoding='latin-1')

print("Original columns:")
print(df.columns.tolist())

df['InvoiceData'] = pd.to_datetime(df['InvoiceData'])

df('Month') = df['InvoiceData'].dt.mouth

df['DayOfWeek'] = df['InvoiceData'].dt.dayofweek