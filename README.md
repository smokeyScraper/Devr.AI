# Devr.AI - AI-Powered Developer Relations Assistant

## Table of Contents

-   [Project Overview](#project-overview)
-   [System Architecture](#system-architecture)
-   [Setup Guide](#setup-guide)
-   [Core Features](#core-features)
-   [Technology Stack](#technology-stack)
-   [Integration Details](#integration-details)
-   [Workflows](#workflows)
-   [Data Flow and Storage](#data-flow-and-storage)
-   [Planned Features & Roadmap](#planned-features--roadmap)
-   [Deployment Strategy](#deployment-strategy)

## Project Overview

Devr.AI is an advanced AI-powered Developer Relations (DevRel) assistant designed to revolutionize open-source community management. Currently integrating with Discord and GitHub, Devr.AI functions as a virtual DevRel advocate that helps maintainers engage with contributors, streamline onboarding processes, and deliver real-time project updates.

The system leverages Large Language Models (LLMs), knowledge retrieval mechanisms, and workflow automation to enhance community engagement, simplify contributor onboarding, and ensure that open-source projects remain active and well-supported.

Devr.AI bridges the gap between projects and their developer communities by providing technical education, creating engaging content, facilitating documentation access, and delivering personalized experiences that reduce maintainer workload while improving overall community satisfaction.

### Key Value Propositions

-   **Reduce maintainer workload** by automating routine interactions and queries
-   **Improve contributor experience** through personalized onboarding and support
-   **Enhance project visibility** via consistent engagement and community nurturing
-   **Generate actionable insights** from community interactions and contribution patterns
-   **Ensure knowledge preservation** by capturing and organizing project information
-   **Accelerate developer productivity** with interactive tutorials and code assistance
-   **Strengthen documentation** with AI-powered navigation and custom content generation

## System Architecture

```mermaid
flowchart TB
    %% External Platforms
    subgraph "External Platforms"
        GH["GitHub"]
        DS["Discord"]
    end

    %% React Frontend
    subgraph "React Frontend"
        FRONT["React + Vite + TailwindCSS"]
        DASH["Dashboard"]
    end

    %% FastAPI Backend
    subgraph "FastAPI Backend"
        API["FastAPI Gateway"]
        HEALTH["Health Endpoints"]
        AUTH_EP["Auth Endpoints"]
    end

    %% Authentication
    subgraph "Authentication"
        GitAuth["GitHub OAuth"]
        SupaAuth["Supabase Authentication"]
    end

    %% LangGraph Agent Orchestration
    subgraph "LangGraph Agent System"
        AC["Agent Coordinator"]
        DEVREL["DevRel Agent"]
        GITHUB_AGENT["GitHub Toolkit"]
    end

    %% Agent Workflow (ReAct Pattern)
    subgraph "DevRel Agent Workflow"
        GATHER["Gather Context"]
        SUPERVISOR["ReAct Supervisor"]
        TOOLS["Tool Execution"]
        RESPONSE["Generate Response"]
        SUMMARY["Summarization"]
    end

    %% Tools & Capabilities
    subgraph "Agent Tools"
        WEB_SEARCH["Web Search (Tavily)"]
        FAQ["FAQ Tool"]
        ONBOARD["Onboarding Tool"]
        GH_TOOLS["GitHub Tools"]
    end

    %% Queue System
    subgraph "Async Processing"
        RABBIT["RabbitMQ Queue"]
        WORKERS["Queue Workers"]
    end

    %% AI Services
    subgraph "AI Services"
        GEMINI["Google Gemini LLM"]
        TAVILY["Tavily Search API"]
        EMBEDDINGS["Text Embeddings"]
    end

    %% Integration Services
    subgraph "Integration Services"
        DISCORD_BOT["Discord Bot"]
        DISCORD_COGS["Discord Commands"]
        GH_WEBHOOK["GitHub Webhooks"]
    end

    %% Data Storage Layer
    subgraph "Data Storage"
        SUPA_DB["Supabase (PostgreSQL)"]
        WEAVIATE["Weaviate (Vector DB)"]
        MEMORY["Agent Memory Store"]
    end

    %% User Management
    subgraph "User Management"
        USER_PROF["User Profiles"]
        VERIFICATION["GitHub Verification"]
        SESSIONS["Conversation Sessions"]
    end

    %% Connections - External to Frontend
    FRONT --> DASH
    DASH <--> API

    %% API Endpoints
    API --> HEALTH
    API --> AUTH_EP

    %% External Platform Connections
    DS <--> DISCORD_BOT
    GH <--> GH_WEBHOOK

    %% Discord Integration
    DISCORD_BOT <--> DISCORD_COGS
    DISCORD_BOT <--> RABBIT

    %% Authentication Flow
    API <--> GitAuth
    API <--> SupaAuth
    AUTH_EP <--> VERIFICATION

    %% Agent Orchestration
    RABBIT <--> AC
    AC --> DEVREL
    AC --> GITHUB_AGENT

    %% Agent Workflow
    DEVREL --> GATHER
    GATHER --> SUPERVISOR
    SUPERVISOR --> TOOLS
    TOOLS --> RESPONSE
    RESPONSE --> SUMMARY

    %% Tool Connections
    TOOLS --> WEB_SEARCH
    TOOLS --> FAQ
    TOOLS --> ONBOARD
    TOOLS --> GH_TOOLS

    %% AI Service Connections
    SUPERVISOR <--> GEMINI
    RESPONSE <--> GEMINI
    WEB_SEARCH <--> TAVILY
    EMBEDDINGS <--> WEAVIATE

    %% Data Storage Connections
    DEVREL <--> MEMORY
    USER_PROF <--> SUPA_DB
    VERIFICATION <--> SUPA_DB
    SESSIONS <--> SUPA_DB
    MEMORY <--> WEAVIATE

    %% Queue Processing
    RABBIT --> WORKERS
    WORKERS --> AC

    %% Response Flow
    RESPONSE --> RABBIT
    RABBIT --> DISCORD_BOT

    %% Styling
    classDef external fill:#e0f7fa,stroke:#00796b,stroke-width:2px,color:#000;
    classDef frontend fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#000;
    classDef backend fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#000;
    classDef auth fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#000;
    classDef agents fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#000;
    classDef workflow fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000;
    classDef tools fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000;
    classDef queue fill:#fff8e1,stroke:#ffa000,stroke-width:2px,color:#000;
    classDef ai fill:#e8f5e9,stroke:#4caf50,stroke-width:2px,color:#000;
    classDef integration fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#000;
    classDef storage fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000;
    classDef users fill:#f1f8e9,stroke:#689f38,stroke-width:2px,color:#000;

    %% Apply classes
    class GH,DS external;
    class FRONT,DASH frontend;
    class API,HEALTH,AUTH_EP backend;
    class GitAuth,SupaAuth auth;
    class AC,DEVREL,GITHUB_AGENT agents;
    class GATHER,SUPERVISOR,TOOLS,RESPONSE,SUMMARY workflow;
    class WEB_SEARCH,FAQ,ONBOARD,GH_TOOLS tools;
    class RABBIT,WORKERS queue;
    class GEMINI,TAVILY,EMBEDDINGS ai;
    class DISCORD_BOT,DISCORD_COGS,GH_WEBHOOK integration;
    class SUPA_DB,WEAVIATE,MEMORY storage;
    class USER_PROF,VERIFICATION,SESSIONS users;
```

### High-Level Architecture Overview

Devr.AI is built on a **LangGraph agent-based architecture** that replaces traditional centralized LLM approaches with autonomous, reasoning agents that can think, act, and observe. The system follows a **ReAct (Reasoning and Acting) pattern** for intelligent decision-making and tool usage.

#### **Core Architectural Components**

-   **LangGraph Agent System**

    -   **Agent Coordinator**: Central orchestrator that manages agent instances and handles routing between different specialized agents
    -   **DevRel Agent**: Primary conversational agent using ReAct workflow for community support and engagement
    -   **GitHub Toolkit**: Specialized agent for GitHub-specific operations and integrations

-   **ReAct Agent Workflow**

    -   **Gather Context**: Collects user information, conversation history, and platform-specific context
    -   **ReAct Supervisor**: Implements Think → Act → Observe pattern to decide which tools to use
    -   **Tool Execution**: Dynamically selects and executes appropriate tools (web search, FAQ, onboarding, GitHub operations)
    -   **Generate Response**: Synthesizes tool results into coherent, contextual responses
    -   **Summarization**: Maintains long-term conversation memory and context preservation

-   **Asynchronous Processing**

    -   **RabbitMQ Message Queue**: Handles high-throughput message processing with priority-based queuing
    -   **Queue Workers**: Multiple worker processes for parallel message handling and agent coordination
    -   **Background Tasks**: User profiling, verification flows, and maintenance operations

-   **AI Services Integration**

    -   **Google Gemini**: Primary LLM for reasoning, response generation, and conversation management
    -   **Tavily Search API**: Real-time web search and information retrieval
    -   **Text Embeddings**: Semantic search and knowledge retrieval from vector storage

-   **Platform Integrations**

    -   **Discord Bot**: Real-time community engagement with command support and conversation threads
    -   **GitHub Integration**: Webhook processing, issue triage, and repository analysis

-   **Data Storage Architecture**

    -   **Supabase (PostgreSQL)**: User profiles, authentication, conversation metadata, and structured data
    -   **Weaviate Vector Database**: Semantic search, embeddings storage, and knowledge retrieval
    -   **Agent Memory Store**: Persistent conversation context and user interaction history

-   **Authentication & User Management**
    -   **GitHub OAuth Integration**: User verification and repository access
    -   **Supabase Authentication**: Session management and user account linking
    -   **Multi-platform Identity**: Unified user profiles across Discord and GitHub

## Core Features

### 1. LangGraph Agent-Based Intelligence

-   **ReAct Reasoning Pattern**

    -   Think → Act → Observe workflow for intelligent decision making
    -   Dynamic tool selection based on conversation context
    -   Iterative problem-solving with self-correction capabilities

-   **Conversational Memory**

    -   Persistent conversation context across Discord sessions
    -   Automatic summarization after 15+ interactions or timeout
    -   Long-term user relationship building with topic tracking

-   **Multi-Tool Orchestration**
    -   Web search integration via Tavily for real-time information
    -   FAQ knowledge base for common questions
    -   GitHub toolkit for repository-specific assistance (basic implementation)
    -   Onboarding flows for new community members

### 2. Discord Community Integration

-   **Intelligent Message Processing**

    -   Real-time classification of messages requiring AI intervention
    -   Context-aware responses based on conversation history
    -   Background processing via RabbitMQ for scalable message handling

-   **GitHub Account Verification**

    -   OAuth-based GitHub account linking for enhanced personalization
    -   Automatic user profiling with repository and contribution analysis
    -   Secure verification flow with time-limited tokens

-   **Command Interface**
    -   `!verify_github` for account linking and verification
    -   `!verification_status` to check current account status
    -   `!reset` for conversation memory management
    -   `!help_devrel` for command assistance and bot capabilities

### 3. Advanced Data Management

-   **Multi-Database Architecture**

    -   Supabase (PostgreSQL) for structured user data and authentication
    -   Weaviate vector database for semantic search and embeddings
    -   Integrated data flow between relational and vector storage

-   **User Profiling & Analytics**

    -   Comprehensive GitHub profile analysis (repositories, languages, contributions)
    -   Semantic user modeling stored in vector format for intelligent matching
    -   Cross-platform identity linking (Discord ↔ GitHub integration)

-   **Conversation Intelligence**
    -   Persistent conversation context with automatic summarization
    -   Topic extraction and conversation pattern analysis
    -   Memory management with configurable retention policies

### 4. Scalable Infrastructure & Processing

-   **Asynchronous Message Processing**

    -   RabbitMQ message queue with priority-based processing
    -   Multiple worker processes for parallel task execution
    -   Graceful error handling and message acknowledgment

-   **Agent Coordination Framework**

    -   Central coordinator managing multiple specialized agents
    -   LangGraph state management with persistent checkpointing
    -   Dynamic routing between DevRel and GitHub toolkit agents

-   **Real-Time Response Generation**
    -   Google Gemini integration for natural language understanding
    -   Context-aware response personalization
    -   Platform-specific formatting and delivery optimization

## Planned Features & Roadmap

### Upcoming Integrations

-   **Slack Workspace Integration**
    -   Block Kit interactive components
    -   Workflow automation for technical announcements
    -   Channel-specific DevRel agent configurations

-   **CLI Tool Integration**
    -   Command-line interface for developers
    -   Local environment integration
    -   Repository health checks and diagnostics

-   **Web Widget Integration**
    -   Embeddable chat widget for documentation sites
    -   Real-time assistance for website visitors
    -   Seamless handoff to Discord/GitHub

### Enhanced GitHub Features

-   **Advanced Issue Triage**
    -   Automated issue labeling and assignment
    -   Duplicate detection and linking
    -   Priority classification

-   **Pull Request Assistance**
    -   Review comment suggestions
    -   Code quality analysis
    -   Automated testing recommendations

-   **Repository Analytics**
    -   Contributor statistics and recognition
    -   Health monitoring and insights
    -   Release notes generation

### Content Creation & Education

-   **Technical Content Generation**
    -   Blog post drafts with code examples
    -   Social media announcements
    -   Tutorial creation assistance

-   **Interactive Learning**
    -   Step-by-step coding tutorials
    -   Live debugging assistance
    -   Skill assessment and personalized learning paths

-   **Documentation Enhancement**
    -   AI-powered documentation generation
    -   Contextual help integration
    -   Knowledge gap identification

### Advanced Analytics

-   **Community Health Metrics**
    -   Engagement trend analysis
    -   Contributor retention insights
    -   Sentiment monitoring

-   **Performance Analytics**
    -   Response time optimization
    -   User satisfaction tracking
    -   Feature usage analytics

## Setup Guide

For installing the project locally refer to the [Installation Guide](./docs/INSTALL_GUIDE.md)

## Technology Stack

### Backend Services

-   **Core Framework**: FastAPI with asynchronous lifespan management
-   **Agent Framework**: LangGraph for multi-agent orchestration
-   **Messaging Queue**: RabbitMQ with `aio-pika` for asynchronous processing
-   **Containerization**: Docker & Docker Compose
-   **Web Server**: Uvicorn ASGI server

### AI & LLM Services

-   **Primary LLM**: Google Gemini (gemini-2.5-flash, gemini-2.0-flash)
-   **Web Search**: Tavily Search API for real-time information retrieval
-   **Text Embeddings**: Sentence Transformers for semantic search
-   **Agent Patterns**: ReAct (Reasoning and Acting) workflow implementation
-   **Memory Management**: LangGraph checkpointing with conversation summarization

### Data Storage

-   **Relational Database**: Supabase (PostgreSQL) for user profiles, auth, and structured data
-   **Vector Database**: Weaviate for semantic search and embeddings storage
-   **Authentication**: Supabase Auth with GitHub OAuth integration
-   **Agent Memory**: Persistent conversation context and state management

### Frontend Components

-   **Landing Page**: React + Vite + TypeScript
-   **Styling**: Tailwind CSS with custom themes
-   **Animations**: Framer Motion for interactive UI
-   **Icons**: Lucide React icon library
-   **Routing**: React Router DOM
-   **Deployment**: Netlify with SPA configuration

### Platform Integrations

-   **Discord**: py-cord (Discord.py v2) with commands and cogs
-   **GitHub**: PyGithub for repository and issue management
-   **User Verification**: GitHub OAuth flow integration
-   **Webhooks**: FastAPI endpoints for platform event handling

### Development & Infrastructure

-   **Language**: Python 3.9+ with type hints
-   **Package Management**: Poetry with pyproject.toml
-   **Environment**: python-dotenv for configuration
-   **Async Operations**: aiohttp, asyncio for concurrent processing
-   **Testing**: pytest for unit and integration tests
-   **Code Quality**: flake8, autopep8, isort for code formatting

### Monitoring & Observability

-   **Tracing**: LangSmith integration for agent workflow tracing
-   **Health Checks**: Built-in health endpoints for system monitoring
-   **Logging**: Structured logging with configurable levels
-   **Error Handling**: Comprehensive exception management in agent flows

## Integration Details

### Discord Integration

```mermaid
sequenceDiagram
    participant User as Discord User
    participant Bot as Discord Bot
    participant ClassRouter as Classification Router
    participant Queue as RabbitMQ Queue
    participant Coordinator as Agent Coordinator
    participant DevRel as DevRel Agent
    participant DB as Supabase/Weaviate

    User->>Bot: Sends message or uses command
    Bot->>ClassRouter: Classify message intent
    ClassRouter->>Bot: Triage result (process/ignore)
    
    alt Message requires DevRel processing
        Bot->>Queue: Enqueue devrel_request
        Queue->>Coordinator: Process message
        Coordinator->>DevRel: Create AgentState & invoke
        
        DevRel->>DevRel: Gather Context
        DevRel->>DevRel: ReAct Supervisor (Think→Act→Observe)
        DevRel->>DevRel: Generate Response
        DevRel->>DB: Update conversation memory
        
        DevRel->>Queue: Queue response
        Queue->>Bot: Discord response event
        Bot->>User: Send formatted response
    else Command processing
        Bot->>Bot: Handle command directly
        Bot->>User: Command response
    end

    Note over DevRel,DB: Agent maintains persistent<br/>conversation memory
```

#### Current Implementation

-   **Discord Bot Framework**: py-cord (Discord.py v2) with modern async/await patterns
-   **Command System**: Discord Cogs architecture for modular command organization
-   **Message Processing**: Real-time classification and intelligent routing
-   **Memory Management**: Thread-based conversation persistence with user context

#### Bot Commands

-   **`!verify_github`**: Initiates GitHub OAuth verification flow
-   **`!verification_status`**: Checks GitHub account linking status
-   **`!reset`**: Clears conversation thread memory
-   **`!help_devrel`**: Shows available commands and bot capabilities

#### Features

-   **Intelligent Classification**: Determines which messages need AI processing vs simple responses
-   **Thread Management**: Creates conversation threads for complex discussions
-   **User Verification**: GitHub account linking for enhanced personalization
-   **Context Preservation**: Maintains conversation history across sessions
-   **Background Processing**: Asynchronous message handling via RabbitMQ
-   **Error Handling**: Graceful degradation with user-friendly error messages

#### Data Flow

1. Discord bot receives message or command using py-cord event handlers
2. Classification router determines if DevRel agent processing is needed
3. Messages requiring AI processing are queued via RabbitMQ with priority
4. Agent Coordinator creates AgentState and invokes appropriate LangGraph agent
5. DevRel Agent executes ReAct workflow (gather context → think → act → respond)
6. Response is queued back to Discord bot for delivery
7. Conversation state and user interactions are persisted to databases

### Slack Integration

```mermaid
sequenceDiagram
    participant User as Slack User
    participant Slack as Slack Platform
    participant API as API Gateway
    participant EP as Event Processor
    participant AI as AI Service
    participant KB as Knowledge Base

    User->>Slack: Sends message/command
    Slack->>API: Forwards via Events API
    API->>EP: Process Slack event

    EP->>KB: Query relevant information
    KB->>EP: Return knowledge snippets

    EP->>AI: Generate response
    AI->>EP: Return formatted response

    EP->>Slack: Send Block Kit message
    Slack->>User: Display interactive response

    alt User Interaction
        User->>Slack: Clicks interactive element
        Slack->>API: Action payload
        API->>EP: Process interaction
        EP->>Slack: Update message
        Slack->>User: Show updated content
    end
```

#### Authentication & Setup

-   Slack App Directory installation flow
-   Workspace-specific settings configuration
-   Channel mapping to project components

#### Event Handling

-   Message events in channels and direct messages
-   App mention events
-   Interactive component events (buttons, dropdowns)

#### Features

-   Slash commands for project information
-   Interactive message components for issue triage
-   Automatic daily/weekly project updates
-   Direct message onboarding for new contributors
-   Technical content generation for announcements
-   Documentation search functionality
-   Code assistance and review through file sharing

#### Data Flow

1. Slack Events API sends event to API Gateway
2. Event processor validates and processes the event
3. User context and preferences are retrieved
4. Workflow engine determines appropriate action
5. Response is formatted according to Slack Block Kit
6. Message is sent back to appropriate Slack channel

### GitHub Integration

```mermaid
sequenceDiagram
    participant GH as GitHub
    participant API as API Gateway
    participant EP as Event Processor
    participant AT as Automated Triage
    participant AI as AI Service
    participant DB as Database

    GH->>API: Webhook (Issue/PR/Comment)
    API->>EP: Process GitHub event

    alt New Issue
        EP->>AT: Triage new issue
        AT->>AI: Analyze issue content
        AI->>AT: Return classification
        AT->>GH: Apply labels & suggestions
        AT->>DB: Log issue metadata
    else New PR
        EP->>AT: Review PR
        AT->>AI: Analyze code changes
        AI->>AT: Return review comments
        AT->>GH: Post initial review
        AT->>DB: Track PR statistics
    else Comment
        EP->>AI: Process comment context
        AI->>EP: Generate appropriate response
        EP->>GH: Post response comment
        EP->>DB: Update conversation tracking
    end
```

#### Authentication & Setup

-   GitHub App installation process
-   Repository-specific configuration
-   Permission scopes management

#### Event Handling

-   Issue creation, update, and comment events
-   Pull request lifecycle events
-   Repository star and fork events
-   Release publication events

#### Features

-   Automated issue labeling and assignment
-   PR review comments and suggestions
-   Release notes generation
-   Contributor statistics and recognition
-   Documentation suggestions for code changes
-   Sample code generation for issue resolution
-   Quickstart guides based on repository structure

#### Data Flow

1. GitHub webhook sends event to API Gateway
2. Event processor categorizes and enriches event data
3. User context and repository information are retrieved
4. Task is assigned to appropriate service based on event type
5. Response actions are taken via GitHub API
6. Event and action are logged for analytics

### CLI Integration

#### Authentication & Setup

-   API key authentication
-   Repository linking
-   User preference synchronization

#### Event Handling

-   Command execution events
-   Interactive prompts and inputs
-   File system access events

#### Features

-   Direct access to documentation and code examples
-   Interactive tutorials and guided workflows
-   Local environment setup assistance
-   Repository health checks and diagnostics
-   Custom command extension capabilities
-   Contextual help based on current project

#### Data Flow

1. CLI tool sends command to API Gateway
2. Command is processed with user context and repository information
3. Response is generated based on command parameters
4. Results are displayed in the terminal interface
5. User interactions are tracked for personalization

### Web Widget Integration

#### Authentication & Setup

-   JavaScript snippet for website embedding
-   Configuration options for appearance and behavior
-   Anonymous or authenticated user sessions

#### Event Handling

-   Widget activation events
-   User query submissions
-   Interface interaction events

#### Features

-   Documentation search and browsing
-   Contextual help based on current page
-   Question answering capabilities
-   Code example generation and explanation
-   Guided onboarding for new developers
-   Analytics for most common queries and issues

#### Data Flow

1. Widget sends user interaction to API Gateway
2. Page context and user information are included in request
3. Response is generated based on query and context
4. Results are displayed within the widget interface
5. Interactions are logged for analytics and personalization

### Discourse Integration

#### Authentication & Setup

-   API key authentication
-   Category and tag mapping
-   User role configuration

#### Event Handling

-   New topic creation events
-   Post creation and update events
-   User registration events

#### Features

-   Automatic responses to common questions
-   Cross-linking between forum topics and GitHub issues
-   Knowledge base article suggestions
-   Community showcase of project achievements
-   Technical content generation for forum posts
-   Interactive tutorial linking
-   Documentation search capability

#### Data Flow

1. Discourse webhook or API polling detects new content
2. Content is processed and classified
3. User context and preferences are retrieved
4. Knowledge retrieval finds relevant information
5. Response is generated and posted to appropriate thread
6. New knowledge is extracted and stored for future use

## Workflows

### LangGraph Agent Workflow (ReAct Pattern)

```mermaid
stateDiagram-v2
    [*] --> MessageReceived

    MessageReceived --> ClassificationTriage
    ClassificationTriage --> QueueMessage: DevRel Needed
    ClassificationTriage --> IgnoreMessage: No Action Required

    QueueMessage --> AgentCoordinator
    AgentCoordinator --> CreateAgentState
    CreateAgentState --> DevRelAgent

    %% DevRel Agent ReAct Workflow
    DevRelAgent --> GatherContext
    GatherContext --> ReActSupervisor

    ReActSupervisor --> Think
    Think --> Act
    Act --> WebSearchTool: Web Search Needed
    Act --> FAQTool: FAQ Query
    Act --> OnboardingTool: New User
    Act --> GitHubToolkit: GitHub Related
    Act --> Complete: Sufficient Info

    WebSearchTool --> UpdateContext
    FAQTool --> UpdateContext
    OnboardingTool --> UpdateContext
    GitHubToolkit --> UpdateContext

    UpdateContext --> ReActSupervisor: Continue Loop
    UpdateContext --> CheckIteration: Max Iterations
    CheckIteration --> ReActSupervisor: Under Limit
    CheckIteration --> Complete: Over Limit

    Complete --> GenerateResponse
    GenerateResponse --> CheckSummarization
    
    CheckSummarization --> SummarizeConversation: Needed
    CheckSummarization --> SendResponse: Not Needed

    SummarizeConversation --> UpdateMemory
    UpdateMemory --> SendResponse

    SendResponse --> QueueResponse
    QueueResponse --> PlatformDelivery
    PlatformDelivery --> [*]

    IgnoreMessage --> [*]
```

The LangGraph Agent Workflow implements a **ReAct (Reasoning and Acting) pattern** that enables the AI to think before acting and observe results to make informed decisions.

#### **Workflow Phases**

-   **Message Processing**
    -   Platform messages (Discord, GitHub, etc.) are received and classified
    -   Classification triage determines if DevRel agent intervention is needed
    -   Qualified messages are queued with appropriate priority

-   **Agent Initialization**
    -   Agent Coordinator creates initial AgentState with user context
    -   Session management handles conversation continuity and memory
    -   DevRel Agent begins processing with conversation history

-   **Context Gathering**
    -   Collects user profile information and interaction history
    -   Loads previous conversation summary and key topics
    -   Prepares platform-specific context for decision making

-   **ReAct Loop (Think → Act → Observe)**
    -   **Think**: Supervisor analyzes current context and determines next action
    -   **Act**: Executes selected tool (web search, FAQ lookup, onboarding, GitHub operations)
    -   **Observe**: Reviews tool results and updates conversation context
    -   Loop continues until sufficient information is gathered or max iterations reached

-   **Response Generation**
    -   Synthesizes all gathered information into a coherent response
    -   Personalizes response based on user profile and conversation history
    -   Applies platform-specific formatting (Discord embeds, GitHub comments, etc.)

-   **Memory Management**
    -   Checks if conversation summarization is needed (after 15+ interactions or timeout)
    -   Creates compressed conversation summaries for long-term memory
    -   Updates user profile with new topics and interaction patterns

-   **Response Delivery**
    -   Queues response message for appropriate platform
    -   Handles platform-specific delivery mechanisms
    -   Tracks delivery status and error handling

### GitHub Verification Workflow

```mermaid
stateDiagram-v2
    [*] --> UserJoinsDiscord
    
    UserJoinsDiscord --> DiscordInteraction
    DiscordInteraction --> VerifyGitHubCommand: !verify_github
    DiscordInteraction --> CheckStatusCommand: !verification_status
    DiscordInteraction --> Continue: Other Commands
    
    VerifyGitHubCommand --> CheckExistingUser
    CheckExistingUser --> AlreadyVerified: GitHub Linked
    CheckExistingUser --> CreateVerificationSession: Not Verified
    
    CreateVerificationSession --> GenerateOAuthURL
    GenerateOAuthURL --> SendDMToUser
    SendDMToUser --> UserClicksLink
    
    UserClicksLink --> GitHubOAuth
    GitHubOAuth --> AuthCallback
    AuthCallback --> VerifyAndLinkAccount
    
    VerifyAndLinkAccount --> ProfileUserAsync: Success
    VerifyAndLinkAccount --> AuthError: Failure
    
    ProfileUserAsync --> FetchGitHubData
    FetchGitHubData --> StoreInWeaviate
    StoreInWeaviate --> NotifySuccess
    
    CheckStatusCommand --> QueryUserStatus
    QueryUserStatus --> ReturnStatus
    
    AlreadyVerified --> [*]
    NotifySuccess --> [*]
    AuthError --> [*]
    ReturnStatus --> [*]
    Continue --> [*]
```

#### **GitHub Integration Process**

-   **Discord Command Integration**
    -   `!verify_github` command initiates OAuth flow
    -   `!verification_status` checks current account linking status
    -   Background token cleanup prevents expired verification sessions

-   **OAuth Verification Flow**
    -   Creates temporary verification session with expiring tokens
    -   Generates GitHub OAuth URL with state parameter for security
    -   Sends private message to user with verification instructions

-   **Account Linking**
    -   Validates OAuth callback with authorization code
    -   Links GitHub account to Discord user in Supabase database
    -   Prevents duplicate account associations

-   **User Profiling**
    -   Asynchronously fetches GitHub user data, repositories, and pull requests
    -   Analyzes programming language usage across repositories
    -   Stores comprehensive user profile in Weaviate for semantic search

-   **Data Persistence**
    -   User profiles stored in Supabase for structured queries
    -   Conversation context maintained for cross-session continuity
    -   Vector embeddings in Weaviate for intelligent recommendations

### Technical Education Workflow

```mermaid
stateDiagram-v2
    [*] --> DetectLearningIntent

    DetectLearningIntent --> LoadUserProfile
    LoadUserProfile --> AssessKnowledgeLevel

    AssessKnowledgeLevel --> CodeExplainer: Code Questions
    AssessKnowledgeLevel --> QuickstartGenerator: Setup Requests
    AssessKnowledgeLevel --> TutorialEngine: How do I Questions
    AssessKnowledgeLevel --> LiveAssistance: Debug Help

    CodeExplainer --> GenerateMarkdown
    CodeExplainer --> CreateDiagrams

    QuickstartGenerator --> CreateCodeSnippets

    TutorialEngine --> BuildInteractiveUI

    LiveAssistance --> UseCodeAnalysis
    LiveAssistance --> AccessKnowledgeBase

    GenerateMarkdown --> DeliverResponse
    CreateDiagrams --> DeliverResponse
    CreateCodeSnippets --> DeliverResponse
    BuildInteractiveUI --> DeliverResponse
    UseCodeAnalysis --> DeliverResponse
    AccessKnowledgeBase --> DeliverResponse

    DeliverResponse --> MonitorProgress

    MonitorProgress --> ProvideHints: User Stuck
    MonitorProgress --> ValidateCompletion: Step Completed

    ProvideHints --> MonitorProgress

    ValidateCompletion --> NextStep: Tutorial Ongoing
    ValidateCompletion --> CompleteTutorial: All Steps Done

    NextStep --> MonitorProgress

    CompleteTutorial --> UpdateUserProfile
    UpdateUserProfile --> SuggestNextTutorial
    SuggestNextTutorial --> [*]
```

-   **Trigger**: User requests learning resources or system detects learning opportunity
-   **Request Routing**: System routes the request to the appropriate education service:
    -   Code Explainer for code understanding questions
    -   Quickstart Generator for setup assistance
    -   Tutorial Engine for how-to questions
    -   Live Assistance for debugging problems
-   **Content Generation**: Creates personalized educational response:
    -   Markdown explanations with formatted text
    -   Diagrams for visual learners
    -   Code snippets with examples
    -   Interactive UI for hands-on learning
-   **Delivery**: Presents educational content through:
    -   Step-by-step guides in chat interface
    -   Visual aids and diagrams where appropriate
    -   Interactive elements for engagement
-   **Feedback Loop**: Monitors progress and provides assistance:
    -   Real-time validation of exercise completion
    -   Hints when user is stuck
    -   Celebration of milestone achievements
    -   Recording of progress for future sessions

### Content Creation Workflow

```mermaid
stateDiagram-v2
    [*] --> UserSignUp

    UserSignUp --> ScheduledTask
    ScheduledTask --> WebScraper

    WebScraper --> ContentRouter
    ContentRouter --> LLMContentGenerator

    LLMContentGenerator --> ContentReview

    ContentReview --> ApprovalSystem
    ContentReview --> AudioGenerator
    ContentReview --> LLMRepoInsights
    ContentReview --> ReferenceEngine

    ApprovalSystem --> PublishingSystem
    PublishingSystem --> AnalyticsLogs
    AnalyticsLogs --> [*]
```

-   **Trigger**: Scheduled content generation task, user signup event, or maintainer request
-   **Content Collection**: Web scraper gathers relevant information from:
    -   Documentation sites
    -   Blog posts
    -   Technical papers
    -   Community discussions
-   **Content Routing**: System categorizes content needs and directs to appropriate generators
-   **Generation**: LLM-based content generator creates appropriate content type:
    -   Technical blog post drafts with code examples
    -   Sample code for various use cases
    -   API documentation with practical examples
    -   Social media announcements with key highlights
-   **Review & Enhancement**: Content undergoes quality checks and enhancements:
    -   Technical accuracy verification
    -   Style and formatting adjustments
    -   Repository insights integration
    -   Reference linking and citation
-   **Output Processing**: Finalized content is prepared for distribution:
    -   Manual or automated approval
    -   Publication to appropriate channels
    -   Audio generation for accessibility
    -   Analytics tracking for performance measurement

### Personalization Workflow

```mermaid
stateDiagram-v2
    [*] --> GatherUserData

    GatherUserData --> DataCollection

    DataCollection --> ProfileGeneration
    DataCollection --> InterestAnalysis
    DataCollection --> SkillDetection

    ProfileGeneration --> ContentFiltering
    InterestAnalysis --> SuggestionGeneration
    SkillDetection --> ResponseTailoring

    ContentFiltering --> RecommendationSystem
    SuggestionGeneration --> RecommendationSystem
    ResponseTailoring --> RecommendationSystem

    RecommendationSystem --> DeliverPersonalizedExperience
    DeliverPersonalizedExperience --> [*]
```

-   **Data Collection**: Gathers user-specific information from various sources:
    -   Interaction history with the system
    -   Developer profile and background
    -   Usage patterns across platforms
    -   Stated preferences and feedback
    -   Geographic location and language
-   **User Modeling**: Processes collected data to build comprehensive user profile:
    -   Technical expertise level determination
    -   Interest area identification
    -   Skill assessment and gap analysis
-   **Content Adaptation**: Customizes interactions based on user model:
    -   Content filtering to match expertise level
    -   Suggestion generation for relevant resources
    -   Response tailoring for communication style
-   **Recommendation System**: Delivers personalized content and assistance:
    -   Content ranking based on relevance
    -   Discovery engine for new resources
    -   Contextual recommendations

### Issue Triage Workflow

```mermaid
stateDiagram-v2
    [*] --> NewIssueDetected

    NewIssueDetected --> AnalyzeContent

    AnalyzeContent --> CheckDuplicates
    CheckDuplicates --> IdentifyDuplicate: Match Found
    CheckDuplicates --> ClassifyIssue: No Duplicate

    IdentifyDuplicate --> LinkIssues
    LinkIssues --> NotifyUser
    NotifyUser --> CloseAsDuplicate
    CloseAsDuplicate --> [*]

    ClassifyIssue --> AssignLabels
    AssignLabels --> DetermineComplexity

    DetermineComplexity --> SuggestAssignees
    SuggestAssignees --> CheckCompleteness

    CheckCompleteness --> RequestInfo: Incomplete
    CheckCompleteness --> GenerateRepro: Bug Report
    CheckCompleteness --> CreateSample: Feature Request
    CheckCompleteness --> UpdateProject: Documentation Issue

    RequestInfo --> AwaitResponse
    AwaitResponse --> AnalyzeContent: Info Provided
    AwaitResponse --> CloseStale: No Response

    GenerateRepro --> UpdateProject
    CreateSample --> UpdateProject

    UpdateProject --> NotifyTeam
    NotifyTeam --> ScheduleFollowUp
    ScheduleFollowUp --> [*]

    CloseStale --> [*]
```

-   **Trigger**: New issue created on GitHub
-   **Analysis**:
    -   AI extracts key information from issue description
    -   Compares with existing issues for duplicates
    -   Identifies affected components and potential severity
-   **Classification**:
    -   Applies appropriate labels (bug, feature, documentation, etc.)
    -   Assigns priority level
    -   Suggests potential assignees based on expertise
-   **Enhancement**:
    -   Requests additional information if description is incomplete
    -   Generates reproduction steps for bug reports when possible
    -   Creates sample code for feature requests to clarify intent
    -   Provides links to relevant documentation
-   **Notification**:
    -   Alerts appropriate team members in Slack/Discord
    -   Updates project boards
    -   Schedules follow-up if issue remains unaddressed

### Knowledge Query Workflow

```mermaid
stateDiagram-v2
    [*] --> QuestionDetected

    QuestionDetected --> LoadUserContext
    LoadUserContext --> ClassifyIntent
    ClassifyIntent --> ExtractEntities

    ExtractEntities --> SearchKnowledgeBase
    SearchKnowledgeBase --> SearchCodebase
    SearchCodebase --> SearchPriorConversations

    SearchPriorConversations --> GenerateResponse: Information Found
    SearchPriorConversations --> FallbackResponse: No Information

    GenerateResponse --> PersonalizeContent
    PersonalizeContent --> FormatWithExamples
    FormatWithExamples --> AddReferences
    AddReferences --> DeliverResponse

    FallbackResponse --> GenerateGenericGuidance
    GenerateGenericGuidance --> SuggestAlternatives
    SuggestAlternatives --> DeliverResponse

    DeliverResponse --> UpdateUserContext
    UpdateUserContext --> RecordInteraction
    RecordInteraction --> UpdateFAQ: Common Question
    RecordInteraction --> [*]: Unique Question

    UpdateFAQ --> [*]
```

-   **Trigger**: Question asked in any integrated platform
-   **Context Loading**:
    -   Retrieves user's interaction history and preferences
    -   Identifies user's knowledge level and communication style
-   **Intent Recognition**:
    -   Identifies question type and topic
    -   Extracts key entities and concepts
-   **Knowledge Retrieval**:
    -   Searches vector database for semantically similar content
    -   Retrieves relevant documentation and past answers
    -   Examines code repository for relevant examples
-   **Personalization**:
    -   Adapts complexity level to user's expertise
    -   References previous interactions for continuity
    -   Formats response based on user preferences
-   **Response Generation**:
    -   Creates comprehensive yet concise answer
    -   Includes code examples if appropriate
    -   Adds links to official documentation
-   **Knowledge Capture**:
    -   Records question and answer in knowledge base
    -   Updates user context with new information
    -   Updates FAQ if question is common

### Community Analytics Workflow

-   **Data Collection**:
    -   Continuous monitoring of activity across all platforms
    -   Tracking of individual contributor actions
    -   Recording of response times and resolution rates
-   **Processing**:
    -   Aggregation of metrics by timeframe and category
    -   Calculation of derived metrics (e.g., contributor retention)
    -   Trend analysis and anomaly detection
    -   Sentiment analysis of community interactions
-   **Insight Generation**:
    -   Identification of active vs. declining areas
    -   Recognition of valuable contributors
    -   Detection of potential community issues
    -   Assessment of content effectiveness
-   **Reporting**:
    -   Automated weekly summaries to maintainers
    -   Interactive dashboard updates
    -   Quarterly comprehensive project health reports
    -   Content performance analytics
-   **Action Recommendation**:
    -   Suggestions for community engagement improvements
    -   Identification of contributors for recognition
    -   Alerts for areas needing maintainer attention
    -   Content strategy recommendations

## Data Flow and Storage

### Current Data Architecture

```mermaid
flowchart TB
    subgraph "Data Sources"
        DISCORD["Discord Messages"]
        GITHUB_API["GitHub API"]
        USER_INPUT["User Commands"]
        OAUTH["OAuth Callbacks"]
    end

    subgraph "Processing Layer"
        BOT["Discord Bot"]
        CLASSIFIER["Classification Router"]
        RABBIT["RabbitMQ Queue"]
        COORD["Agent Coordinator"]
    end

    subgraph "Agent Layer"
        DEVREL["DevRel Agent"]
        GITHUB_AGENT["GitHub Toolkit"]
        TOOLS["Agent Tools"]
    end

    subgraph "Storage Systems"
        SUPA["Supabase PostgreSQL"]
        WEAVIATE["Weaviate Vector DB"]
        MEMORY["Agent Memory"]
    end

    subgraph "Data Types"
        USERS["User Profiles"]
        CONVOS["Conversations"]
        EMBEDDINGS["Vector Embeddings"]
        SESSIONS["Verification Sessions"]
    end

    %% Data Flow
    DISCORD --> BOT
    USER_INPUT --> BOT
    OAUTH --> BOT

    BOT --> CLASSIFIER
    CLASSIFIER --> RABBIT
    RABBIT --> COORD

    COORD --> DEVREL
    COORD --> GITHUB_AGENT
    DEVREL --> TOOLS

    GITHUB_API --> GITHUB_AGENT
    GITHUB_AGENT --> WEAVIATE

    %% Storage Connections
    DEVREL --> MEMORY
    MEMORY --> SUPA
    MEMORY --> WEAVIATE

    USERS --> SUPA
    CONVOS --> SUPA
    EMBEDDINGS --> WEAVIATE
    SESSIONS --> SUPA

    %% Response Flow
    DEVREL --> RABBIT
    RABBIT --> BOT
    BOT --> DISCORD
```

#### **Data Processing Pipeline**

-   **Message Ingestion**
    -   Discord bot receives messages and commands via py-cord
    -   Classification router determines processing requirements
    -   Priority-based queuing via RabbitMQ for scalable processing

-   **Agent Processing**
    -   Agent Coordinator manages LangGraph agent lifecycle
    -   DevRel Agent executes ReAct workflow with persistent state
    -   Tool execution results stored in conversation context

-   **Data Persistence**
    -   **Supabase (PostgreSQL)**: User profiles, authentication, conversation metadata
    -   **Weaviate (Vector DB)**: User embeddings, semantic search, knowledge base
    -   **Agent Memory**: Conversation summaries, interaction history, context preservation

#### **Storage Schema**

-   **User Management**
    -   Discord and GitHub account linking
    -   OAuth verification tokens and session management
    -   User preferences and interaction statistics

-   **Conversation Intelligence**
    -   Thread-based conversation context
    -   Automatic summarization for long-term memory
    -   Topic extraction and conversation pattern analysis

-   **Vector Knowledge Base**
    -   User profile embeddings for semantic matching
    -   Repository and contribution analysis
    -   FAQ and knowledge article embeddings for retrieval

## Deployment Strategy

### Infrastructure Architecture

```mermaid
flowchart TB
    subgraph "Development Environment"
        DEV_K8S["Kubernetes Cluster"]
        DEV_DB["Database Services"]
        DEV_CACHE["Cache Layer"]
    end

    subgraph "Staging Environment"
        STAGE_K8S["Kubernetes Cluster"]
        STAGE_DB["Database Services"]
        STAGE_CACHE["Cache Layer"]
    end

    subgraph "Production Environment"
        subgraph "Region A"
            PROD_K8S_A["Kubernetes Cluster"]
            PROD_DB_A["Database Primary"]
            PROD_CACHE_A["Cache Primary"]
        end

        subgraph "Region B"
            PROD_K8S_B["Kubernetes Cluster"]
            PROD_DB_B["Database Replica"]
            PROD_CACHE_B["Cache Replica"]
        end

        LB["Load Balancer"]
        CDN["Content Delivery Network"]
    end

    subgraph "CI/CD Pipeline"
        GIT["Git Repository"]
        CI["Continuous Integration"]
        REG["Container Registry"]
        CD["Continuous Deployment"]
    end

    GIT --> CI
    CI --> REG
    REG --> CD

    CD --> DEV_K8S
    CD --> STAGE_K8S
    CD --> PROD_K8S_A
    CD --> PROD_K8S_B

    LB --> PROD_K8S_A
    LB --> PROD_K8S_B

    PROD_DB_A <--> PROD_DB_B
    PROD_CACHE_A <--> PROD_CACHE_B

    CDN --> LB
```

-   **Multi-environment Setup**:

    -   Development environment for active feature development
    -   Staging environment for integration testing
    -   Production environment for live deployment

-   **Containerized Deployment**:

    -   Microservices packaged as Docker containers
    -   Kubernetes for orchestration and scaling
    -   Helm charts for deployment configuration

-   **High Availability Design**:
    -   Multiple replicas of critical services
    -   Cross-zone deployment on cloud provider
    -   Automatic failover mechanisms

### CI/CD Pipeline

-   **Code Integration**:

    -   Pull request validation
    -   Automated code quality checks
    -   Unit test execution

-   **Build Process**:

    -   Docker image building
    -   Image vulnerability scanning
    -   Artifact versioning

-   **Deployment Stages**:

    -   Automated deployment to development
    -   Manual approval for staging promotion
    -   Canary deployment to production
    -   Progressive rollout strategy

-   **Monitoring and Rollback**:
    -   Health check validation post-deployment
    -   Automatic rollback on critical metrics deviation
    -   Deployment audit logging
