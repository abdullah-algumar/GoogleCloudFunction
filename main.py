import json
from google.cloud import bigquery

def bbc_news(request):
    client = bigquery.Client()
    query_job = client.query("""
        SELECT title
        FROM `bigquery-public-data.bbc_news.fulltext`
        WHERE category = 'tech'
        LIMIT 50
    """)
    
    results = query_job.result()
    titles = [row.title for row in results]
    
    response = {
        'titles': titles
    }
    
    return json.dumps(response)