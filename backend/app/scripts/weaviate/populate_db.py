import json
from datetime import datetime
from app.db.weaviate.weaviate_client import get_client

def populate_weaviate_user_profile(client):
    """
    Populate WeaviateUserProfile collection with sample data matching the model structure.
    """
    current_time = datetime.now().astimezone()

    user_profiles = [
        {
            "user_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
            "github_username": "jane-dev",
            "display_name": "Jane Developer",
            "bio": "Creator of innovative open-source tools. Full-stack developer with a passion for Rust and WebAssembly.",
            "location": "Berlin, Germany",
            "repositories": json.dumps([
                {
                    "name": "rust-web-framework",
                    "description": "A high-performance web framework for Rust.",
                    "url": "https://github.com/jane-dev/rust-web-framework",
                    "languages": ["Rust", "TOML"],
                    "stars": 2500,
                    "forks": 400
                },
                {
                    "name": "data-viz-lib",
                    "description": "A declarative data visualization library for JavaScript.",
                    "url": "https://github.com/jane-dev/data-viz-lib",
                    "languages": ["JavaScript", "TypeScript"],
                    "stars": 1200,
                    "forks": 150
                }
            ]),
            "languages": ["Rust", "JavaScript", "TypeScript", "TOML"],
            "topics": ["rust", "webdev", "performance", "framework", "data-visualization", "d3", "charts"],
            "followers_count": 1800,
            "following_count": 250,
            "total_stars_received": 3700,
            "total_forks": 550,
            "profile_text_for_embedding": "Jane Developer, Creator of innovative open-source tools. Full-stack developer with a passion for Rust and WebAssembly. Repositories: rust-web-framework, A high-performance web framework for Rust. data-viz-lib, A declarative data visualization library for JavaScript. Languages: Rust, JavaScript, TypeScript. Topics: rust, webdev, performance, data-visualization.",
            "last_updated": current_time
        },
        {
            "user_id": "b2c3d4e5-f6g7-8901-2345-678901bcdefg",
            "github_username": "python-ninja",
            "display_name": "Alex Chen",
            "bio": "Python enthusiast and machine learning researcher. Building the future of AI.",
            "location": "San Francisco, CA",
            "repositories": json.dumps([
                {
                    "name": "ml-toolkit",
                    "description": "A comprehensive machine learning toolkit for Python.",
                    "url": "https://github.com/python-ninja/ml-toolkit",
                    "languages": ["Python", "Jupyter Notebook"],
                    "stars": 3200,
                    "forks": 580
                },
                {
                    "name": "data-pipeline",
                    "description": "Scalable data processing pipeline for big data applications.",
                    "url": "https://github.com/python-ninja/data-pipeline",
                    "languages": ["Python", "SQL"],
                    "stars": 1800,
                    "forks": 320
                }
            ]),
            "languages": ["Python", "SQL", "Jupyter Notebook"],
            "topics": ["machine-learning", "ai", "data-science", "python", "big-data"],
            "followers_count": 2400,
            "following_count": 180,
            "total_stars_received": 5000,
            "total_forks": 900,
            "profile_text_for_embedding": "Alex Chen, Python enthusiast and machine learning researcher. Building the future of AI. Repositories: ml-toolkit, A comprehensive machine learning toolkit for Python. data-pipeline, Scalable data processing pipeline for big data applications. Languages: Python, SQL. Topics: machine-learning, ai, data-science, python.",
            "last_updated": current_time
        },
        {
            "user_id": "c3d4e5f6-g7h8-9012-3456-789012cdefgh",
            "github_username": "go-developer",
            "display_name": "Sam Rodriguez",
            "bio": "Cloud infrastructure engineer specializing in Go and Kubernetes.",
            "location": "Austin, TX",
            "repositories": json.dumps([
                {
                    "name": "k8s-operator",
                    "description": "Custom Kubernetes operator for managing microservices.",
                    "url": "https://github.com/go-developer/k8s-operator",
                    "languages": ["Go", "Dockerfile"],
                    "stars": 1500,
                    "forks": 280
                }
            ]),
            "languages": ["Go", "Dockerfile"],
            "topics": ["kubernetes", "microservices", "cloud", "devops", "api"],
            "followers_count": 890,
            "following_count": 120,
            "total_stars_received": 1500,
            "total_forks": 280,
            "profile_text_for_embedding": "Sam Rodriguez, Cloud infrastructure engineer specializing in Go and Kubernetes. Repositories: k8s-operator, Custom Kubernetes operator for managing microservices. Languages: Go, Dockerfile. Topics: kubernetes, microservices, cloud, devops.",
            "last_updated": current_time
        },
        {
            "user_id": "d4e5f6g7-h8i9-0123-4567-890123defghi",
            "github_username": "frontend-wizard",
            "display_name": "Emily Johnson",
            "bio": "Frontend developer creating beautiful and accessible web experiences.",
            "location": "New York, NY",
            "repositories": json.dumps([
                {
                    "name": "react-components",
                    "description": "Reusable React component library with TypeScript.",
                    "url": "https://github.com/frontend-wizard/react-components",
                    "languages": ["TypeScript", "CSS", "JavaScript"],
                    "stars": 2100,
                    "forks": 420
                },
                {
                    "name": "css-animations",
                    "description": "Collection of smooth CSS animations and transitions.",
                    "url": "https://github.com/frontend-wizard/css-animations",
                    "languages": ["CSS", "HTML"],
                    "stars": 850,
                    "forks": 180
                }
            ]),
            "languages": ["TypeScript", "JavaScript", "CSS", "HTML"],
            "topics": ["react", "frontend", "typescript", "css", "ui-ux", "accessibility"],
            "followers_count": 1320,
            "following_count": 200,
            "total_stars_received": 2950,
            "total_forks": 600,
            "profile_text_for_embedding": "Emily Johnson, Frontend developer creating beautiful and accessible web experiences. Repositories: react-components, Reusable React component library with TypeScript. css-animations, Collection of smooth CSS animations and transitions. Languages: TypeScript, JavaScript, CSS. Topics: react, frontend, typescript, css, ui-ux.",
            "last_updated": current_time
        },
        {
            "user_id": "e5f6g7h8-i9j0-1234-5678-901234efghij",
            "github_username": "rust-enthusiast",
            "display_name": "David Kim",
            "bio": "Systems programmer passionate about performance and memory safety.",
            "location": "Seattle, WA",
            "repositories": json.dumps([
                {
                    "name": "memory-allocator",
                    "description": "Custom memory allocator written in Rust for high-performance applications.",
                    "url": "https://github.com/rust-enthusiast/memory-allocator",
                    "languages": ["Rust"],
                    "stars": 1750,
                    "forks": 240
                },
                {
                    "name": "concurrent-data-structures",
                    "description": "Lock-free data structures for concurrent programming in Rust.",
                    "url": "https://github.com/rust-enthusiast/concurrent-data-structures",
                    "languages": ["Rust"],
                    "stars": 1200,
                    "forks": 180
                }
            ]),
            "languages": ["Rust", "C++", "Assembly"],
            "topics": ["rust", "systems-programming", "performance", "memory-safety", "concurrency"],
            "followers_count": 980,
            "following_count": 85,
            "total_stars_received": 2950,
            "total_forks": 420,
            "profile_text_for_embedding": "David Kim, Systems programmer passionate about performance and memory safety. Repositories: memory-allocator, Custom memory allocator written in Rust for high-performance applications. concurrent-data-structures, Lock-free data structures for concurrent programming in Rust. Languages: Rust, C++, Assembly. Topics: rust, systems-programming, performance, memory-safety.",
            "last_updated": current_time
        }
    ]

    try:
        with client.batch.dynamic() as batch:
            for profile in user_profiles:
                batch.add_object(
                    collection="weaviate_user_profile",
                    properties=profile
                )
        print("✅ Populated weaviate_user_profile with sample user data.")
    except Exception as e:
        print(f"❌ Error populating weaviate_user_profile: {e}")

def populate_all_collections():
    """
    Populate only the user profile collection as per the updated model structure.
    """
    client = get_client()
    print("Populating Weaviate user profile collection with sample data...")
    populate_weaviate_user_profile(client)
    client.close()
    print("✅ User profile collection populated successfully.")
