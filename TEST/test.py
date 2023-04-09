import argparse
from google.cloud import bigquery
from google.oauth2 import service_account

parser = argparse.ArgumentParser(description="main")
parser.add_argument('-p', '--path', help="Path",action="store", required=True)


# parse the arguments
args = parser.parse_args()
# deployment_file= args.deployment_file
#GOOGLE_CLOUD_STORAGE_CREDENTIALS = args.path

json_file=json.load(args.path)

credentials = service_account.Credentials.from_service_account_file(json_file)

project_id = 'bigquery-demo-377718'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
   SELECT *
   FROM dataset_py.table_py
   LIMIT 1000 """)

results = query_job.result() # Wait for the job to complete.

# parser = argparse.ArgumentParser(description="main")
# parser.add_argument('-p', '--path', help="Path",action="store", required=True)


# # parse the arguments
# args = parser.parse_args()
# # deployment_file= args.deployment_file
# GOOGLE_CLOUD_STORAGE_CREDENTIALS = args.path

# client=bigquery.Client.from_service_account_json(GOOGLE_CLOUD_STORAGE_CREDENTIALS)
# dataset_id='bigquery-demo-377718.dataset_github'
# dataset=bigquery.Dataset(dataset_id)
# dataset.location="US"
# dataset.description="dataset from python"

# dataset_ref=client.create_dataset(dataset,timeout=30)

# print("created dataset {}.{}".format(client.project, dataset_ref.dataset_id))
