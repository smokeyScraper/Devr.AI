from app.db.weaviate.weaviate_client import get_client
import weaviate.classes.config as wc

def create_user_profile_schema(client):
    client.collections.create(
        name="weaviate_user_profile",
        properties=[
            wc.Property(name="supabaseUserId", data_type=wc.DataType.TEXT),
            wc.Property(name="profileSummary", data_type=wc.DataType.TEXT),
            wc.Property(name="primaryLanguages", data_type=wc.DataType.TEXT_ARRAY),
            wc.Property(name="expertiseAreas", data_type=wc.DataType.TEXT_ARRAY),
        ],
        vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
        generative_config=wc.Configure.Generative.openai()
    )
    print("Created: weaviate_user_profile")


def create_code_chunk_schema(client):
    client.collections.create(
        name="weaviate_code_chunk",
        properties=[
            wc.Property(name="supabaseChunkId", data_type=wc.DataType.TEXT),
            wc.Property(name="codeContent", data_type=wc.DataType.TEXT),
            wc.Property(name="language", data_type=wc.DataType.TEXT),
            wc.Property(name="functionNames", data_type=wc.DataType.TEXT_ARRAY),
        ],
        vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
        generative_config=wc.Configure.Generative.openai()
    )
    print("Created: weaviate_code_chunk")

def create_interaction_schema(client):
    client.collections.create(
        name="weaviate_interaction",
        properties=[
            wc.Property(name="supabaseInteractionId", data_type=wc.DataType.TEXT),
            wc.Property(name="conversationSummary", data_type=wc.DataType.TEXT),
            wc.Property(name="platform", data_type=wc.DataType.TEXT),
            wc.Property(name="topics", data_type=wc.DataType.TEXT_ARRAY),
        ],
        vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
        generative_config=wc.Configure.Generative.openai()
    )
    print("Created: weaviate_interaction")

def create_all_schemas():
    client = get_client()
    existing_collections = client.collections.list_all()
    if "Weaviate_code_chunk" not in existing_collections:
        create_code_chunk_schema(client)
    if "Weaviate_interaction" not in existing_collections:
        create_interaction_schema(client)
    if "Weaviate_user_profile" not in existing_collections:
        create_user_profile_schema(client)
    print("✅ All schemas ensured.")
