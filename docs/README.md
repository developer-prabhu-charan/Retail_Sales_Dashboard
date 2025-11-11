# 📊 Retail Sales Analytics Pipeline

> **End-to-End Data Engineering Project** — From Raw CSV to Interactive Analytics Dashboard

<div align="center">

![Data Pipeline](https://img.shields.io/badge/Pipeline-CSV%20→%20MySQL%20→%20BigQuery%20→%20Looker-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python)
![BigQuery](https://img.shields.io/badge/BigQuery-Sandbox-4285F4?style=flat-square&logo=google-cloud)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

**Author:** [Prabhu Charan](#)  
**GCP Project:** `sales-data-analysis-477907` | **Dataset:** `retail_ds`

</div>

---

## 🎯 Overview

A **production-ready data pipeline** that demonstrates modern data engineering principles. This project showcases:

✨ **Key Features:**
- 🐳 **Containerized MySQL** for simulated on-premise data source
- 🔄 **Python ETL Pipeline** with pandas for data cleaning & transformation
- ☁️ **Google BigQuery Sandbox** for scalable cloud data warehouse (no billing)
- 📈 **Interactive Looker Studio Dashboard** with KPIs, trends, and drill-down filters
- 📚 **Production-grade** SQL queries and documentation

**Core KPIs Tracked:**
- 💰 Total Sales & Profit
- 📊 Profit Margin Analysis
- 📅 Monthly Sales Trends
- 🗺️ Regional Performance
- 🏆 Top Products & Categories

---

## 📝 Project Description

### **What is This Project?**

This is a **complete end-to-end data engineering solution** that simulates a real-world retail analytics platform. It demonstrates how enterprises move data from transactional systems to cloud-based data warehouses for business intelligence and decision-making.

### **Business Problem Solved**

A retail company has sales data scattered across multiple systems. This project provides:

1. **Centralized Data Management** — Consolidate raw CSV/database records into a unified data warehouse
2. **Data Quality Assurance** — Clean, validate, and enrich data through automated ETL processes
3. **Scalable Analytics** — Move from on-premise MySQL to cloud-based BigQuery for unlimited scale
4. **Self-Service BI** — Enable business users to explore data and create insights with Looker Studio dashboards

### **Technical Workflow**

```
┌─────────────────────────────────────────────────────────────────┐
│                         THE JOURNEY                             │
└─────────────────────────────────────────────────────────────────┘

📥 INGEST
   └─ Read sales.csv (raw retail transactions)
   └─ Load into MySQL with SQLAlchemy

🔄 TRANSFORM (ETL)
   └─ Parse dates & numeric types
   └─ Validate & deduplicate records
   └─ Compute derived metrics (ProfitMargin, YearMonth)
   └─ Clean text fields & handle nulls
   └─ Output: clean_sales_transformed.csv

✅ VALIDATE
   └─ Schema verification
   └─ Row count validation
   └─ Data type checks

☁️ LOAD (BigQuery)
   └─ Upload CSV to BigQuery Sandbox (free tier)
   └─ Auto-detect schema
   └─ Create `retail_ds.sales` table

📊 VISUALIZE
   └─ Connect Looker Studio to BigQuery
   └─ Create KPI scorecards
   └─ Build trend charts & filters
   └─ Share interactive dashboard
```

### **Who Should Use This?**

✅ **Data Engineers** — Learn ETL pipeline design, data validation, cloud integration  
✅ **Data Analysts** — Understand the data journey from source to BI tool  
✅ **Business Analysts** — See how raw data transforms into business intelligence  
✅ **Students** — Portfolio project demonstrating real-world data skills  
✅ **Portfolio Builders** — Production-ready project for job interviews  

### **Key Value Propositions**

| Aspect | Benefit |
|--------|---------|
| **Cost** | Uses BigQuery Sandbox (free) — no billing, no setup fees |
| **Speed** | Automates repetitive data tasks with Python scripts |
| **Reliability** | Data validation at each pipeline stage |
| **Scalability** | Handles 100s or 1000s of records seamlessly |
| **Transparency** | Documented SQL queries and process steps |
| **Reusability** | Code patterns applicable to other datasets |

### **Real-World Applications**

This pipeline pattern applies to many industries:

- **Retail:** Sales, inventory, customer behavior analysis
- **Finance:** Transaction monitoring, fraud detection, P&L reporting
- **Healthcare:** Patient records, treatment outcomes, billing analytics
- **E-Commerce:** Order tracking, customer segments, product performance
- **Manufacturing:** Production metrics, supply chain, quality assurance
- **SaaS:** Usage analytics, customer churn prediction, feature adoption

### **Project Outcomes**

After completing this project, you will have:

📦 **Deliverables**
- 3 production-ready Python ETL scripts
- 10+ validated SQL queries
- Interactive Looker Studio dashboard
- Complete documentation & architecture diagrams
- Portfolio-ready GitHub repository

🎓 **Skills Demonstrated**
- Data pipeline orchestration
- Python data processing (pandas, SQLAlchemy)
- MySQL database administration
- Cloud data warehousing (BigQuery)
- SQL analytics & query optimization
- Business intelligence visualization
- DevOps fundamentals (Docker)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RETAIL SALES PIPELINE                        │
└─────────────────────────────────────────────────────────────────┘

    CSV                  MySQL              Python ETL
  (Source)             (On-Prem)          (Transform)
     │                    │                    │
     └──────────────────→ │ ←─ Load CSV        │
                          │                    │
                          └──────────────────→ │
                                               │
                                    ┌──────────┴───────────┐
                                    │                      │
                            Validation          Sanitization
                            (optional)          (optional)
                                    │                      │
                                    └──────────┬───────────┘
                                               │
                              ┌────────────────┘
                              │
                        BigQuery Sandbox
                        (retail_ds.sales)
                              │
                              │
                        Looker Studio
                         (Dashboard)
```

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Source** | CSV (Synthetic Retail Data) | - |
| **Database** | MySQL + Docker | 8.0 |
| **ETL** | Python • pandas • SQLAlchemy | 3.10+ |
| **Cloud DW** | Google BigQuery (Sandbox) | Free |
| **BI Tool** | Looker Studio | - |
| **Environment** | Windows 11 + PowerShell | - |
| **IDE** | VS Code | Latest |

---

## 📁 Repository Structure

```
retail_cloud_project/
│
├── 📄 README.md                          ← Project documentation
├── 📝 requirements.txt                   ← Python dependencies
├── 🔐 gcp-key.json                       ← GCP credentials (git-ignored)
│
├── 📂 data/
│   ├── sales.csv                         # Source: 100-row synthetic data
│   ├── clean_sales_transformed.csv       # ETL output (main)
│   └── clean_sales_transformed_bq.csv    # BQ-optimized (sanitized)
│
├── 📂 etl/
│   ├── load_to_mysql.py                  # Ingest CSV → MySQL
│   ├── etl_transform.py                  # Main ETL pipeline
│   └── make_bq_csv.py                    # CSV sanitizer for BigQuery
│
├── 📂 bigquery/
│   ├── queries.sql                       # Validation & analysis queries
│   └── schema.json                       # Table schema (optional)
│
├── 📂 gcloud/
│   └── upload_to_gcs.py                  # GCS upload (optional)
│
├── 📂 mysql/
│   └── init.sql                          # MySQL schema initialization
│
└── 📂 docs/
    └── screenshots/                      # Dashboard screenshots
```

---

## 📦 Dependencies

```txt
pandas                      # Data manipulation
sqlalchemy                  # ORM & database abstraction
pymysql                     # MySQL connector (pure Python)
mysql-connector-python      # MySQL official connector
python-dateutil             # Date utilities
google-cloud-bigquery       # BigQuery client library (optional)
```

**Install all dependencies:**

```powershell
pip install -r .\requirements.txt
```

---

## 🚀 Quick Start

### 1️⃣ Prerequisites

- ✅ **Docker Desktop** (Windows)
- ✅ **Python 3.10+**
- ✅ **Google Cloud Account** (free BigQuery Sandbox)
- ✅ **VS Code** + PowerShell

### 2️⃣ Environment Setup

```powershell
# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r .\requirements.txt
```

### 3️⃣ Launch MySQL Container

```powershell
docker run --name mysql-retail `
  -e MYSQL_ROOT_PASSWORD=rootpwd `
  -e MYSQL_DATABASE=retail_db `
  -p 3306:3306 `
  -d mysql:8.0
```

Verify MySQL is running:

```powershell
docker ps -a | findstr mysql-retail
```

---

## 📋 Step-by-Step Execution

### **Step A:** Initialize MySQL Schema

Connect to MySQL and create the `sales` table:

```powershell
docker exec -it mysql-retail mysql -u root -p
# Password: rootpwd
```

Then paste this SQL:

```sql
USE retail_db;

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
  OrderID VARCHAR(50) PRIMARY KEY,
  OrderDate DATE,
  CustomerID VARCHAR(50),
  CustomerName VARCHAR(150),
  Region VARCHAR(50),
  State VARCHAR(100),
  City VARCHAR(100),
  Category VARCHAR(100),
  SubCategory VARCHAR(100),
  ProductID VARCHAR(50),
  ProductName VARCHAR(255),
  Quantity INT,
  UnitPrice DECIMAL(12,2),
  Sales DECIMAL(12,2),
  Discount DECIMAL(6,4),
  Profit DECIMAL(12,2),
  ProfitMargin DECIMAL(8,4),
  OrderPriority VARCHAR(50),
  ShipMode VARCHAR(100),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Verify table creation:

```sql
SHOW TABLES;
DESC sales;
```

---

### **Step B:** Load CSV Data into MySQL

**File:** `etl/load_to_mysql.py`

```python
import pandas as pd
from sqlalchemy import create_engine

# Read source CSV
df = pd.read_csv(r'./data/sales.csv')

# Create database connection
engine = create_engine(
    "mysql+pymysql://root:rootpwd@localhost:3306/retail_db",
    echo=False
)

# Load to MySQL
df.to_sql(
    'sales',
    con=engine,
    if_exists='replace',
    index=False,
    chunksize=500
)

print(f"✅ Successfully uploaded {len(df)} rows to MySQL.")
engine.dispose()
```

**Run the loader:**

```powershell
python .\etl\load_to_mysql.py
```

**Verify data:**

```powershell
docker exec mysql-retail mysql -u root -prootpwd -e "USE retail_db; SELECT COUNT(*) as row_count FROM sales;"
```

---

### **Step C:** Run ETL Transformation

**File:** `etl/etl_transform.py`

This script performs:
- ✅ Parse dates & coerce numeric types
- ✅ Recompute `Sales` and `ProfitMargin` where missing
- ✅ Add derived columns: `Year`, `Month`, `OrderYearMonth`
- ✅ Clean text fields (trim, lowercase where appropriate)
- ✅ Remove duplicates

**Run transformation:**

```powershell
python .\etl\etl_transform.py
# Output: data/clean_sales_transformed.csv
```

---

### **Step D:** (Optional) Sanitize for BigQuery

Removes problematic characters and newlines from CSV:

```powershell
python .\etl\make_bq_csv.py
# Output: data/clean_sales_transformed_bq.csv
```

---

### **Step E:** Load into BigQuery Sandbox

#### **Option 1 — BigQuery Web UI** (Recommended for beginners)

1. Open [Google BigQuery Console](https://console.cloud.google.com/bigquery)
2. Select project: **`sales-data-analysis-477907`**
3. Create new dataset:
   - Name: `retail_ds`
   - Location: **US** (required for Sandbox)
   - Click **Create Dataset**

4. Create new table:
   - **Source:** Upload → Select file `data/clean_sales_transformed_bq.csv`
   - **Format:** CSV
   - **Destination:** `sales-data-analysis-477907.retail_ds.sales`
   - **Schema:** ☑️ Auto detect
   - **Advanced Options:** Skip header rows = **1**
   - Click **Create Table**

#### **Option 2 — BigQuery CLI** (For automation)

```powershell
# Create dataset
bq --location=US mk -d sales-data-analysis-477907:retail_ds

# Load CSV
bq --location=US load `
  --autodetect `
  --source_format=CSV `
  sales-data-analysis-477907:retail_ds.sales `
  ".\data\clean_sales_transformed_bq.csv"
```

---

## 📊 Validation Queries

Run these queries in BigQuery to validate the pipeline. See `bigquery/queries.sql` for full details.

### **Row Count**

```sql
SELECT COUNT(*) AS total_rows
FROM `sales-data-analysis-477907.retail_ds.sales`;
```

### **Core KPIs**

```sql
SELECT 
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  ROUND(AVG(ProfitMargin), 4) AS avg_profit_margin,
  COUNT(DISTINCT OrderID) AS total_orders
FROM `sales-data-analysis-477907.retail_ds.sales`;
```

### **Monthly Sales Trend**

```sql
SELECT 
  OrderYearMonth,
  ROUND(SUM(Sales), 2) AS monthly_sales,
  COUNT(DISTINCT OrderID) AS order_count
FROM `sales-data-analysis-477907.retail_ds.sales`
GROUP BY OrderYearMonth
ORDER BY OrderYearMonth ASC;
```

### **Regional Performance**

```sql
SELECT 
  Region,
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  ROUND(AVG(ProfitMargin), 4) AS avg_margin
FROM `sales-data-analysis-477907.retail_ds.sales`
GROUP BY Region
ORDER BY total_sales DESC;
```

### **Top 10 Products**

```sql
SELECT 
  ProductName,
  ROUND(SUM(Sales), 2) AS total_sales,
  SUM(Quantity) AS total_quantity,
  ROUND(AVG(ProfitMargin), 4) AS avg_margin
FROM `sales-data-analysis-477907.retail_ds.sales`
GROUP BY ProductName
ORDER BY total_sales DESC
LIMIT 10;
```

---

## 📈 Build Looker Studio Dashboard

### **Dashboard Setup**

1. Open [Looker Studio](https://lookerstudio.google.com/)
2. Create **Blank Report**
3. **Add Data Source:**
   - Click **Create New Data Source**
   - **Connector:** BigQuery
   - Select: `sales-data-analysis-477907 → retail_ds → sales`
   - **Connect**

### **Visualizations**

Add these components to your dashboard:

#### **Scorecards (Top-left)**
- **Total Sales:** `SUM(Sales)`
- **Total Profit:** `SUM(Profit)`
- **Avg Margin:** `AVG(ProfitMargin)`

#### **Line Chart (Center)**
- X-axis: `OrderYearMonth`
- Y-axis: `SUM(Sales)`
- Title: "Monthly Sales Trend"

#### **Bar Chart (Right)**
- X-axis: `Region`
- Y-axis: `SUM(Sales)`
- Title: "Sales by Region"

#### **Data Table (Bottom)**
- Dimensions: `ProductName`, `Category`
- Metrics: `SUM(Sales)`, `SUM(Quantity)`, `AVG(ProfitMargin)`
- Sort: Sales (descending)

#### **Filters (Top)**
- Dropdown 1: `Category`
- Dropdown 2: `Region`

### **Styling**

```
🎨 Color Scheme:
├─ Background: #F5F5F5
├─ Cards: #FFFFFF (with subtle shadow)
├─ Primary: #1F77B4 (Blue)
├─ Success: #2CA02C (Green)
└─ Warning: #FF7F0E (Orange)

📐 Layout:
├─ Title: "Retail Sales Dashboard — Prabhu Charan"
├─ Font: Roboto / Arial
├─ Border Radius: 4px
└─ Theme: Light + Minimal
```

### **Export & Share**

1. Click **Share** (top-right)
2. Change to **Viewer** access
3. Enable **Allow viewers to download this report**
4. Copy shareable link
5. Export to PDF for portfolio

---

## � Project Showcase

### **BigQuery Table Preview**

After loading data into BigQuery, you should see your table with all columns and rows:

```
📊 Table: sales-data-analysis-477907.retail_ds.sales
├─ Rows: ~100 (your dataset size)
├─ Columns: 19
├─ Size: ~XX KB
└─ Last Modified: [Your timestamp]
```

**Key Columns Visible:**
- OrderID, OrderDate, CustomerName
- Region, State, City
- Category, SubCategory, ProductName
- Quantity, UnitPrice, Sales, Discount, Profit, ProfitMargin
- Year, Month, OrderYearMonth

### **BigQuery Query Results**

Example output from core KPI query:

```
┌─────────────┬──────────────┬──────────────────────┐
│ total_sales │ total_profit │ avg_profit_margin    │
├─────────────┼──────────────┼──────────────────────┤
│ $XXX,XXX.XX │ $XX,XXX.XX   │ 0.XXXX (XX.XX%)      │
└─────────────┴──────────────┴──────────────────────┘
```

### **Looker Studio Dashboard**

The interactive dashboard includes:

📊 **Dashboard Overview:**
- **Top Section:** 3 Scorecards (Total Sales, Total Profit, Avg Profit Margin)
- **Middle Section:** Monthly trend line chart showing sales over time
- **Right Section:** Regional performance bar chart
- **Bottom Section:** Top products data table
- **Top Filters:** Category & Region dropdowns for drill-down analysis

**Visual Elements:**
- Light gray background (#F5F5F5)
- White cards with subtle shadows
- Blue/green color scheme for consistency
- Interactive filters for dynamic exploration
- Title: "Retail Sales Dashboard — Prabhu Charan"

### **Add Your Screenshots**

To showcase your project results, add screenshots to the `docs/screenshots/` folder:

```bash
# Screenshots to add:
screenshots/
├── 01_bigquery_table.png          # Table preview after data load
├── 02_bigquery_kpi_query.png      # KPI validation query results
├── 03_bigquery_monthly_trend.png  # Monthly sales trend query
├── 04_bigquery_region_perf.png    # Regional performance query
├── 05_looker_dashboard_full.png   # Complete dashboard view
├── 06_looker_scorecards.png       # Top KPI scorecards
├── 07_looker_monthly_chart.png    # Monthly sales trend visualization
├── 08_looker_region_chart.png     # Region performance bar chart
└── 09_looker_products_table.png   # Top products data table
```

**How to Take Screenshots:**

1. **BigQuery Table:**
   - Go to BigQuery Console → Dataset `retail_ds` → Table `sales`
   - Click **Preview** tab
   - Take screenshot showing columns and sample rows

2. **BigQuery Query Results:**
   - Run the KPI query in BigQuery Editor
   - Click **Results** after execution
   - Screenshot the results table

3. **Looker Studio Dashboard:**
   - Open your dashboard in Looker Studio
   - Take full-page screenshot (F12 Developer Tools recommended)
   - Take individual component screenshots for key visuals

**To embed screenshots in README:**

Once you have screenshots, add them with markdown syntax:

```markdown
![BigQuery Table Preview](./screenshots/01_bigquery_table.png)
![Looker Dashboard](./screenshots/05_looker_dashboard_full.png)
```

---

## �🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| ❌ **Docker: invalid reference format** | Run `docker run` as **single line** (no line breaks) on Windows |
| ❌ **PyMySQL "cryptography required"** | `pip install cryptography` or use `mysql-connector-python` |
| ❌ **MySQL secure_file_priv error** | Use Python loader (this project does) instead of `LOAD DATA` |
| ❌ **BigQuery "no billing account"** | Use **Sandbox** (always free for new projects) |
| ❌ **CSV newline/encoding issues** | Run `make_bq_csv.py` sanitizer before uploading |
| ❌ **Connection timeout to MySQL** | Check: `docker ps`, restart container, verify credentials |
| ❌ **Data not showing in Looker** | Verify dataset location = **US**, refresh data source |

---

## 📦 Deliverables Checklist

- [x] **ETL Scripts:** `load_to_mysql.py`, `etl_transform.py`, `make_bq_csv.py`
- [x] **Data Files:** `sales.csv`, `clean_sales_transformed.csv`, `clean_sales_transformed_bq.csv`
- [x] **SQL Queries:** `bigquery/queries.sql`
- [x] **Documentation:** This README + comments in code
- [x] **Dashboard:** Looker Studio report with filters & KPIs
- [x] **Screenshots:** (add to `docs/screenshots/`)

---

## 🎓 Learning Outcomes

This project demonstrates:

✅ **Data Engineering Fundamentals**
- ETL pipeline design & best practices
- Data quality & validation techniques
- SQL optimization for analytics

✅ **Cloud Technologies**
- BigQuery Sandbox (free tier)
- GCP IAM & authentication
- Scalable data warehouse concepts

✅ **Tools & Languages**
- Python data processing (pandas)
- Docker containerization
- SQL query optimization
- Looker Studio visualization

✅ **Soft Skills**
- Documentation & communication
- Project portfolio presentation
- End-to-end solution delivery

---

## 📚 References

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Looker Studio Help Center](https://support.google.com/looker-studio)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [MySQL Docker Hub](https://hub.docker.com/_/mysql)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)

---

## 📄 License & Attribution

- **Data:** Synthetic retail dataset for educational purposes
- **Project:** Open source portfolio project
- **Author:** [Prabhu Charan](#)
- **Created:** November 2025

© 2025 Prabhu Charan. All rights reserved.

---

## 🤝 Contributing

Found a bug? Have an improvement idea?

1. Fork the repo
2. Create feature branch: `git checkout -b feature/improvement`
3. Commit changes: `git commit -m "Add improvement"`
4. Push: `git push origin feature/improvement`
5. Open Pull Request

---

## 💡 Future Enhancements

- [ ] Data quality tests with Great Expectations
- [ ] Automated daily pipeline with Cloud Scheduler
- [ ] Real-time streaming with Pub/Sub
- [ ] ML model for sales forecasting
- [ ] Cost analysis & optimization
- [ ] Advanced filters & drill-down in Looker

---

<div align="center">

**⭐ If this project helped you, please consider giving it a star!**

Built with ❤️ using Python, BigQuery, and Looker Studio

</div>
