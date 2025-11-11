# etl/make_bq_csv.py
import pandas as pd
import numpy as np
from pathlib import Path
import csv  # for QUOTE_MINIMAL

# Paths (adjust if needed)
IN_PATH  = Path("data/clean_sales_transformed.csv")   # input you already created
OUT_PATH = Path("data/clean_sales_transformed_bq.csv")  # sanitized for BigQuery

if not IN_PATH.exists():
    raise SystemExit(f"Input file not found: {IN_PATH.resolve()}")

# Read without forcing everything to string so numbers stay numeric
df = pd.read_csv(IN_PATH)

# Identify only text-like columns
text_cols = df.select_dtypes(include=["object", "string"]).columns

# Clean text columns safely: remove newlines/CR, trim, collapse multiple spaces
for c in text_cols:
    s = df[c].astype("string")  # pandas nullable string dtype (keeps NaN as <NA>)
    s = s.str.replace("\r\n", " ", regex=False)\
         .str.replace("\n",  " ", regex=False)\
         .str.replace("\r",  " ", regex=False)\
         .str.replace(r"\s+", " ", regex=True)\
         .str.strip()
    df[c] = s

# (Optional) enforce consistent date format if you have a date column
for date_col in [col for col in df.columns if "Date" in col or col.lower() == "orderdate"]:
    try:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce").dt.strftime("%Y-%m-%d")
    except Exception:
        pass  # skip if not actually a date

# Write a clean CSV for BigQuery (LF line endings, minimal quoting)
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_PATH, index=False, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
print(f"✅ Wrote BigQuery-ready CSV -> {OUT_PATH.resolve()}")
print(f"    Rows: {len(df)}, Columns: {len(df.columns)}")