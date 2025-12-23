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

## **WEEK 1-2: Foundation (Days 1-14)**

- [ ] **Day 1:** First API Response - Get a single response from Claude/OpenAI
- [ ] **Day 2:** User Input Loop - Accept ongoing conversation
- [ ] **Day 3:** Conversation Memory - Track message history
- [ ] **Day 4:** Streaming Responses - Real-time token display
- [ ] **Day 5:** System Prompts - Add agent personality
- [ ] **Day 6:** Save Conversations - Persist to JSON file
- [ ] **Day 7:** Error Handling - Network errors, rate limits, graceful failures
- [ ] **Day 8:** First Tool - `get_current_time()` function
- [ ] **Day 9:** Tool Calling Protocol - Understand request→tool→result flow
- [ ] **Day 10:** Calculator Tool - Add function with parameters
- [ ] **Day 11:** Multiple Tools - Agent chooses between 4+ tools
- [ ] **Day 12:** Tool Error Handling - Graceful tool failures
- [ ] **Day 13:** Tool Logging - Track all tool calls
- [ ] **Day 14:** Simple Tools Collection - File reader, coin flip, dice roller

---

## **WEEK 3-4: External World (Days 15-28)**

- [ ] **Day 15:** Web Search Setup - Integrate search API
- [ ] **Day 16:** Parse Search Results - Extract clean data
- [ ] **Day 17:** Web Search Tool - Agent searches autonomously
- [ ] **Day 18:** Fetch Web Pages - Get full page content
- [ ] **Day 19:** Search + Fetch Chain - Multi-step tool usage
- [ ] **Day 20:** Summarization - Condense long text
- [ ] **Day 21:** Source Citations - Track information sources
- [ ] **Day 22:** Conversation Summarization - Compress old messages
- [ ] **Day 23:** Vector Database Setup - Install ChromaDB
- [ ] **Day 24:** Generate Embeddings - Create text embeddings
- [ ] **Day 25:** Semantic Search - Query by meaning
- [ ] **Day 26:** Auto-Store Messages - Build long-term memory
- [ ] **Day 27:** Memory Retrieval Tool - Agent searches own memory
- [ ] **Day 28:** Memory Metadata - Add timestamps and tags

---

## **WEEK 5-6: Documents (Days 29-42)**

- [ ] **Day 29:** Read Text Files - Load local documents
- [ ] **Day 30:** Chunk Documents - Split into manageable pieces
- [ ] **Day 31:** Store Documents - Index in vector database
- [ ] **Day 32:** Query Documents - Search uploaded files
- [ ] **Day 33:** Multi-Document Support - Handle multiple files
- [ ] **Day 34:** PDF Support - Read PDF files
- [ ] **Day 35:** Smart Chunking - Sentence-based splitting
- [ ] **Day 36:** Chain-of-Thought - Force step-by-step reasoning
- [ ] **Day 37:** Reasoning Tool - Explicit think-aloud function
- [ ] **Day 38:** Task Decomposition - Break tasks into steps
- [ ] **Day 39:** Sequential Execution - Complete steps in order
- [ ] **Day 40:** Verification - Agent checks own work
- [ ] **Day 41:** Self-Correction Loop - Retry on failure
- [ ] **Day 42:** Confidence Scoring - Rate answer certainty

---

## **WEEK 7-8: Code Execution (Days 43-56)**

- [ ] **Day 43:** Code Sandbox Setup - Docker or E2B environment
- [ ] **Day 44:** Python Execution Tool - Run code safely
- [ ] **Day 45:** Data Analysis - Pandas integration
- [ ] **Day 46:** Visualization - Generate plots with matplotlib
- [ ] **Day 47:** Package Installation - Dynamic pip install
- [ ] **Day 48:** Multi-File Code - Create complex programs
- [ ] **Day 49:** Iterative Debugging - Fix errors automatically
- [ ] **Day 50:** Query Rewriting - Improve vague queries
- [ ] **Day 51:** Multi-Query Generation - Search from multiple angles
- [ ] **Day 52:** Reranking - Score and sort results
- [ ] **Day 53:** Hybrid Search - Keyword + semantic
- [ ] **Day 54:** Contextual Retrieval - Include surrounding chunks
- [ ] **Day 55:** Metadata Filtering - Filter by date/type/source
- [ ] **Day 56:** Agentic Retrieval - Agent decides when to search

---

## **WEEK 9-10: APIs & Planning (Days 57-70)**

- [ ] **Day 57:** Weather API - External service integration
- [ ] **Day 58:** Calendar Read - Google Calendar API
- [ ] **Day 59:** Calendar Write - Create events
- [ ] **Day 60:** Email Read - Gmail integration
- [ ] **Day 61:** Send Emails - With confirmation safety
- [ ] **Day 62:** Stock Prices - Financial data API
- [ ] **Day 63:** News Headlines - News API integration
- [ ] **Day 64:** Goal Stack - Track goals and subgoals
- [ ] **Day 65:** Plan-Execute Pattern - Separate planning from doing
- [ ] **Day 66:** Backtracking - Recover from failed steps
- [ ] **Day 67:** Dependency Tracking - Order tasks correctly
- [ ] **Day 68:** Parallel Execution - Run independent tasks simultaneously
- [ ] **Day 69:** Progress Tracking - Show completion percentage
- [ ] **Day 70:** Checkpointing - Save and resume state

---

## **WEEK 11-12: Multi-Agent (Days 71-84)**

- [ ] **Day 71:** Second Agent - Create researcher agent
- [ ] **Day 72:** Agent Communication - Message passing protocol
- [ ] **Day 73:** Coordinator Agent - Route tasks to specialists
- [ ] **Day 74:** Specialist Agents - Coder, writer, researcher
- [ ] **Day 75:** Debate Pattern - Two agents argue positions
- [ ] **Day 76:** Shared Memory - Collective knowledge base
- [ ] **Day 77:** Consensus Voting - Aggregate multiple agents
- [ ] **Day 78:** Input Validation - Detect prompt injection
- [ ] **Day 79:** Output Filtering - Content safety checks
- [ ] **Day 80:** Rate Limiting - Control request frequency
- [ ] **Day 81:** Cost Tracking - Monitor token usage
- [ ] **Day 82:** Evaluation Suite - Automated testing
- [ ] **Day 83:** Hallucination Detection - Verify factual claims
- [ ] **Day 84:** Confidence Intervals - Quantify uncertainty

---

## **WEEK 13-14: Performance & Production (Days 85-98)**

- [ ] **Day 85:** Response Caching - Save expensive calls
- [ ] **Day 86:** Streaming Tools - Real-time tool feedback
- [ ] **Day 87:** Model Routing - Choose model by complexity
- [ ] **Day 88:** Async Tools - Non-blocking execution
- [ ] **Day 89:** Batch Processing - Handle multiple requests
- [ ] **Day 90:** Token Optimization - Compress conversations
- [ ] **Day 91:** Lazy Loading - Load resources on demand
- [ ] **Day 92:** FastAPI Wrapper - REST API endpoints
- [ ] **Day 93:** Authentication - API key validation
- [ ] **Day 94:** Database Storage - PostgreSQL for users
- [ ] **Day 95:** Logging System - Structured logs
- [ ] **Day 96:** Error Monitoring - Sentry integration
- [ ] **Day 97:** Docker Container - Containerize system
- [ ] **Day 98:** Deploy to Cloud - Railway/Render/Fly.io

---

## **WEEK 15: Final (Days 99-100)**

- [ ] **Day 99:** Web Interface - HTML/JS frontend
- [ ] **Day 100:** Documentation & Launch - README, demo video, share publicly

---

## 📊 Progress Tracking

```
Days completed: 0/100
Current week: 1
Started: [DATE]
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
