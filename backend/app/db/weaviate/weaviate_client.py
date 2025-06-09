import os
import weaviate

# Connect to Weaviate Cloud
client = weaviate.connect_to_local()


def get_client():
    return client
