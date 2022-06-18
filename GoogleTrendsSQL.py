from google.cloud import bigquery
import pandas

client = bigquery.Client()

datasetRef = client.dataset('google_trends', project='bigquery-public-data')

dataset = client.get_dataset(datasetRef)

tables = [t.table_id for t in list(client.list_tables(dataset))]

print(tables)


table_ref = datasetRef.table('top_rising_terms')

table = client.get_table(table_ref)

for x in table.schema:
    print(x)

print(client.list_rows(table, max_results=5).to_dataframe()['week'])


query = """
SELECT term, COUNT(1) AS num_days
FROM `bigquery-public-data.google_trends.top_rising_terms`    
WHERE EXTRACT(MONTH from week)>5 AND EXTRACT(YEAR from week)>=2022
GROUP BY term
ORDER BY num_days DESC
"""

query_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)

query = client.query(query, job_config=query_config)

queryData = query.to_dataframe()

queryData.to_csv("./topterms.csv")

print(queryData.head())



