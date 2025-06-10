import weaviate

# Connect to local Weaviate instance
client = weaviate.connect_to_local()


def get_client():
    return client
