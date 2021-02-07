from google.cloud import bigquery

# create bigquery clienet
client = bigquery.Client()

# set dataset
dataset_id = 'my_dataset'
dataset_ref = client.dataset(dataset_id)

# define BigQuery laod job config
job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.skip_leading_rows = 1
job_config.source_format = bigquery.SourceFormat.CSV
uri = "gs://mybucket/mydata.csv"

# call BigQuery load job
load_job = client.load_table_from_uri(
    uri, dataset_ref.table("mytable"), job_config=job_config)  # API request
print("Starting job {}".format(load_job.job_id))

# wait for load job to complete
load_job.result()  # Waits for table load to complete.
print("Job finished.")
