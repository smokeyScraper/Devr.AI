from app.db.weaviate.weaviate_client import get_client


async def populate_Weaviate_code_chunk(client):
    code_chunks = [
        {
            "supabaseChunkId": "095a5ff0-545a-48ff-83ad-2ea3566f5674",
            "codeContent": (
                "Maybe evening clearly trial want whose far. Sound life away senior difficult put. "
                "Whose source hand so add Mr."
            ),
            "language": "C++",
            "functionNames": ["comment"]
        },
        {
            "supabaseChunkId": "b6bbdb5a-deb1-43c7-bf99-b9f88e4af1ed",
            "codeContent": (
                "Break doctor Mr home he we recent. Industry score choice increase between majority impact.\n"
                "Real describe know. Talk between rate name within."
            ),
            "language": "Go",
            "functionNames": ["function"]
        },
        {
            "supabaseChunkId": "1f787967-316c-4232-b251-64bcf8e3251b",
            "codeContent": (
                "Music sometimes body term. Address so draw food.\n"
                "Appear score moment second live. Message board mean war analysis situation."
            ),
            "language": "C++",
            "functionNames": ["module"]
        },
        {
            "supabaseChunkId": "233530b2-d89f-416d-a73c-40b4ebb33c50",
            "codeContent": (
                "Result Democrat later direction fund law indeed. Fine fine effort well.\n"
                "Before be it season. Speech news only form business. Them wait institution trouble anything explain."
            ),
            "language": "C++",
            "functionNames": ["import"]
        },
        {
            "supabaseChunkId": "b3103899-d683-422a-9072-2ad26050d8f5",
            "codeContent": (
                "Ahead event several TV go. Thank not husband center. Begin most heavy. "
                "Game have return since nothing be apply."
            ),
            "language": "C++",
            "functionNames": ["function"]
        },
        {
            "supabaseChunkId": "28ea68b7-1f26-472c-b568-319e1d41732b",
            "codeContent": (
                "War should share face build. Section compare herself region matter street south.\n"
                "Technology amount affect TV television office. Identify policy face if whom commercial way."
            ),
            "language": "C++",
            "functionNames": ["module"]
        },
        {
            "supabaseChunkId": "1cb8ccc0-db27-49c5-8dff-8d535d5a37d3",
            "codeContent": (
                "Concern significant management senior. Large under north play person ten physical character.\n"
                "Kind field ever argue medical financial later. Hard expert popular within."
            ),
            "language": "C++",
            "functionNames": ["module"]
        },
        {
            "supabaseChunkId": "9edaae8a-3d6c-47c1-8777-ff0b0002b85a",
            "codeContent": (
                "Position always remain yard model particular hair. Hold simple quickly appear piece."
            ),
            "language": "Java",
            "functionNames": ["import"]
        },
        {
            "supabaseChunkId": "d1927881-d0e7-4df3-a97a-18521db08ff4",
            "codeContent": (
                "Gun guy Congress degree way main difficult. Choice fast small medical. Strong this also from short.\n"
                "Story side speak close. Analysis hair rest wide particular sell."
            ),
            "language": "Rust",
            "functionNames": ["comment"]
        },
        {
            "supabaseChunkId": "fdda052a-ca4f-40b5-ae99-a711e2161d85",
            "codeContent": (
                "Expect several evening town. Store begin treat stage. Us increase how hear history bank.\n"
                "Five between research. Social case expert stop receive catch."
            ),
            "language": "JavaScript",
            "functionNames": ["function"]
        }
    ]
    try:
        with client.batch.dynamic() as batch:
            for chunk in code_chunks:
                batch.add_object(
                    collection="weaviate_code_chunk",
                    properties=chunk
                )
        print("Populated: weaviate_code_chunk with sample data.")
    except Exception as e:
        print(f"Error populating weaviate_code_chunk: {e}")
async def populate_Weaviate_interaction(client):
    interactions = [
        {
            "supabaseInteractionId": "095a5ff0-545a-48ff-83ad-2ea3566f5674",
            "conversationSummary": "User asked about C++ code chunk.",
            "platform": "web",
            "topics": ["C++", "Code Chunk"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "b6bbdb5a-deb1-43c7-bf99-b9f88e4af1ed",
            "conversationSummary": "User inquired about Go function.",
            "platform": "mobile",
            "topics": ["Go", "Function"],
            "embedding": [0.4, 0.5, 0.6]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "1f787967-316c-4232-b251-64bcf8e3251b",
            "conversationSummary": "User asked for a summary of the C++ module.",
            "platform": "web",
            "topics": ["C++", "Module"],
            "embedding": [0.7, 0.8, 0.9]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "233530b2-d89f-416d-a73c-40b4ebb33c50",
            "conversationSummary": "User inquired about the import statement in C++.",
            "platform": "web",
            "topics": ["C++", "Import"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "b3103899-d683-422a-9072-2ad26050d8f5",
            "conversationSummary": "User asked if this function in C++ is recursive.",
            "platform": "web",
            "topics": ["C++", "Function", "Recursion"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "28ea68b7-1f26-472c-b568-319e1d41732b",
            "conversationSummary": "User inquired about what this module handles in the codebase.",
            "platform": "web",
            "topics": ["C++", "Module"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "1cb8ccc0-db27-49c5-8dff-8d535d5a37d3",
            "conversationSummary": "User asked about the logic in this C++ module.",
            "platform": "web",
            "topics": ["C++", "Module"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "9edaae8a-3d6c-47c1-8777-ff0b0002b85a",
            "conversationSummary": "User inquired about the import statement in Java.",
            "platform": "web",
            "topics": ["Java", "Import"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "d1927881-d0e7-4df3-a97a-18521db08ff4",
            "conversationSummary": "User asked if this is a comment or code in Rust.",
            "platform": "web",
            "topics": ["Rust", "Comment", "Code"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        },
        {
            "supabaseInteractionId": "fdda052a-ca4f-40b5-ae99-a711e2161d85",
            "conversationSummary": "User inquired about the output of this JavaScript function.",
            "platform": "web",
            "topics": ["JavaScript", "Function", "Output"],
            "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
        }
    ]
    try:
        with client.batch.dynamic() as batch:
            for interaction in interactions:
                batch.add_object(
                    collection="weaviate_interaction",
                    properties=interaction
                )
        print("Populated: weaviate_interaction with sample data.")
    except Exception as e:
        print(f"Error populating weaviate_interaction: {e}")
async def populate_Weaviate_user_profile(client):
    user_profiles = [
        {
            "supabaseUserId": "095a5ff0-545a-48ff-83ad-2ea3566f5674",
            "profileSummary": "Experienced C++ developer with a focus on performance optimization.",
            "primaryLanguages": ["C++", "Python"],
            "expertiseAreas": ["Performance Tuning", "Concurrency"]
        },
        {
            "supabaseUserId": "b6bbdb5a-deb1-43c7-bf99-b9f88e4af1ed",
            "profileSummary": "Go developer with a passion for building scalable systems.",
            "primaryLanguages": ["Go", "JavaScript"],
            "expertiseAreas": ["Microservices", "Cloud Computing"]
        },
        {
            "supabaseUserId": "1f787967-316c-4232-b251-64bcf8e3251b",
            "profileSummary": "C++ module developer with experience in embedded systems.",
            "primaryLanguages": ["C++", "Rust"],
            "expertiseAreas": ["Embedded Systems", "Real-time Processing"]
        },
        {
            "supabaseUserId": "233530b2-d89f-416d-a73c-40b4ebb33c50",
            "profileSummary": "C++ developer with a knack for clean imports and modular code.",
            "primaryLanguages": ["C++"],
            "expertiseAreas": ["Code Organization", "Modularity"]
        },
        {
            "supabaseUserId": "b3103899-d683-422a-9072-2ad26050d8f5",
            "profileSummary": "C++ enthusiast focusing on algorithmic challenges.",
            "primaryLanguages": ["C++"],
            "expertiseAreas": ["Algorithms", "Problem Solving"]
        },
        {
            "supabaseUserId": "28ea68b7-1f26-472c-b568-319e1d41732b",
            "profileSummary": "C++ developer with experience in system architecture.",
            "primaryLanguages": ["C++"],
            "expertiseAreas": ["System Design", "Architecture"]
        },
        {
            "supabaseUserId": "1cb8ccc0-db27-49c5-8dff-8d535d5a37d3",
            "profileSummary": "C++ developer passionate about medical technology.",
            "primaryLanguages": ["C++"],
            "expertiseAreas": ["Medical Tech", "Data Analysis"]
        },
        {
            "supabaseUserId": "9edaae8a-3d6c-47c1-8777-ff0b0002b85a",
            "profileSummary": "Java developer with a focus on enterprise solutions.",
            "primaryLanguages": ["Java"],
            "expertiseAreas": ["Enterprise Software", "APIs"]
        },
        {
            "supabaseUserId": "d1927881-d0e7-4df3-a97a-18521db08ff4",
            "profileSummary": "Rustacean interested in safe and fast code.",
            "primaryLanguages": ["Rust"],
            "expertiseAreas": ["Memory Safety", "Performance"]
        },
        {
            "supabaseUserId": "fdda052a-ca4f-40b5-ae99-a711e2161d85",
            "profileSummary": "JavaScript developer with a love for UI/UX.",
            "primaryLanguages": ["JavaScript"],
            "expertiseAreas": ["Frontend", "User Experience"]
        }
    ]
    try:
        with client.batch.dynamic() as batch:
            for profile in user_profiles:
                batch.add_object(
                    collection="weaviate_user_profile",
                    properties=profile
                )
        print("Populated: weaviate_user_profile with sample data.")
    except Exception as e:
        print(f"Error populating weaviate_user_profile: {e}")
async def populate_all_collections():
    client = get_client()
    print("Populating Weaviate collections with sample data...")
    await populate_Weaviate_code_chunk(client)
    await populate_Weaviate_interaction(client)
    await populate_Weaviate_user_profile(client)
    print("✅ All collections populated with sample data.")
