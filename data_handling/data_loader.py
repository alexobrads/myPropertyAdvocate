from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError
import requests

elasticsearch_url = "http://localhost:9200"
es = Elasticsearch([elasticsearch_url])
index_name = 'property-test-2'


def load_to_elastic(data):
    documents = [
        {
            '_op_type': 'index',
            '_index': index_name,
            '_source': doc
        }
        for doc in data
    ]

    # Use the bulk API to index the documents
    try:
        success, failed = bulk(es, documents)
        print(f"Successful indexing: {success}")
        print(f"Failed indexing: {failed}")
    except BulkIndexError as e:
        print(f"Error: {e}")
        for error in e.errors:
            print(f"Failed document: {error}")


def create_geo_index():
    mapping = {
        "properties": {
            "geoLocation": {
                "type": "geo_point"
            }
        }
    }

    # Create the index with the specified mapping
    es.indices.create(index=index_name, body={"mappings": mapping}, ignore=400)
