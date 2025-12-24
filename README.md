# 100-Day AI Agent Engineering Course
## Build a Production AI Agent From Scratch

**One concept per day. One agent. 100 capabilities.**

---

## 🎯 Course Philosophy

- **30-60 minutes per day**
- **One new feature each day**
- **Same codebase grows throughout**
- **Git commit after each day**
- **No skipping - each day builds on the last**

By Day 100, you'll have a production-ready AI agent system you built from first principles.

---

## 📋 Prerequisites

- Python 3.9+
- Basic Python knowledge (functions, classes, loops)
- Git installed
- Text editor or IDE
- ~150-200 hours total time commitment

---

## 🚀 Setup

### 1. Clone or Create Your Project

```bash
mkdir my-agent
cd my-agent
git init
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate    # Windows
```

### 3. Install Initial Dependencies

```bash
pip install anthropic python-dotenv
```

### 4. Create `.env` File

```bash
# Create .env file
echo "ANTHROPIC_API_KEY=your_key_here" > .env
```

Get your API key from: https://console.anthropic.com/

### 5. Create `.gitignore`

```bash
cat > .gitignore << EOF
.env
__pycache__/
*.pyc
venv/
conversation_history.json
EOF
```

### 6. Create Your First File

```bash
touch agent.py
```

You're ready to start Day 1!

---

## 📅 100-Day Challenge Roadmap

### ✅ Completion Tracking

Mark each day with ✅ when complete, add your commit hash for reference.

---
## **100-Day AI Agent Engineering Challenge**

### **WEEK 1-2: Foundation (Days 1-14)**

- **Day 1:** First API Response - Get a single response from Claude
  - Read Anthropic's [Create a Message](https://platform.claude.com/docs/en/api/python/messages/create) documentation and implement a call to the endpoint. Print the response to console.

- **Day 2:** User Input Loop - Accept ongoing conversation
  - Wrap your API call in a `while True` loop that takes user input and displays responses until user types 'quit'.

- **Day 3:** Conversation Memory - Track message history
  - Create a `conversation_history` list that stores all user and assistant messages. Pass this full history to each API call.

- **Day 4:** Streaming Responses - Real-time token display
  - Replace `messages.create()` with `messages.stream()` to display words as they're generated instead of waiting for complete response.

- **Day 5:** System Prompts - Add agent personality
  - Add a `system` parameter to your API call with instructions that define your agent's personality, tone, and expertise.

- **Day 6:** Save Conversations - Persist to JSON file
  - Use Python's `json` module to save `conversation_history` to a file when user quits, and load it on startup.

- **Day 7:** Error Handling - Network errors, rate limits, graceful failures
  - Wrap API calls in try/except blocks to catch `APIError`, `APIConnectionError`, and `RateLimitError`. Display friendly error messages.

- **Day 8:** First Tool - `get_current_time()` function
  - Create a simple Python function that returns current time. Define it in the `tools` parameter and let Claude decide when to call it.

- **Day 9:** Tool Calling Protocol - Understand request→tool→result flow
  - Add logging to see when Claude requests a tool, what parameters it sends, and how you return results in the next message.

- **Day 10:** Calculator Tool - Add function with parameters
  - Create a `calculate(operation, a, b)` function and define its schema with required parameters. Test with math questions.

- **Day 11:** Multiple Tools - Agent chooses between 4+ tools
  - Add weather, web search, file read, and random number tools. Ask questions requiring different tools to see Claude's selection logic.

- **Day 12:** Tool Error Handling - Graceful tool failures
  - Wrap tool execution in try/except. Return error messages to Claude so it can retry or explain the failure to the user.

- **Day 13:** Tool Logging - Track all tool calls
  - Create a `tool_log.json` file that records every tool call with timestamp, tool name, inputs, outputs, and success/failure status.

- **Day 14:** Simple Tools Collection - File reader, coin flip, dice roller
  - Build 5+ simple utility tools with clear descriptions. Test that Claude picks the right tool for diverse user requests.

---

### **WEEK 3-4: External World (Days 15-28)**

- **Day 15:** Web Search Setup - Integrate search API
  - Sign up for a search API (Brave, Serper, or Tavily). Store API key in `.env` and test basic search queries.

- **Day 16:** Parse Search Results - Extract clean data
  - Write a function that takes raw search JSON and extracts title, snippet, URL into a clean format Claude can use.

- **Day 17:** Web Search Tool - Agent searches autonomously
  - Add web search as a tool. Claude should now be able to search the internet when it needs current information.

- **Day 18:** Fetch Web Pages - Get full page content
  - Use `requests` + `BeautifulSoup` to create a tool that fetches and extracts main text content from URLs.

- **Day 19:** Search + Fetch Chain - Multi-step tool usage
  - Ask Claude a research question. It should search, then fetch relevant pages, then synthesize an answer with citations.

- **Day 20:** Summarization - Condense long text
  - Create a tool that chunks long documents and asks Claude to summarize each chunk, then combine summaries.

- **Day 21:** Source Citations - Track information sources
  - Modify your tools to return source metadata. Prompt Claude to always cite sources in its responses.

- **Day 22:** Conversation Summarization - Compress old messages
  - When conversation exceeds 10 messages, summarize oldest messages into a single context message to save tokens.

- **Day 23:** Vector Database Setup - Install ChromaDB
  - `pip install chromadb`. Create a collection and test adding/querying a few text chunks with embeddings.

- **Day 24:** Generate Embeddings - Create text embeddings
  - Use Voyage AI or OpenAI embeddings API to convert text chunks into vectors. Store them in ChromaDB.

- **Day 25:** Semantic Search - Find similar chunks
  - Build a tool that takes a query, creates its embedding, and returns top-k most similar chunks from your vector database.

- **Day 26:** Document Chunking - Split docs intelligently
  - Create a function that splits documents by paragraphs or sentences while keeping chunks under 500 tokens with some overlap.

- **Day 27:** Metadata Filtering - Filter by source, date
  - Add metadata (source, date, category) to chunks. Modify search tool to filter results by these attributes.

- **Day 28:** Hybrid Search - Combine keyword and semantic
  - Implement BM25 keyword search alongside vector search. Combine and rerank results from both approaches.

---

### **WEEK 5-6: Memory & RAG Systems (Days 29-42)**

- **Day 29:** Reranking - Two-stage retrieval
  - Use a reranking model (Cohere or cross-encoder) to score and reorder your retrieved chunks for better relevance.

- **Day 30:** PROJECT: Personal Knowledge Base
  - Build a complete system: upload PDFs/text files, chunk and embed them, then chat with your documents using RAG.

- **Day 31:** Advanced RAG - Query Rewriting
  - Before retrieving, ask Claude to rewrite the user's vague question into 2-3 specific search queries for better results.

- **Day 32:** Multi-Query RAG - Multiple search queries
  - Generate 3 different query variations, retrieve docs for each, combine and deduplicate results before answering.

- **Day 33:** Agentic RAG - Agent decides when to retrieve
  - Don't auto-retrieve. Give Claude a "search_knowledge_base" tool and let it decide when it needs to look things up.

- **Day 34:** Citation & Source Tracking - No hallucinations
  - Format retrieved chunks with [Source 1], [Source 2] markers. Prompt Claude to cite specific sources for every claim.

- **Day 35:** Conversation + RAG Integration - Memory + knowledge
  - Combine conversation memory with RAG. Agent remembers chat history AND can retrieve from knowledge base simultaneously.

- **Day 36:** Chain-of-Thought Prompting - Step-by-step reasoning
  - Add "Think step-by-step" to your system prompt. Compare answers with and without CoT for complex problems.

- **Day 37:** Few-Shot Learning - Examples in prompts
  - For structured tasks (extraction, classification), provide 3-5 examples in your system prompt showing desired input→output.

- **Day 38:** Self-Consistency - Multiple reasoning paths
  - For important questions, ask Claude to generate 3 different reasoning chains, then pick the most common answer.

- **Day 39:** Tool-Enhanced CoT - Reasoning + tools
  - Prompt Claude to explain its reasoning before using tools, then verify results after tool execution.

- **Day 40:** Error Recovery - Agent fixes own mistakes
  - When a tool fails or returns unexpected results, let Claude see the error and ask it to try a different approach.

- **Day 41:** Verification Loop - Agent checks its work
  - After generating an answer, ask Claude to critique it and identify potential errors before showing to user.

- **Day 42:** PROJECT: Research Assistant
  - Build an agent that takes a research question, searches web, reads papers, synthesizes findings with citations.

---

### **WEEK 7-8: Memory Architecture (Days 43-56)**

- **Day 43:** Short-Term Memory - Recent conversation buffer
  - Keep last 10 messages in full detail while older messages get summarized. Implement a sliding window.

- **Day 44:** Long-Term Memory - Persistent user facts
  - Extract facts about the user ("prefers Python," "works at Google") and store them in a separate context that persists across sessions.

- **Day 45:** Working Memory - Task-specific context
  - For complex multi-step tasks, maintain a separate "working memory" that tracks progress, next steps, and intermediate results.

- **Day 46:** Memory Retrieval - Smart context selection
  - When context gets large, retrieve only relevant memories based on current query instead of loading everything.

- **Day 47:** Hybrid Search - Combine keyword and semantic search
  - Apply the same hybrid search from Day 28 to your memory retrieval—search memories by both keywords and semantic similarity.

- **Day 48:** Memory Consolidation - Summarize and compress
  - Periodically review old memories and consolidate similar facts, remove duplicates, and compress detailed logs.

- **Day 49:** Episodic Memory - Store specific interactions
  - Save complete conversation episodes with timestamps. Let agent recall "what we discussed last Tuesday about X."

- **Day 50:** Memory Retrieval Strategy - Relevance ranking
  - Implement scoring for memories: recency + relevance + importance. Retrieve top-k memories instead of all.

---

### **WEEK 8-9: Planning & Reasoning (Days 51-65)**

- **Day 51:** Chain-of-Thought - Force step-by-step reasoning
  - Add explicit "reasoning" section to prompts. Make Claude show its work before answering.

- **Day 52:** Tree of Thoughts - Explore multiple paths
  - For complex problems, ask Claude to explore 3 different solution approaches before committing to one.

- **Day 53:** ReAct Pattern - Reasoning + Acting loop
  - Implement Thought→Action→Observation cycle. Agent thinks, acts with tools, observes results, and repeats.

- **Day 54:** Task Decomposition - Break into subtasks
  - Give Claude a complex task and ask it to break it into numbered subtasks before executing each one.

- **Day 55:** Plan-Execute Pattern - Separate planning/execution
  - First pass: Claude creates a detailed plan. Second pass: Execute each step of the plan with separate API calls.

- **Day 56:** Self-Ask - Agent asks clarifying questions
  - Before answering vague queries, prompt Claude to ask 2-3 clarifying questions to understand user intent better.

- **Day 57:** Reflexion - Agent critiques own outputs
  - After generating a response, ask Claude to identify weaknesses or errors in its own answer and improve it.

- **Day 58:** Goal Stack - Hierarchical goal structure
  - Maintain a stack of goals/subgoals. Agent pops completed goals and tracks progress toward main objective.

- **Day 59:** Iterative Refinement - Multiple improvement passes
  - Generate initial answer, then run 2-3 refinement passes asking Claude to improve clarity, accuracy, and completeness.

- **Day 60:** Constraint Satisfaction - Meet requirements
  - Give Claude explicit constraints (word limit, must include 3 examples, etc.). Verify outputs meet all constraints.

- **Day 61:** Backtracking - Recover from failures
  - When an approach fails, store it in "tried_approaches" and ask Claude to try a different method.

- **Day 62:** Verification Loop - Check own work
  - After task completion, run verification prompts: "Are there any errors? Did we miss anything?"

- **Day 63:** Meta-Prompting - Agent writes prompts
  - Give Claude a task and ask it to first write the optimal prompt for solving it, then execute using that prompt.

- **Day 64:** Reasoning Traces - Log thought processes
  - Save all intermediate reasoning steps to a file for debugging and understanding agent's decision-making.

- **Day 65:** Adaptive Strategies - Switch approaches
  - Define different strategies (fast/thorough, creative/analytical). Let Claude choose based on task type.

---

### **WEEK 10-11: Multi-Agent Systems (Days 66-80)**

- **Day 66:** Two-Agent Dialogue - Agents discuss problems
  - Create two agents with different personalities. Have them discuss a topic back-and-forth for 5 turns.

- **Day 67:** Agent Communication Protocol - Message passing
  - Define a structured message format (JSON) for agents to exchange information, requests, and results.

- **Day 68:** Specialist Agents - Domain experts
  - Create 3 specialized agents: Researcher, Coder, Writer. Each has different system prompts and tools.

- **Day 69:** Agent Orchestration - Central coordinator
  - Build a coordinator agent that receives user requests and delegates to specialist agents based on task type.

- **Day 70:** Debate Pattern - Agents argue perspectives
  - Create two agents arguing opposite sides of a question. Third "judge" agent picks the best argument.

- **Day 71:** Ensemble Voting - Vote on best answer
  - Generate answers from 3 agents independently. Combine them or vote on the best response.

- **Day 72:** Agent Handoff - Pass tasks between agents
  - Agent 1 does research, passes findings to Agent 2 who writes report. Maintain context across handoff.

- **Day 73:** Hierarchical Agents - Manager/worker structure
  - Manager agent breaks task into subtasks and assigns each to worker agents. Manager synthesizes results.

- **Day 74:** Collaborative RAG - Multiple knowledge bases
  - Each agent has access to different knowledge bases. They collaborate to answer questions requiring multiple sources.

- **Day 75:** Agent Market - Bid on tasks
  - Agents "bid" on tasks based on their confidence/expertise. Coordinator selects the best agent for each task.

- **Day 76:** Consensus Building - Negotiate understanding
  - Agents propose answers, discuss disagreements, and iteratively refine until they reach consensus.

- **Day 77:** Parallel Agent Execution - Simultaneous work
  - Use `asyncio` to run multiple agents simultaneously. Combine results once all complete.

- **Day 78:** Agent Swarms - Many simple agents
  - Create 10+ simple agents with single-purpose tools. Swarm solves problems through collective behavior.

- **Day 79:** Meta-Agent - Creates/manages other agents
  - Build an agent that can spawn new specialized agents dynamically based on user requirements.

- **Day 80:** Multi-Agent Memory - Shared knowledge
  - All agents read/write to a shared memory store. Updates from one agent are visible to others.

---

### **WEEK 12: Advanced Capabilities (Days 81-90)**

- **Day 81:** Input Validation - Detect prompt injections
  - Check user inputs for injection patterns ("Ignore previous instructions"). Reject or sanitize malicious inputs.

- **Day 82:** Output Filtering - Content safety
  - Screen agent outputs for harmful content, PII, or policy violations before displaying to user.

- **Day 83:** Hallucination Detection - Verify claims
  - When agent makes factual claims, verify them against retrieved sources or search results.

- **Day 84:** Uncertainty Quantification - Confidence levels
  - Prompt agent to express confidence (high/medium/low) for each claim. Lower confidence = search for verification.

- **Day 85:** Evaluation Harness - Automated testing
  - Create 20 test cases with expected outputs. Run agent on all tests and calculate pass rate.

- **Day 86:** A/B Testing Framework - Compare configurations
  - Run same queries through two different system prompts or settings. Compare quality, cost, and latency.

- **Day 87:** Prompt Optimization - Auto-improve prompts
  - Generate variations of your system prompt. Test each on validation set and keep the best performer.

- **Day 88:** Few-Shot Learning - Dynamic example selection
  - Store example library. For each query, retrieve most similar examples and include them in the prompt.

- **Day 89:** Agent Fine-Tuning Data - Collect training data
  - Log all user queries and agent responses. Format them as training examples for future fine-tuning.

- **Day 90:** RLHF - Basic reinforcement learning
  - Add thumbs up/down to responses. Use feedback to identify high/low quality outputs for training data.

---

### **WEEK 13-14: Production (Days 91-100)**

- **Day 91:** API Wrapper - REST API with FastAPI
  - Install FastAPI. Create POST `/chat` endpoint that accepts messages and returns agent responses.

- **Day 92:** Rate Limiting - Control request frequency
  - Use `slowapi` to limit requests per IP (10/minute). Return 429 status when limit exceeded.

- **Day 93:** Caching Layer - Cache expensive calls
  - Use Redis to cache identical queries. Check cache before calling LLM to save costs.

- **Day 94:** Async Processing - Long-running tasks
  - Use Celery + Redis for tasks taking >30 seconds. Return task ID immediately, poll for results.

- **Day 95:** Monitoring & Alerting - Track performance
  - Add Prometheus metrics: request count, latency, errors, token usage. Set up alerts for anomalies.

- **Day 96:** User Session Management - Multiple users
  - Use JWT tokens for auth. Store each user's conversation history separately in database.

- **Day 97:** Cost Optimization - Smart model routing
  - Route simple queries to fast/cheap model (Haiku). Complex queries to powerful model (Opus). Track savings.

- **Day 98:** Deployment Pipeline - Container & deploy
  - Write Dockerfile. Set up GitHub Actions to build and deploy to cloud (Railway/Render) on every push.

- **Day 99:** Load Testing - Stress test agent
  - Use `locust` to simulate 100 concurrent users. Identify bottlenecks and optimize.

- **Day 100:** Complete Agent System - End-to-end production
  - Polish your entire system, write comprehensive README, create demo video, deploy publicly, and share your journey!

---

**🎉 Congratulations!** You've built a production AI agent from scratch, one day at a time.
---

## 📊 Progress Tracking

```
Days completed: 1 /100
Current week: 1
Started: Dec 22, 2025
Target completion: [DATE + 15 weeks]
```

---

## 🎓 Learning Tips

### Daily Routine

1. **Read** the day's goal (5 min)
2. **Code** the feature (30-60 min)
3. **Test** that it works (5-10 min)
4. **Commit** to git (1 min)
5. **Reflect** on what you learned (5 min)

### Git Workflow

```bash
# After each day
git add .
git commit -m "Day X: [feature description]"
git tag day-X
```

### If You Get Stuck

1. Read error messages carefully
2. Add print statements to debug
3. Search the specific error online
4. Take a break and come back
5. Ask for help (communities, forums, AI)

### If You Fall Behind

- Don't skip days to catch up
- Do them in order, even if it takes longer
- Weekend are for catching up
- Better to do it right than fast

---

## 🏆 Milestones

- **Day 10:** First working tool-using agent
- **Day 28:** Agent with memory
- **Day 42:** Agent that reasons
- **Day 56:** Agent that searches intelligently
- **Day 70:** Agent that plans
- **Day 84:** Multi-agent system
- **Day 98:** Production deployment
- **Day 100:** Complete system

---

## 📝 Notes Section

Use this space to track insights, bugs, ideas:

```
Day 1: [Your notes]
Day 2: [Your notes]
...
```

---

## 🚀 Ready to Start?

1. Complete the setup above
2. Open `agent.py` in your editor
3. Start with Day 1: Get your first API response
4. Commit after each day
5. Track progress by checking boxes above

**Remember:** The goal isn't speed. The goal is understanding. Build it right.

Good luck! 🎉

---

## 📚 Resources

- [Anthropic Docs](https://docs.anthropic.com/)
- [OpenAI Docs](https://platform.openai.com/docs)
- [LangChain Docs](https://python.langchain.com/)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

---

**Version:** 1.0  
**Last Updated:** December 2024  
**License:** MIT



