from app.db.weaviate.weaviate_client import get_client
import weaviate.classes.config as wc

def create_schema(client, name, properties):
    client.collections.create(
        name=name,
        properties=properties,
    )
    print(f"Created: {name}")

def create_user_profile_schema(client):
    """
    Create schema for WeaviateUserProfile model.
    Main vectorization will be on profile_text_for_embedding field.
    """
    properties = [
        wc.Property(name="user_id", data_type=wc.DataType.TEXT),
        wc.Property(name="github_username", data_type=wc.DataType.TEXT),
        wc.Property(name="display_name", data_type=wc.DataType.TEXT),
        wc.Property(name="bio", data_type=wc.DataType.TEXT),
        wc.Property(name="location", data_type=wc.DataType.TEXT),
        wc.Property(name="repositories", data_type=wc.DataType.TEXT),  # JSON string
        wc.Property(name="languages", data_type=wc.DataType.TEXT_ARRAY),
        wc.Property(name="topics", data_type=wc.DataType.TEXT_ARRAY),
        wc.Property(name="followers_count", data_type=wc.DataType.INT),
        wc.Property(name="following_count", data_type=wc.DataType.INT),
        wc.Property(name="total_stars_received", data_type=wc.DataType.INT),
        wc.Property(name="total_forks", data_type=wc.DataType.INT),
        wc.Property(name="profile_text_for_embedding", data_type=wc.DataType.TEXT),
        wc.Property(name="last_updated", data_type=wc.DataType.DATE),
    ]
    create_schema(client, "weaviate_user_profile", properties)

def create_all_schemas():
    """
    Create only the user profile schema as per the updated model structure.
    """
    client = get_client()
    create_user_profile_schema(client)
    client.close()
    print("✅ User profile schema created successfully.")
