# Quick Start Guide

Get started with the Cloud Engineer Bootcamp in 5 minutes!

## 1. Prerequisites

- Python 3.10+ installed
- Terminal access
- Text editor

## 2. Installation (2 minutes)

```bash
# Clone the repository
git clone https://github.com/StevMech/cloud-engineer-bootcamp.git
cd cloud-engineer-bootcamp

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 3. Configuration (1 minute)

**Option A: With AI (Recommended)**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Get free key at: https://platform.openai.com
nano .env  # or use your favorite editor
```

**Option B: Demo Mode (No API Key)**
Skip this step! The bootcamp works in demo mode without AI features.

## 4. Start Learning! (2 minutes)

```bash
# Start the bootcamp
python mentor_agent.py start

# Or explore available commands
python mentor_agent.py --help

# Ask a question
python mentor_agent.py ask "What is Docker?"

# View resources
python mentor_agent.py resources

# Check progress
python mentor_agent.py progress
```

## 5. Daily Workflow

```bash
# Morning: Start your day
python mentor_agent.py standup

# Throughout the day: Learn
python mentor_agent.py start

# Ask questions as you go
python mentor_agent.py ask "How do I fix this error?"

# Evening: Check progress
python mentor_agent.py progress
```

## Common Commands

```bash
python mentor_agent.py start       # Begin/continue learning
python mentor_agent.py ask "..."   # Ask AI mentor
python mentor_agent.py progress    # View your progress
python mentor_agent.py assess --week 1  # Take assessment
python mentor_agent.py interview   # Practice interviews
python mentor_agent.py resources   # View learning resources
```

## Troubleshooting

**"Module not found" errors:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**"API key not found" warnings:**
- Add OPENAI_API_KEY to .env file, or
- Use demo mode (manual curriculum reading)

**Need help?**
- Check `docs/faq.md`
- Read `docs/setup.md`
- Open an issue on GitHub

## Next Steps

1. Complete Week 1, Day 1 curriculum
2. Work through the exercises
3. Take the Week 1 assessment
4. Build your first portfolio project

---

**Ready? Let's start your cloud engineering journey! 🚀**

```bash
python mentor_agent.py start
```
