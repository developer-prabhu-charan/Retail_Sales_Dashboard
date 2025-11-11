# etl/etl_transform.py
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# MySQL connection (container mapped to localhost:3306)
ENGINE_STR = "mysql+pymysql://root:rootpwd@localhost:3306/retail_db"
engine = create_engine(ENGINE_STR)

# 1. Read raw table from MySQL
df = pd.read_sql("SELECT * FROM sales", engine)

# 2. Clean & normalize columns
df.columns = [c.strip() for c in df.columns]
# Parse dates
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
# Numeric conversions
for col in ['Quantity','UnitPrice','Sales','Discount','Profit','ProfitMargin']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Derived/fix logic
# Recalculate Sales if missing or inconsistent
df['Sales_calc'] = (df['Quantity'] * df['UnitPrice']).round(2)
df['Sales'] = df['Sales'].fillna(df['Sales_calc'])
# Recalculate ProfitMargin where missing
df['ProfitMargin_calc'] = (df['Profit'] / df['Sales']).replace([np.inf, -np.inf], pd.NA)
df['ProfitMargin'] = df['ProfitMargin'].fillna(df['ProfitMargin_calc'])
# Recalculate Profit if missing
df['Profit'] = df['Profit'].fillna((df['Sales'] * df['ProfitMargin']).round(2))

# 4. Add Year & Month for analytics
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['OrderYearMonth'] = df['OrderDate'].dt.to_period('M').astype(str)

# 5. Basic cleaning: drop rows with missing OrderID or OrderDate
df = df.dropna(subset=['OrderID','OrderDate'])

# 6. Reorder columns and export cleaned CSV
cols = ['OrderID','OrderDate','Year','Month','OrderYearMonth','CustomerID','CustomerName','Region','State','City',
        'Category','SubCategory','ProductID','ProductName','Quantity','UnitPrice','Sales','Discount','Profit','ProfitMargin',
        'OrderPriority','ShipMode']
cols = [c for c in cols if c in df.columns]
out_path = "../data/clean_sales_transformed.csv"
df[cols].to_csv(out_path, index=False, float_format='%.2f', date_format='%Y-%m-%d')
print("Saved cleaned CSV to:", out_path)
