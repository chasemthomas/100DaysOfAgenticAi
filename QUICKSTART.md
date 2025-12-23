# Quick Start - Get Running in 5 Minutes

## Step 1: Setup Environment

```bash
# Navigate to project folder
cd 100-day-agent-course

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Add API Key

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your key
# ANTHROPIC_API_KEY=sk-ant-...
```

Get your API key: https://console.anthropic.com/

## Step 3: Start Day 1

Open `agent.py` and write your first code:

```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(message.content[0].text)
```

## Step 4: Run It

```bash
export ANTHROPIC_API_KEY=your_key_here  # or use python-dotenv
python agent.py
```

You should see a response from Claude!

## Step 5: Commit Day 1

```bash
git init
git add .
git commit -m "Day 1: First API response"
git tag day-1
```

## What's Next?

- [ ] Mark Day 1 complete in README.md
- [ ] Update JOURNAL.md with your notes
- [ ] Tomorrow: Add a conversation loop (Day 2)

---

## Troubleshooting

**"No module named anthropic"**  
→ Did you activate venv? Run: `pip install -r requirements.txt`

**"API key not found"**  
→ Create `.env` file with your key, or export it in terminal

**Still stuck?**  
→ Check the full README.md for detailed instructions

---

You're building an AI agent from scratch. Let's go! 🚀
