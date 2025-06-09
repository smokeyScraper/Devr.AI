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
            "userId": "095a5ff0-545a-48ff-83ad-2ea3566f5674",
            "message": "Hi, can you explain the code chunk with ID 095a5ff0-545a-48ff-83ad-2ea3566f5674?",
            "timestamp": "2023-01-01T12:00:00Z"
        },
        {
            "userId": "b6bbdb5a-deb1-43c7-bf99-b9f88e4af1ed",
            "message": "What does the function in Go do?",
            "timestamp": "2023-01-01T12:01:00Z"
        },
        {
            "userId": "1f787967-316c-4232-b251-64bcf8e3251b",
            "message": "Can you summarize the module in C++?",
            "timestamp": "2023-01-01T12:02:00Z"
        },
        {
            "userId": "233530b2-d89f-416d-a73c-40b4ebb33c50",
            "message": "What is the purpose of the import in this C++ chunk?",
            "timestamp": "2023-01-01T12:03:00Z"
        },
        {
            "userId": "b3103899-d683-422a-9072-2ad26050d8f5",
            "message": "Is this function in C++ recursive?",
            "timestamp": "2023-01-01T12:04:00Z"
        },
        {
            "userId": "28ea68b7-1f26-472c-b568-319e1d41732b",
            "message": "What does this module handle in the codebase?",
            "timestamp": "2023-01-01T12:05:00Z"
        },
        {
            "userId": "1cb8ccc0-db27-49c5-8dff-8d535d5a37d3",
            "message": "Can you explain the logic in this C++ module?",
            "timestamp": "2023-01-01T12:06:00Z"
        },
        {
            "userId": "9edaae8a-3d6c-47c1-8777-ff0b0002b85a",
            "message": "What does the import statement in Java do?",
            "timestamp": "2023-01-01T12:07:00Z"
        },
        {
            "userId": "d1927881-d0e7-4df3-a97a-18521db08ff4",
            "message": "Is this a comment or code in Rust?",
            "timestamp": "2023-01-01T12:08:00Z"
        },
        {
            "userId": "fdda052a-ca4f-40b5-ae99-a711e2161d85",
            "message": "What is the output of this JavaScript function?",
            "timestamp": "2023-01-01T12:09:00Z"
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
