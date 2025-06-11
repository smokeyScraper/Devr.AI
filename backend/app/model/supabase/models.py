from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional, List
from datetime import datetime


class User(BaseModel):
    """
    Represents a user profile with various platform integrations and metadata.

    Attributes:
      id (UUID): Unique identifier for the user.
      created_at (datetime): Timestamp when the user was created.
      updated_at (datetime): Timestamp when the user was last updated.
      discord_id (Optional[str]): Discord user ID, if linked.
      discord_username (Optional[str]): Discord username, if linked.
      github_id (Optional[str]): GitHub user ID, if linked.
      github_username (Optional[str]): GitHub username, if linked.
      slack_id (Optional[str]): Slack user ID, if linked.
      slack_username (Optional[str]): Slack username, if linked.
      display_name (str): Display name of the user.
      email (str): Email address of the user.
      avatar_url (Optional[str]): URL to the user's avatar image.
      bio (Optional[str]): Short biography or description of the user.
      location (Optional[str]): User's location.
      is_verified (bool): Indicates if the user is verified.
      verification_token (Optional[str]): Token used for verifying the user.
      verified_at (Optional[datetime]): Timestamp when the user was verified.
      skills (Optional[List[str]]): List of user's skills.
      github_stats (Optional[dict]): GitHub statistics for the user.
      last_active_discord (Optional[datetime]): Last active time on Discord.
      last_active_github (Optional[datetime]): Last active time on GitHub.
      last_active_slack (Optional[datetime]): Last active time on Slack.
      total_interactions_count (int): Total number of user interactions.
      preferred_languages (List[str]): List of user's preferred programming languages.
      weaviate_user_id (Optional[str]): Associated Weaviate user ID, if any.
    """
    id: UUID
    created_at: datetime
    updated_at: datetime
    discord_id: Optional[str] = None
    discord_username: Optional[str] = None
    github_id: Optional[str] = None
    github_username: Optional[str] = None
    slack_id: Optional[str] = None
    slack_username: Optional[str] = None
    display_name: str
    email: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    is_verified: bool = False
    verification_token: Optional[str] = None
    verified_at: Optional[datetime] = None
    skills: Optional[List[str]] = None
    github_stats: Optional[dict] = None
    last_active_discord: Optional[datetime] = None
    last_active_github: Optional[datetime] = None
    last_active_slack: Optional[datetime] = None
    total_interactions_count: int = 0
    preferred_languages: List[str] = Field(default_factory=list)
    weaviate_user_id: Optional[str] = None

class Repository(BaseModel):
    """
    Represents a GitHub repository with metadata and indexing status.

    Attributes:
      id (UUID): Unique identifier for the repository.
      created_at (datetime): Timestamp when the repository record was created.
      updated_at (datetime): Timestamp when the repository record was last updated.
      github_id (Optional[int]): GitHub's unique identifier for the repository.
      full_name (str): Full name of the repository (e.g., "owner/name").
      name (str): Name of the repository.
      owner (str): Owner of the repository.
      description (Optional[str]): Description of the repository.
      stars_count (int): Number of stars the repository has received.
      forks_count (int): Number of times the repository has been forked.
      open_issues_count (int): Number of open issues in the repository.
      language (Optional[str]): Primary programming language used in the repository.
      topics (List[str]): List of topics/tags associated with the repository.
      is_indexed (bool): Indicates if the repository has been indexed.
      indexed_at (Optional[datetime]): Timestamp when the repository was indexed.
      indexing_status (Optional[str]): Current status of the indexing process.
      total_chunks_count (int): Total number of chunks generated during indexing.
      last_commit_hash (Optional[str]): Hash of the last commit indexed.
      indexing_progress (Optional[dict]): Progress details of the indexing process.
      weaviate_repo_id (Optional[str]): Identifier for the repository in Weaviate.
    """
    id: UUID
    created_at: datetime
    updated_at: datetime
    github_id: Optional[int] = None
    full_name: str
    name: str
    owner: str
    description: Optional[str] = None
    stars_count: int = 0
    forks_count: int = 0
    open_issues_count: int = 0
    language: Optional[str] = None
    topics: List[str] = Field(default_factory=list)
    is_indexed: bool = False
    indexed_at: Optional[datetime] = None
    indexing_status: Optional[str] = None
    total_chunks_count: int = 0
    last_commit_hash: Optional[str] = None
    indexing_progress: Optional[dict] = None
    weaviate_repo_id: Optional[str] = None

class CodeChunk(BaseModel):
    """
    Represents a chunk of code extracted from a file within a repository.

    Attributes:
      id (UUID): Unique identifier for the code chunk.
      repository_id (UUID): Identifier of the repository this chunk belongs to.
      created_at (datetime): Timestamp when the chunk was created.
      file_path (str): Path to the file containing the code chunk.
      file_name (str): Name of the file containing the code chunk.
      file_extension (Optional[str]): Extension of the file (e.g., '.py', '.js').
      chunk_index (int): Index of the chunk within the file.
      content (str): The actual code content of the chunk.
      chunk_type (Optional[str]): Type of the chunk (e.g., 'function', 'class', 'block').
      language (Optional[str]): Programming language of the code chunk.
      lines_start (Optional[int]): Starting line number of the chunk in the file.
      lines_end (Optional[int]): Ending line number of the chunk in the file.
      code_metadata (Optional[dict]): Additional metadata related to the code chunk.
      weaviate_chunk_id (Optional[str]): Identifier for the chunk in Weaviate vector database.
    """
    id: UUID
    repository_id: UUID
    created_at: datetime
    file_path: str
    file_name: str
    file_extension: Optional[str] = None
    chunk_index: int
    content: str
    chunk_type: Optional[str] = None
    language: Optional[str] = None
    lines_start: Optional[int] = None
    lines_end: Optional[int] = None
    code_metadata: Optional[dict] = None
    weaviate_chunk_id: Optional[str] = None

class Interaction(BaseModel):
    """
    Represents an interaction within a repository platform, such as a message, comment, or post.

    Attributes:
      id (UUID): Unique identifier for the interaction.
      created_at (datetime): Timestamp when the interaction was created.
      updated_at (datetime): Timestamp when the interaction was last updated.
      user_id (UUID): Unique identifier of the user who performed the interaction.
      repository_id (UUID): Unique identifier of the repository associated with the interaction.
      platform (str): Name of the platform where the interaction occurred (e.g., GitHub, Slack).
      platform_specific_id (str): Platform-specific identifier for the interaction.
      channel_id (Optional[str]): Identifier for the channel where the interaction took place, if applicable.
      thread_id (Optional[str]): Identifier for the thread within the channel, if applicable.
      content (str): The textual content of the interaction.
      interaction_type (str): Type of interaction (e.g., message, comment, issue).
      sentiment_score (Optional[float]): Sentiment analysis score of the interaction content.
      intent_classification (Optional[str]): Classification of the user's intent in the interaction.
      topics_discussed (List[str]): List of topics discussed in the interaction.
      metadata (Optional[dict]): Additional metadata related to the interaction.
      weaviate_interaction_id (Optional[str]): Identifier for the interaction in the Weaviate vector database.
    """
    id: UUID
    created_at: datetime
    updated_at: datetime
    user_id: UUID
    repository_id: UUID
    platform: str
    platform_specific_id: str
    channel_id: Optional[str] = None
    thread_id: Optional[str] = None
    content: str
    interaction_type: str
    sentiment_score: Optional[float] = None
    intent_classification: Optional[str] = None
    topics_discussed: List[str] = Field(default_factory=list)
    metadata: Optional[dict] = None
    weaviate_interaction_id: Optional[str] = None
