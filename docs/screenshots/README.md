# 📸 Project Screenshots

This folder contains screenshots showcasing the Retail Sales Analytics Pipeline at each stage.

## Screenshot Checklist

Add the following screenshots to this folder:

### BigQuery Screenshots

- [ ] **01_bigquery_table.png** - Table preview showing all columns and sample data
  - Navigate to: BigQuery Console → retail_ds → sales table → Preview tab
  - Show: Column names, data types, sample rows

- [ ] **02_bigquery_kpi_query.png** - KPI validation query results
  - Query: Core KPIs (total_sales, total_profit, avg_profit_margin)
  - Show: Results table with metrics

- [ ] **03_bigquery_monthly_trend.png** - Monthly sales trend query
  - Query: OrderYearMonth vs SUM(Sales)
  - Show: Results sorted by OrderYearMonth

- [ ] **04_bigquery_region_perf.png** - Regional performance query
  - Query: Region vs SUM(Sales), SUM(Profit)
  - Show: Results sorted by sales descending

### Looker Studio Screenshots

- [ ] **05_looker_dashboard_full.png** - Complete dashboard overview
  - Show: All visualizations, filters, title
  - Resolution: 1920x1080 or higher for clarity

- [ ] **06_looker_scorecards.png** - KPI scorecards section
  - Show: Total Sales, Total Profit, Avg Profit Margin cards
  - Highlight: Color scheme and styling

- [ ] **07_looker_monthly_chart.png** - Monthly sales trend line chart
  - Show: Time series visualization
  - Highlight: Trend patterns

- [ ] **08_looker_region_chart.png** - Regional performance bar chart
  - Show: Region comparison
  - Highlight: Top performers

- [ ] **09_looker_products_table.png** - Top products data table
  - Show: ProductName, SUM(Sales), SUM(Quantity)
  - Highlight: Top 10 products

## How to Take Screenshots

### BigQuery Screenshots

1. **Login to BigQuery:** https://console.cloud.google.com/bigquery
2. **Navigate to Table:**
   - Project: `sales-data-analysis-477907`
   - Dataset: `retail_ds`
   - Table: `sales`
3. **Take Screenshot:** Use Print Screen or browser dev tools (F12)
4. **Save:** Use `Shift + S` in Windows or browser screenshot tool

### Looker Studio Screenshots

1. **Open Dashboard:** https://lookerstudio.google.com/
2. **View Your Report:** Find your "Retail Sales Dashboard"
3. **Full Page Screenshot:**
   - Press `F12` → DevTools
   - Press `Ctrl + Shift + P` → "Capture screenshot"
   - Or use Windows Snipping Tool (`Win + Shift + S`)
4. **Component Screenshots:**
   - Scroll to each section
   - Take individual screenshots for clarity
5. **Save:** PNG or JPG format

## File Naming Convention

Use format: `##_description.png`
- `##` = Sequential number (01, 02, 03...)
- `description` = Brief description in lowercase with underscores

Examples:
- ✅ `01_bigquery_table.png`
- ✅ `05_looker_dashboard_full.png`
- ❌ `screenshot.png` (too vague)
- ❌ `BQ_Screenshot.png` (inconsistent naming)

## Image Quality Guidelines

- **Resolution:** Minimum 1280x720, Recommended 1920x1080
- **Format:** PNG (preferred) or JPG
- **File Size:** Compress if > 2MB (use TinyPNG or similar)
- **Content:** Include full UI context, not just cropped sections
- **Text:** Ensure text is readable at normal zoom

## Quick Embedding in README

Once screenshots are added, embed them in the main README with:

```markdown
### BigQuery Table Preview

![BigQuery Table](./screenshots/01_bigquery_table.png)

### Looker Studio Dashboard

![Looker Dashboard](./screenshots/05_looker_dashboard_full.png)
```

## Tools for Screenshots

| Tool | Platform | Best For |
|------|----------|----------|
| Windows Snipping Tool | Windows | Quick screenshots |
| Greenshot | Windows | Advanced annotations |
| Lightshot | Cross-platform | Easy sharing |
| Chrome DevTools | Browser | Web app screenshots |
| Print Screen | All | Simple capture |

---

Once you add screenshots, update this checklist and they'll automatically appear in the README gallery!
