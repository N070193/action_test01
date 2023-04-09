import argparse
from google.cloud import bigquery

parser = argparse.ArgumentParser(description="main")
parser.add_argument('-p', '--path', help="Path",action="store", required=True)


# parse the arguments
args = parser.parse_args()
# deployment_file= args.deployment_file
GOOGLE_CLOUD_STORAGE_CREDENTIALS = args.path

client=bigquery.Client.from_service_account_json(GOOGLE_CLOUD_STORAGE_CREDENTIALS)
dataset_id='bigquery-demo-377718.dataset_github'
dataset=bigquery.Dataset(dataset_id)
dataset.location="US"
dataset.description="dataset from python"

dataset_ref=client.create_dataset(dataset,timeout=30)

print("created dataset {}.{}".format(client.project, dataset_ref.dataset_id))
