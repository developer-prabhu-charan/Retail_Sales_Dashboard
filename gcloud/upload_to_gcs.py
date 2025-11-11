# gcloud/upload_to_gcs.py
from google.cloud import storage
import os

# === CONFIGURE THIS ===
BUCKET_NAME = "retail-project-prabh-2025-bucket"   # <-- update to your bucket name
LOCAL_PATH = os.path.join("data", "clean_sales_transformed.csv")  # relative to this file
DEST_BLOB = "clean_sales_transformed.csv"
# ======================

def upload_file(bucket_name, local_path, dest_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{bucket_name}/{dest_blob}")

if __name__ == "__main__":
    if not os.path.exists(LOCAL_PATH):
        raise SystemExit(f"Local file not found: {LOCAL_PATH}")
    upload_file(BUCKET_NAME, LOCAL_PATH, DEST_BLOB)
