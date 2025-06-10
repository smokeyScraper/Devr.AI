from app.db.weaviate.weaviate_client import get_client
import weaviate.classes.config as wc
def create_schema(client, name, properties):
    client.collections.create(
        name=name,
        properties=properties,
        vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
        generative_config=wc.Configure.Generative.openai()
    )
    print(f"Created: {name}")
def create_user_profile_schema(client):
    properties = [
        wc.Property(name="supabaseUserId", data_type=wc.DataType.TEXT),
        wc.Property(name="profileSummary", data_type=wc.DataType.TEXT),
        wc.Property(name="primaryLanguages", data_type=wc.DataType.TEXT_ARRAY),
        wc.Property(name="expertiseAreas", data_type=wc.DataType.TEXT_ARRAY),
    ]
    create_schema(client, "weaviate_user_profile", properties)


def create_code_chunk_schema(client):
    properties = [
        wc.Property(name="supabaseChunkId", data_type=wc.DataType.TEXT),
        wc.Property(name="codeContent", data_type=wc.DataType.TEXT),
        wc.Property(name="language", data_type=wc.DataType.TEXT),
        wc.Property(name="functionNames", data_type=wc.DataType.TEXT_ARRAY),
    ]
    create_schema(client, "weaviate_code_chunk", properties)

def create_interaction_schema(client):
    properties = [
        wc.Property(name="supabaseInteractionId", data_type=wc.DataType.TEXT),
        wc.Property(name="conversationSummary", data_type=wc.DataType.TEXT),
        wc.Property(name="platform", data_type=wc.DataType.TEXT),
        wc.Property(name="topics", data_type=wc.DataType.TEXT_ARRAY),
    ]
    create_schema(client, "weaviate_interaction", properties)

def create_all_schemas():
    client = get_client()
    existing_collections = client.collections.list_all()
    if "weaviate_code_chunk" not in existing_collections:
        create_code_chunk_schema(client)
    if "weaviate_interaction" not in existing_collections:
        create_interaction_schema(client)
    if "weaviate_user_profile" not in existing_collections:
        create_user_profile_schema(client)
    print("✅ All schemas ensured.")
