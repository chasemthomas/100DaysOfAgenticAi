# 100-Day Agent Building Journal

Track your progress, insights, and challenges here.

---

## Week 1: Foundation

### Day 1 - First API Response
**Date:** Dec 22, 202520 minutes
**Completed:** [x]  

**What I built:** 
Simple client and message connection to Anthropic

**What I learned:**
1. Store api key in .env folder
2. Use OS and Dotenv modules to assign api key as environment variable
3. Use os.getenv to assign the api key to variable
4. Pass api key to Anthropic client
5. Create a message on the client, and pass in model, max tokens, and message. 
6. Print the response with `message.client`


**Challenges:**
My corporate laptop messes with the connection, so I had to disable the ssl certification for this program, which should be okay because it's for educational purposes. 

**Notes:**

Found the Anthropic documentation on how to [Create a Message](https://platform.claude.com/docs/en/api/python/messages/create) and followed that. 

Anthropic has you hard code the api key, but since I want to push this to github I went with the .env variable route. 

Docs say `api_key=os.environ.get("ANTHROPIC_API_KEY")` is passed into `anthropic.Anthropic` by default. Tested this with and without, and it is true.

> "The Messages API can be used for either single queries or stateless multi-turn conversations." 
- Single queries = send one message, get one response. 
- Stateless = API itself has no memory between requests

This means that this api will not behave like the Claude chat interface, remembering previous contexts. 

Streaming is false by default. Pass in "stream=True" to enable. However, when I did this I got the error "AttributeError: 'Stream' object has no attribute 'content'." Will save this for day 3. 

`message.content` gets you the full json repsonse. `message.content[0].text` gets you the specific text. 




---

### Day 2 - User Input Loop - Accept ongoing conversation
Wrap your API call in a `while True` loop that takes user input and displays responses until user types 'quit'.

**Date:**  Dec 23, 2025
**Completed:** [x]  

**What I built:** 
- A chatbot that I can have a conversation with in the terminal

**What I learned:**
- Each call to the api is a one-off sending in the current message. We then print that message to console and start the loop over. Therefore, each question happens in total isolation and the bot has no memory. Adding memory will mean saving each question and passing that in as context to the current question. 

**Challenges:**

**Notes:**
1. I had Claude generate descriptions to go underneath all of the day headers because it needed more direction. 
2. I copied the first day's code onto a new page. The intent is to build that muscle memory so that in the future I can do it from memory. 
3. Currently the api call is hard coded with a message. I need to wrap this in a function and pass in a user message variable. This will enable it to be called several times in the conversation. 
4. I added `if __name__ == "__main__"` to ensure the code is only called if the file is called directly 
5. First call worked. Now I need to put the call inside a loop. But I'm not sure how make sure 'quit' will exit the loop. 
6. I passed the existing print call with hard coded question. This created an infinite loop. What's the name of the method to get a text input from the user in console? `input`. 
7. Now I'm passing in `input("User: ")` to the while loop, which just repeats the input question. So I will save the response to a variable and then pass that into the api call. 
8. Response was empty. Wrapping in print statement.
9. Just had a multi-turn conversation. I asked it several questions, and then asked it to repeat the first question in the conversation. It say this was the first question. So this is conversation it has no memory. Now I need to get the "Quit" keyword to work. 
10. The answer is simple. Check what user input is. If they type in quit then break the loop. 
---

### Day 3 - Conversation Memory - Track message history
Create a `conversation_history` list that stores all user and assistant messages. Pass this full history to each API call.

**Date:** 12/24/2025
**Completed:** [X]  

**Notes:**

I started off by creating a new page with comment hints guiding me to reproducing yesterday's answer. The repetition is helpful, I only missed a few things. 

So, yesterday learned that the bot has no memory of previous questions because each call is a new conversation. So for this challenge I'm going to save each question/answer to a variable and pass that in as context to each call. 

This new variable gets initialized before the `while True` statement. I append the question to it. But then how do I save the answer? If conversation_history is a global variable I can append both to it. So I'll add it to the top. 

Inside the call_claude function I'm appanding conversation history twice: once with user message and once with the text of the convesation. The first question I told in my my name. Then the second question I asked it my name, but it didn't know. 

I have the variable and am printing it to console, but I'm not passing it to the api call. That's the issue. 

I created a prompt and pass in the conversation history using an f-string. But I'm wondering if conversation history now needsto be passed into call claude. I think it does.

How do I pass in an empty vairable? conversation_history=None

Got it. I have to append each turn of the conversation is a dictionary with role and content. Now it is able to remember previous parts of the conversation. 

---

### Day 4 - Streaming Responses - Real-time token display
Change it to display words as they're generated instead of waiting for complete response.
See documentation on [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming)

**Date:**  12/24/2025

**Completed:** [X]  

**Notes:**

I read the [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) documentation and followed the example there. 

I noticed a shift from assigning the api call to a variable to opening it temporarily using the `with` keyword, similar to how you could open a document in python. 

Then I noticed a change from `client.messages.create` to `client.messages.stream`. 

The `with` is paired to `as stream:`, which meant that I had to save the response as it was streaming, instead of accessing the entire reponse and parsing the response. This is probably incorrect, but it's how I got it working. 

Everything ele worked as is. 

Okay, looked into it and found the correct way to get the full repsonse text. 
```python
final_message = stream.get_final_message()
assistant_response = final_message.content[0].text
```

I asked the AI in my IDE for the answer because I didn't see it on the documentationl on streaming. 


---

### Day 5 - System Prompts - Add agent personality
Add a [system](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts) parameter to your API call with instructions that define your agent's personality, tone, and expertise.

**Date:**  12/24/2025

**Notes:**

This was super easy. All I had to do was pass in a "system" parameter with a new prompt. 

I did have an interesting conversation though. My prompt said it was a General Super Intelligence. But the model refused, saying it was actually not GSI and didn't want to deceive me. We have a nice philosophical conversation about it. 

---

### Day 6 - Save Conversations - Persist to JSON file
Use Python's `json` module to save `conversation_history` to a file when user quits, and load it on startup.

**Date:**  Dec 25, 2025

**Notes:** 



---

### Day 7 - Error Handling - Network errors, rate limits, graceful failures
Wrap API calls in try/except blocks to catch `APIError`, `APIConnectionError`, and `RateLimitError`. Display friendly error messages.

**Date:**  Dec 26, 2025

**Notes:**

I connected the repo to OpenAi's codex and asked for a code review. Here are the suggestions:

1. Split call_claude into smaller functions ✅
2. Centralize History Load/Save into smaller standalone functions ✅
3. Make history path configurable ✅
4. Add exceptions to handle APIError, APIConnectionError, and RateLimitError ✅
5. Append history only after success or record an error response. This will avoid partial history updates on failure. ✅
6. Add a KeyboardInterrupt handler during streaming ✅
7. Avoid Printing Entire History Every Time. Only print latest response. ✅
---


---

## Week 1 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 2:** [ ]

---

## Week 2: Tools

### Day 8 - First Tool - `get_current_time()` function
Create a simple Python function that returns current time. Define it in the `tools` parameter and let Claude decide when to call it.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 9 - Tool Calling Protocol - Understand request→tool→result flow
Add logging to see when Claude requests a tool, what parameters it sends, and how you return results in the next message.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 10 - Calculator Tool - Add function with parameters
Create a `calculate(operation, a, b)` function and define its schema with required parameters. Test with math questions.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 11 - Multiple Tools - Agent chooses between 4+ tools
Add weather, web search, file read, and random number tools. Ask questions requiring different tools to see Claude's selection logic.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 12 - Tool Error Handling - Graceful tool failures
Wrap tool execution in try/except. Return error messages to Claude so it can retry or explain the failure to the user.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 13 - Tool Logging - Track all tool calls
Create a `tool_log.json` file that records every tool call with timestamp, tool name, inputs, outputs, and success/failure status.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 14 - Simple Tools Collection - File reader, coin flip, dice roller
Build 5+ simple utility tools with clear descriptions. Test that Claude picks the right tool for diverse user requests.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 2 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 3:** [ ]

---

## Week 3-4: External World

### Day 15 - Web Search Setup - Integrate search API
Sign up for a search API (Brave, Serper, or Tavily). Store API key in `.env` and test basic search queries.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 16 - Parse Search Results - Extract clean data
Write a function that takes raw search JSON and extracts title, snippet, URL into a clean format Claude can use.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 17 - Web Search Tool - Agent searches autonomously
Add web search as a tool. Claude should now be able to search the internet when it needs current information.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 18 - Fetch Web Pages - Get full page content
Use `requests` + `BeautifulSoup` to create a tool that fetches and extracts main text content from URLs.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 19 - Search + Fetch Chain - Multi-step tool usage
Ask Claude a research question. It should search, then fetch relevant pages, then synthesize an answer with citations.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 20 - Summarization - Condense long text
Create a tool that chunks long documents and asks Claude to summarize each chunk, then combine summaries.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 21 - Source Citations - Track information sources
Modify your tools to return source metadata. Prompt Claude to always cite sources in its responses.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 22 - Conversation Summarization - Compress old messages
When conversation exceeds 10 messages, summarize oldest messages into a single context message to save tokens.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 23 - Vector Database Setup - Install ChromaDB
`pip install chromadb`. Create a collection and test adding/querying a few text chunks with embeddings.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 24 - Generate Embeddings - Create text embeddings
Use Voyage AI or OpenAI embeddings API to convert text chunks into vectors. Store them in ChromaDB.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 25 - Semantic Search - Find similar chunks
Build a tool that takes a query, creates its embedding, and returns top-k most similar chunks from your vector database.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 26 - Document Chunking - Split docs intelligently
Create a function that splits documents by paragraphs or sentences while keeping chunks under 500 tokens with some overlap.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 27 - Metadata Filtering - Filter by source, date
Add metadata (source, date, category) to chunks. Modify search tool to filter results by these attributes.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 28 - Hybrid Search - Combine keyword and semantic
Implement BM25 keyword search alongside vector search. Combine and rerank results from both approaches.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 3-4 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 5:** [ ]

---

## Week 5-6: Memory & RAG Systems

### Day 29 - Reranking - Two-stage retrieval
Use a reranking model (Cohere or cross-encoder) to score and reorder your retrieved chunks for better relevance.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 30 - PROJECT: Personal Knowledge Base
Build a complete system: upload PDFs/text files, chunk and embed them, then chat with your documents using RAG.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 31 - Advanced RAG - Query Rewriting
Before retrieving, ask Claude to rewrite the user's vague question into 2-3 specific search queries for better results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 32 - Multi-Query RAG - Multiple search queries
Generate 3 different query variations, retrieve docs for each, combine and deduplicate results before answering.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 33 - Agentic RAG - Agent decides when to retrieve
Don't auto-retrieve. Give Claude a "search_knowledge_base" tool and let it decide when it needs to look things up.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 34 - Citation & Source Tracking - No hallucinations
Format retrieved chunks with [Source 1], [Source 2] markers. Prompt Claude to cite specific sources for every claim.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 35 - Conversation + RAG Integration - Memory + knowledge
Combine conversation memory with RAG. Agent remembers chat history AND can retrieve from knowledge base simultaneously.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 36 - Chain-of-Thought Prompting - Step-by-step reasoning
Add "Think step-by-step" to your system prompt. Compare answers with and without CoT for complex problems.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 37 - Few-Shot Learning - Examples in prompts
For structured tasks (extraction, classification), provide 3-5 examples in your system prompt showing desired input→output.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 38 - Self-Consistency - Multiple reasoning paths
For important questions, ask Claude to generate 3 different reasoning chains, then pick the most common answer.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 39 - Tool-Enhanced CoT - Reasoning + tools
Prompt Claude to explain its reasoning before using tools, then verify results after tool execution.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 40 - Error Recovery - Agent fixes own mistakes
When a tool fails or returns unexpected results, let Claude see the error and ask it to try a different approach.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 41 - Verification Loop - Agent checks its work
After generating an answer, ask Claude to critique it and identify potential errors before showing to user.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 42 - PROJECT: Research Assistant
Build an agent that takes a research question, searches web, reads papers, synthesizes findings with citations.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 5-6 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 7:** [ ]

---

## Week 7-8: Memory Architecture

### Day 43 - Short-Term Memory - Recent conversation buffer
Keep last 10 messages in full detail while older messages get summarized. Implement a sliding window.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 44 - Long-Term Memory - Persistent user facts
Extract facts about the user ("prefers Python," "works at Google") and store them in a separate context that persists across sessions.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 45 - Working Memory - Task-specific context
For complex multi-step tasks, maintain a separate "working memory" that tracks progress, next steps, and intermediate results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 46 - Memory Retrieval - Smart context selection
When context gets large, retrieve only relevant memories based on current query instead of loading everything.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 47 - Hybrid Search - Combine keyword and semantic search
Apply the same hybrid search from Day 28 to your memory retrieval—search memories by both keywords and semantic similarity.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 48 - Memory Consolidation - Summarize and compress
Periodically review old memories and consolidate similar facts, remove duplicates, and compress detailed logs.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 49 - Episodic Memory - Store specific interactions
Save complete conversation episodes with timestamps. Let agent recall "what we discussed last Tuesday about X."

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 50 - Memory Retrieval Strategy - Relevance ranking
Implement scoring for memories: recency + relevance + importance. Retrieve top-k memories instead of all.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 7-8 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 9:** [ ]

---

## Week 8-9: Planning & Reasoning

### Day 51 - Chain-of-Thought - Force step-by-step reasoning
Add explicit "reasoning" section to prompts. Make Claude show its work before answering.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 52 - Tree of Thoughts - Explore multiple paths
For complex problems, ask Claude to explore 3 different solution approaches before committing to one.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 53 - ReAct Pattern - Reasoning + Acting loop
Implement Thought→Action→Observation cycle. Agent thinks, acts with tools, observes results, and repeats.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 54 - Task Decomposition - Break into subtasks
Give Claude a complex task and ask it to break it into numbered subtasks before executing each one.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 55 - Plan-Execute Pattern - Separate planning/execution
First pass: Claude creates a detailed plan. Second pass: Execute each step of the plan with separate API calls.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 56 - Self-Ask - Agent asks clarifying questions
Before answering vague queries, prompt Claude to ask 2-3 clarifying questions to understand user intent better.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 57 - Reflexion - Agent critiques own outputs
After generating a response, ask Claude to identify weaknesses or errors in its own answer and improve it.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 58 - Goal Stack - Hierarchical goal structure
Maintain a stack of goals/subgoals. Agent pops completed goals and tracks progress toward main objective.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 59 - Iterative Refinement - Multiple improvement passes
Generate initial answer, then run 2-3 refinement passes asking Claude to improve clarity, accuracy, and completeness.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 60 - Constraint Satisfaction - Meet requirements
Give Claude explicit constraints (word limit, must include 3 examples, etc.). Verify outputs meet all constraints.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 61 - Backtracking - Recover from failures
When an approach fails, store it in "tried_approaches" and ask Claude to try a different method.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 62 - Verification Loop - Check own work
After task completion, run verification prompts: "Are there any errors? Did we miss anything?"

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 63 - Meta-Prompting - Agent writes prompts
Give Claude a task and ask it to first write the optimal prompt for solving it, then execute using that prompt.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 64 - Reasoning Traces - Log thought processes
Save all intermediate reasoning steps to a file for debugging and understanding agent's decision-making.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 65 - Adaptive Strategies - Switch approaches
Define different strategies (fast/thorough, creative/analytical). Let Claude choose based on task type.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 8-9 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 10:** [ ]

---

## Week 10-11: Multi-Agent Systems

### Day 66 - Two-Agent Dialogue - Agents discuss problems
Create two agents with different personalities. Have them discuss a topic back-and-forth for 5 turns.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 67 - Agent Communication Protocol - Message passing
Define a structured message format (JSON) for agents to exchange information, requests, and results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 68 - Specialist Agents - Domain experts
Create 3 specialized agents: Researcher, Coder, Writer. Each has different system prompts and tools.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 69 - Agent Orchestration - Central coordinator
Build a coordinator agent that receives user requests and delegates to specialist agents based on task type.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 70 - Debate Pattern - Agents argue perspectives
Create two agents arguing opposite sides of a question. Third "judge" agent picks the best argument.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 71 - Ensemble Voting - Vote on best answer
Generate answers from 3 agents independently. Combine them or vote on the best response.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 72 - Agent Handoff - Pass tasks between agents
Agent 1 does research, passes findings to Agent 2 who writes report. Maintain context across handoff.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 73 - Hierarchical Agents - Manager/worker structure
Manager agent breaks task into subtasks and assigns each to worker agents. Manager synthesizes results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 74 - Collaborative RAG - Multiple knowledge bases
Each agent has access to different knowledge bases. They collaborate to answer questions requiring multiple sources.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 75 - Agent Market - Bid on tasks
Agents "bid" on tasks based on their confidence/expertise. Coordinator selects the best agent for each task.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 76 - Consensus Building - Negotiate understanding
Agents propose answers, discuss disagreements, and iteratively refine until they reach consensus.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 77 - Parallel Agent Execution - Simultaneous work
Use `asyncio` to run multiple agents simultaneously. Combine results once all complete.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 78 - Agent Swarms - Many simple agents
Create 10+ simple agents with single-purpose tools. Swarm solves problems through collective behavior.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 79 - Meta-Agent - Creates/manages other agents
Build an agent that can spawn new specialized agents dynamically based on user requirements.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 80 - Multi-Agent Memory - Shared knowledge
All agents read/write to a shared memory store. Updates from one agent are visible to others.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 10-11 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 12:** [ ]

---

## Week 12: Advanced Capabilities

### Day 81 - Input Validation - Detect prompt injections
Check user inputs for injection patterns ("Ignore previous instructions"). Reject or sanitize malicious inputs.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 82 - Output Filtering - Content safety
Screen agent outputs for harmful content, PII, or policy violations before displaying to user.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 83 - Hallucination Detection - Verify claims
When agent makes factual claims, verify them against retrieved sources or search results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 84 - Uncertainty Quantification - Confidence levels
Prompt agent to express confidence (high/medium/low) for each claim. Lower confidence = search for verification.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 85 - Evaluation Harness - Automated testing
Create 20 test cases with expected outputs. Run agent on all tests and calculate pass rate.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 86 - A/B Testing Framework - Compare configurations
Run same queries through two different system prompts or settings. Compare quality, cost, and latency.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 87 - Prompt Optimization - Auto-improve prompts
Generate variations of your system prompt. Test each on validation set and keep the best performer.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 88 - Few-Shot Learning - Dynamic example selection
Store example library. For each query, retrieve most similar examples and include them in the prompt.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 89 - Agent Fine-Tuning Data - Collect training data
Log all user queries and agent responses. Format them as training examples for future fine-tuning.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 90 - RLHF - Basic reinforcement learning
Add thumbs up/down to responses. Use feedback to identify high/low quality outputs for training data.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 12 Reflection

**What went well:**

**What was hard:**

**Key insights:**

**Ready for Week 13:** [ ]

---

## Week 13-14: Production

### Day 91 - API Wrapper - REST API with FastAPI
Install FastAPI. Create POST `/chat` endpoint that accepts messages and returns agent responses.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 92 - Rate Limiting - Control request frequency
Use `slowapi` to limit requests per IP (10/minute). Return 429 status when limit exceeded.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 93 - Caching Layer - Cache expensive calls
Use Redis to cache identical queries. Check cache before calling LLM to save costs.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 94 - Async Processing - Long-running tasks
Use Celery + Redis for tasks taking >30 seconds. Return task ID immediately, poll for results.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 95 - Monitoring & Alerting - Track performance
Add Prometheus metrics: request count, latency, errors, token usage. Set up alerts for anomalies.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 96 - User Session Management - Multiple users
Use JWT tokens for auth. Store each user's conversation history separately in database.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 97 - Cost Optimization - Smart model routing
Route simple queries to fast/cheap model (Haiku). Complex queries to powerful model (Opus). Track savings.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 98 - Deployment Pipeline - Container & deploy
Write Dockerfile. Set up GitHub Actions to build and deploy to cloud (Railway/Render) on every push.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 99 - Load Testing - Stress test agent
Use `locust` to simulate 100 concurrent users. Identify bottlenecks and optimize.

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

### Day 100 - Complete Agent System - End-to-end production
Polish your entire system, write comprehensive README, create demo video, deploy publicly, and share your journey!

**Date:**  
**Completed:** [ ]  

**What I built:**

**What I learned:**

**Challenges:**

**Notes:**

---

## Week 13-14 Reflection

**What went well:**

**What was hard:**

**Key insights:**

---

## Overall Progress

**Days completed:** 1/100  
**Current streak:** 0 days  
**Longest streak:** 0 days  
**Start date:** Dec 22, 2025  
**Projected end date:**  

## Key Milestones

- [ ] Day 10: First tool-using agent
- [ ] Day 28: Agent with memory
- [ ] Day 42: Agent that reasons
- [ ] Day 56: Intelligent search
- [ ] Day 70: Planning agent
- [ ] Day 84: Multi-agent system
- [ ] Day 98: Production deployment
- [ ] Day 100: Complete!

## Insights & Learnings

**Big breakthroughs:**

**Common mistakes I made:**

**Best practices I discovered:**

**Resources that helped:**

## Ideas for Extensions

(Things you want to add beyond the 100 days)

-
-
-

---

**Remember:** This is YOUR journey. There's no rush. Understanding > Speed.
