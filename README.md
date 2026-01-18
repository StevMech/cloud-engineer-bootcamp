# 🚀 Cloud Engineer Bootcamp - AI Mentor Agent

An intelligent AI-powered mentor agent designed to guide you through an intensive 8-week cloud platform engineering bootcamp. Transform from beginner to job-ready cloud engineer with structured daily lessons, hands-on labs, and continuous assessment.

## 🎯 What You'll Learn

In just 8 weeks, master the essential skills to become a highly employable cloud platform engineer:

- **Weeks 1-2**: Linux fundamentals, networking, scripting (Bash/Python), Git
- **Weeks 3-4**: Docker, Kubernetes, container orchestration, Helm
- **Weeks 5-6**: CI/CD pipelines, GitHub Actions, Terraform, GitOps
- **Weeks 7-8**: Cloud platforms (AWS/Azure/GCP), monitoring, security, production readiness

## ✨ Features

### 🤖 Intelligent Mentor Agent
- **Conversational AI**: Natural language interaction for learning and guidance
- **Adaptive Learning**: Adjusts difficulty based on your performance
- **24/7 Availability**: Get help whenever you need it
- **Code Review**: Receive feedback on your implementations
- **Interview Prep**: Practice common platform engineer interview questions

### 📚 Structured Curriculum
- **40 Daily Lessons**: Comprehensive coverage of platform engineering
- **Daily Schedule**: Morning theory, afternoon labs, evening review
- **Hands-on Labs**: Real-world scenarios and practical exercises
- **Weekly Assessments**: Test your knowledge and skills
- **Portfolio Projects**: Build impressive projects for your resume

### 📊 Progress Tracking
- **Daily Completion**: Track your daily learning progress
- **Skill Proficiency**: Monitor your skill development
- **Streaks & Badges**: Stay motivated with gamification
- **Visual Dashboards**: See your progress at a glance

### 🎓 Job Readiness
- **Resume Projects**: 3-4 portfolio projects to showcase
- **Interview Practice**: Scenario-based problem-solving
- **Best Practices**: Industry standards and conventions
- **Documentation Skills**: Technical writing and runbooks

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Basic computer literacy
- Motivation to learn!

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/StevMech/cloud-engineer-bootcamp.git
   cd cloud-engineer-bootcamp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your AI provider**
   
   Create a `.env` file in the project root:
   ```bash
   # For OpenAI (recommended)
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Or for Anthropic Claude
   # ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Or use Ollama (local, free)
   # No API key needed - just install Ollama
   ```

5. **Start the mentor agent**
   ```bash
   python mentor_agent.py
   ```

## 💡 Usage

### Starting Your First Day

```bash
python mentor_agent.py start
```

The mentor will guide you through:
1. Introduction and goal setting
2. Daily lesson plan
3. Hands-on exercises
4. Progress review

### Available Commands

```bash
# Start a new learning session
python mentor_agent.py start

# Continue from where you left off
python mentor_agent.py continue

# Take a weekly assessment
python mentor_agent.py assess --week 1

# Review your progress
python mentor_agent.py progress

# Get help on a specific topic
python mentor_agent.py ask "How do Kubernetes pods work?"

# Practice interview questions
python mentor_agent.py interview

# Work on portfolio projects
python mentor_agent.py project

# Daily standup (reflect on progress)
python mentor_agent.py standup
```

### Daily Schedule

Each day follows a structured learning schedule:

```
🌅 Morning (09:00-11:00): Theory & Concepts
   - Learning objectives
   - Conceptual explanations
   - Best practices
   - Q&A with the mentor

☀️ Afternoon (14:00-17:00): Hands-On Practice
   - Guided lab exercises
   - Progressive challenges
   - Real-world scenarios
   - Troubleshooting

🌙 Evening (19:00-20:00): Review & Reinforcement
   - Summary and reflection
   - Quick quiz
   - Next day preview
```

## 📖 Curriculum Overview

### Week 1-2: Foundations
**Goal**: Master Linux, networking, and scripting fundamentals

**Topics**:
- Linux command line mastery
- File systems, processes, permissions
- Networking (TCP/IP, DNS, HTTP/HTTPS)
- Bash scripting and automation
- Python for DevOps
- Git version control

**Assessment**: Linux admin tasks, network troubleshooting, script writing

### Week 3-4: Containerization & Orchestration
**Goal**: Build and deploy containerized applications

**Topics**:
- Docker fundamentals
- Multi-container apps with Docker Compose
- Kubernetes architecture
- Deployments, services, ingress
- Helm package management
- Container security

**Assessment**: Deploy multi-tier application on Kubernetes

### Week 5-6: CI/CD & Infrastructure as Code
**Goal**: Automate deployments and infrastructure

**Topics**:
- CI/CD pipeline design
- GitHub Actions workflows
- Terraform infrastructure provisioning
- GitOps with ArgoCD
- Configuration management
- Secrets management

**Assessment**: Complete CI/CD pipeline with IaC

### Week 7-8: Cloud Platforms & Production
**Goal**: Deploy production-ready cloud applications

**Topics**:
- Cloud provider fundamentals (AWS/Azure/GCP)
- Compute, storage, networking services
- Kubernetes on cloud (EKS/AKS/GKE)
- Monitoring and observability
- Security best practices
- Cost optimization
- Incident response

**Assessment**: Production-ready cloud application

## 🎯 Learning Outcomes

By completing this bootcamp, you will be able to:

✅ Confidently use Linux command line and scripting  
✅ Build and deploy containerized applications  
✅ Manage Kubernetes clusters and workloads  
✅ Create automated CI/CD pipelines  
✅ Provision infrastructure using Terraform  
✅ Deploy applications on cloud platforms  
✅ Implement monitoring and observability  
✅ Apply security best practices  
✅ Troubleshoot production issues  
✅ Pass platform engineering interviews  

## 📁 Project Structure

```
cloud-engineer-bootcamp/
├── mentor_agent.py              # Main mentor agent application
├── progress_tracker.py          # Progress tracking system
├── config.yaml                  # Configuration settings
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── CURRICULUM.md               # Complete 8-week curriculum
├── curriculum/                 # Daily lesson plans
│   ├── week1/
│   ├── week2/
│   └── ...
├── exercises/                  # Hands-on lab exercises
│   ├── week1/
│   ├── week2/
│   └── ...
├── assessments/               # Weekly assessments
│   ├── week1_assessment.md
│   └── ...
├── resources/                 # Learning resources
│   ├── cheatsheets/
│   ├── templates/
│   └── links.md
├── progress/                  # Your progress (gitignored)
└── docs/                      # Documentation
    ├── setup.md
    ├── usage.md
    └── faq.md
```

## 🤝 Contributing

While this bootcamp is primarily for individual learning, contributions are welcome!

- **Content Improvements**: Enhance lessons or exercises
- **Bug Fixes**: Report and fix issues
- **Feature Requests**: Suggest new features
- **Resources**: Share helpful learning resources

## 📝 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built with:
- OpenAI GPT-4 / Anthropic Claude for AI mentoring
- Rich and Typer for beautiful CLI experience
- Community resources and best practices

## 📞 Support

- **Documentation**: Check the `docs/` folder
- **Issues**: Open an issue on GitHub
- **FAQ**: See `docs/faq.md`

## 🎓 Success Stories

Track your journey and share your success! Tag us when you:
- Complete the bootcamp
- Land your first cloud engineering role
- Build amazing projects

---

**Ready to start your cloud engineering journey? Let's go! 🚀**

```bash
python mentor_agent.py start
```
