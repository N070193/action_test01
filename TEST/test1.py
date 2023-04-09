from google.cloud import bigquery
from google.oauth2 import service_account

parser = argparse.ArgumentParser(description="main")
parser.add_argument('-p', '--path', help="Path",action="store", required=True)


# parse the arguments
args = parser.parse_args()
# deployment_file= args.deployment_file
GOOGLE_CLOUD_STORAGE_CREDENTIALS = args.path

try:
    credentials = service_account.Credentials.from_service_account_file(GOOGLE_CLOUD_STORAGE_CREDENTIALS)
    project_id = 'bigquery-demo-377718'
    client = bigquery.Client(credentials= credentials,project=project_id)
    query_job = client.query("""
       SELECT *
       FROM dataset_py.table_py
       LIMIT 1000 """)
    results = query_job.result() # Wait for the job to complete.

except OSError as exc:
    if exc.errno == 36:
        handle_filename_too_long()
    else:
        raise  # re-raise previously caught exception
