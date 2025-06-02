import os
import weaviate
from weaviate.classes.init import Auth

# Best practice: store your credentials in environment variables
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]
weaviate_grpc_host = os.environ.get("WEAVIATE_GRPC_HOST")  # Default to localhost if not set
weaviate_grpc_port = os.environ.get("WEAVIATE_GRPC_PORT")  # Fallback to localhost if not set

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
    skip_init_checks=True,
)


def get_client():
    return client
