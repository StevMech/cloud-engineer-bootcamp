# Setup Guide - Cloud Engineer Bootcamp

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10 or higher** installed
- **pip** package manager
- **Git** for version control
- **Terminal/Command Prompt** access
- **Text editor** (VS Code, Sublime, etc.)
- **Motivation and commitment** to learn! 💪

## Step-by-Step Installation

### 1. Check Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed or version is below 3.10, download from [python.org](https://www.python.org/downloads/).

### 2. Clone the Repository

```bash
git clone https://github.com/StevMech/cloud-engineer-bootcamp.git
cd cloud-engineer-bootcamp
```

### 3. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your prompt, indicating the virtual environment is active.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required packages including:
- OpenAI/Anthropic for AI mentoring
- Rich for beautiful CLI output
- Typer for command-line interface
- And more...

### 5. Configure AI Provider

Create a `.env` file in the project root:

```bash
# On Linux/macOS
touch .env

# On Windows
type nul > .env
```

Edit `.env` and add your API key:

#### Option A: OpenAI (Recommended)

```bash
OPENAI_API_KEY=sk-your-openai-api-key-here
```

**How to get an OpenAI API key:**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste into `.env`

**Cost**: ~$0.01-0.02 per interaction with GPT-4

#### Option B: Anthropic Claude

```bash
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key-here
```

**How to get an Anthropic API key:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Generate API key
4. Copy and paste into `.env`

#### Option C: Ollama (Free, Local)

If you want to run AI models locally without API costs:

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Download a model:
   ```bash
   ollama pull llama2
   ```
3. Update `config.yaml`:
   ```yaml
   ai_provider: "ollama"
   ollama_model: "llama2"
   ```
4. No API key needed!

**Note**: Ollama requires more system resources but is completely free.

### 6. Verify Installation

```bash
python mentor_agent.py --help
```

You should see the available commands and options.

### 7. Test the Mentor Agent

```bash
python mentor_agent.py start
```

If everything is set up correctly, you'll see the welcome screen!

## Troubleshooting

### "Python command not found"

- Make sure Python is installed and in your PATH
- Try `python3` instead of `python`
- On Windows, check "Add Python to PATH" during installation

### "Module not found" errors

```bash
# Activate virtual environment first
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Then reinstall
pip install -r requirements.txt
```

### "API key not found" warnings

- Check that `.env` file exists in the project root
- Verify the API key is correct (no extra spaces)
- Restart the application after adding the key

### Virtual environment not activating

**Linux/macOS:**
```bash
# If using bash
source venv/bin/activate

# If using fish
source venv/bin/activate.fish

# If using csh
source venv/bin/activate.csh
```

**Windows:**
```cmd
# Command Prompt
venv\Scripts\activate.bat

# PowerShell
venv\Scripts\Activate.ps1

# If PowerShell gives execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Permission errors on Linux/macOS

```bash
chmod +x mentor_agent.py
```

## System Requirements

### Minimum
- **CPU**: Dual-core processor
- **RAM**: 4GB
- **Storage**: 2GB free space
- **Internet**: Required for AI API calls

### Recommended
- **CPU**: Quad-core processor
- **RAM**: 8GB or more
- **Storage**: 10GB free space (for practice labs)
- **Internet**: Stable broadband connection

## Next Steps

Once installation is complete:

1. Read the [Usage Guide](usage.md)
2. Review the [Full Curriculum](../CURRICULUM.md)
3. Start your first lesson:
   ```bash
   python mentor_agent.py start
   ```

## Getting Help

- **Documentation**: Check `docs/` folder
- **FAQ**: See [faq.md](faq.md)
- **Issues**: Open an issue on GitHub
- **Mentor**: Ask your AI mentor anytime!

## Optional: IDE Setup

### Visual Studio Code

Recommended extensions:
- Python
- Markdown All in One
- Docker
- Kubernetes
- YAML

### PyCharm

Configure the Python interpreter to use the virtual environment:
1. File → Settings → Project → Python Interpreter
2. Add Interpreter → Existing Environment
3. Select `venv/bin/python` (or `venv\Scripts\python.exe` on Windows)

## Optional: Docker Setup

If you want to practice in isolated containers:

```bash
# Install Docker Desktop
# Visit docker.com for your OS

# Pull Ubuntu image
docker pull ubuntu:22.04

# Run interactive container
docker run -it ubuntu:22.04 bash
```

---

**Ready to start? Head to [Usage Guide](usage.md)! 🚀**
