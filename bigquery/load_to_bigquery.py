# bigquery/load_to_bigquery.py
from google.cloud import bigquery

# === CONFIGURE ===
PROJECT_ID = "[sales-data-analysis-477907"            # <-- update
DATASET = "retail_ds"
TABLE = "sales"
GCS_URI = "gs://retail-project-prabh-2025-bucket/clean_sales_transformed.csv"  # update if needed
# ==================

client = bigquery.Client(project=PROJECT_ID)
dataset_ref = client.dataset(DATASET)
table_ref = dataset_ref.table(TABLE)

job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

print("Starting BigQuery load job...")
load_job = client.load_table_from_uri(GCS_URI, table_ref, job_config=job_config)
load_job.result()  # wait for job to finish
table = client.get_table(table_ref)
print(f"Loaded {table.num_rows} rows into {PROJECT_ID}.{DATASET}.{TABLE}")
