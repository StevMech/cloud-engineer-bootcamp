# Frequently Asked Questions (FAQ)

## General Questions

### Q: Do I need prior experience to start this bootcamp?

**A**: No! The bootcamp is designed for beginners. We start with Linux basics and progressively build up to advanced cloud engineering topics. However, basic computer literacy (using a terminal, installing software) is helpful.

### Q: How much time do I need to commit daily?

**A**: The structured schedule requires 6 hours per day:
- Morning: 2 hours (theory)
- Afternoon: 3 hours (hands-on)
- Evening: 1 hour (review)

However, you can adjust the pace to fit your schedule. The content is self-paced.

### Q: Can I complete this bootcamp while working full-time?

**A**: Yes! Many students do 2-3 hours on weekday evenings and catch up on weekends. The 8-week timeline may extend to 12-16 weeks, which is perfectly fine.

### Q: Is this bootcamp free?

**A**: The bootcamp materials are free and open-source. However, you'll need:
- AI API access (OpenAI: ~$5-10/month, or free with Ollama)
- Cloud provider free tier accounts (AWS/Azure/GCP have free tiers)
- Optional: Linux system or VM

### Q: Which cloud provider should I focus on?

**A**: We recommend AWS as it has the largest market share, but the concepts apply to Azure and GCP too. You can configure your preference in `config.yaml`.

## Technical Questions

### Q: What operating system do I need?

**A**: Any modern OS works:
- **Linux**: Native environment, recommended
- **macOS**: Unix-based, great for learning
- **Windows**: Use WSL2 (Windows Subsystem for Linux) or a Linux VM

### Q: Can I use Ollama instead of OpenAI/Anthropic?

**A**: Yes! Ollama allows you to run AI models locally for free. Install Ollama, download a model (e.g., llama2), and update `config.yaml`:

```yaml
ai_provider: "ollama"
ollama_model: "llama2"
```

No API key needed, but requires more system resources (8GB+ RAM recommended).

### Q: The AI mentor isn't responding. What should I do?

**A**: Check these common issues:
1. Verify API key in `.env` file
2. Check internet connection
3. Ensure you have API credits (OpenAI/Anthropic)
4. Try running in demo mode (no API key) - limited functionality

### Q: How do I get an OpenAI API key?

**A**: 
1. Visit [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to API Keys section
4. Create new key
5. Add to `.env` file: `OPENAI_API_KEY=sk-...`

### Q: What if I can't afford API costs?

**A**: Options:
1. **Ollama**: Free, local AI (recommended)
2. **Demo mode**: Read curriculum files directly without AI
3. **Free trials**: OpenAI offers $5 free credit for new users
4. **Share costs**: Study with friends and share an account

## Curriculum Questions

### Q: Can I skip weeks I already know?

**A**: Yes! While we recommend following the sequence, you can jump ahead or focus on specific topics using the `ask` command. However, completing assessments ensures you haven't missed critical concepts.

### Q: What if I fail a weekly assessment?

**A**: 
1. Review the week's material
2. Ask the mentor for clarification
3. Practice the exercises again
4. Retake the assessment (up to 3 attempts)
5. Focus on weak areas identified

### Q: Are there solutions to the exercises?

**A**: Some exercises include solutions in separate files. However, we encourage attempting them first and asking the mentor for help rather than jumping to solutions.

### Q: Can I add my own curriculum content?

**A**: Absolutely! The bootcamp is open-source. You can:
- Add new curriculum files to `curriculum/`
- Create custom exercises in `exercises/`
- Share your additions with the community

## Progress & Completion

### Q: How is progress tracked?

**A**: Progress is stored locally in `progress/user_progress.json`. It tracks:
- Current week and day
- Completed days and assessments
- Learning streak
- Skill proficiency levels
- Earned badges
- Portfolio projects

### Q: What happens if I miss a day?

**A**: Your streak resets, but all other progress is saved. You can continue where you left off. Consistency is key, but life happens - don't stress about breaks!

### Q: Do I get a certificate upon completion?

**A**: Currently, no formal certificate is issued. However, completing the bootcamp gives you:
- Portfolio projects for your GitHub
- Hands-on experience for your resume
- Knowledge for industry certifications (AWS, CKA, etc.)
- Interview preparation

### Q: How do I prove I completed the bootcamp?

**A**: 
1. **GitHub Portfolio**: Share your completed projects
2. **Blog Posts**: Write about your learning journey
3. **Progress Export**: `python mentor_agent.py progress` generates a report
4. **Certifications**: Take official cloud/Kubernetes certifications

## Job Readiness

### Q: Will this bootcamp get me a job?

**A**: The bootcamp provides the technical foundation, but job hunting requires:
- Completing the curriculum
- Building strong portfolio projects
- Networking with professionals
- Practicing interviews
- Tailoring resumes
- Applying consistently

Think of this as necessary but not sufficient - you'll be well-prepared, but still need to put in the job search effort.

### Q: What jobs can I apply for after completion?

**A**: 
- Cloud Engineer
- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer (SRE)
- Infrastructure Engineer
- Kubernetes Administrator
- CI/CD Engineer

Entry-level positions typically require 0-2 years experience, which you can demonstrate through projects.

### Q: Should I get certifications after this?

**A**: Recommended certifications to pursue:
- **AWS Solutions Architect Associate**
- **Certified Kubernetes Administrator (CKA)**
- **HashiCorp Terraform Associate**
- **Cloud Provider specific (Azure/GCP)**

These validate your knowledge and help on job applications.

### Q: How important are the portfolio projects?

**A**: Very important! Employers want to see:
- Real implementations, not just theoretical knowledge
- GitHub repositories with good documentation
- Understanding of best practices
- Problem-solving skills

Spend extra time making your projects professional and well-documented.

## Technical Issues

### Q: "Command not found: python"

**A**: Try:
```bash
python3 mentor_agent.py start
```

Or add an alias:
```bash
alias python=python3
```

### Q: Virtual environment not activating

**A**: 
**Linux/macOS**:
```bash
source venv/bin/activate
```

**Windows PowerShell**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

### Q: "Module not found" errors

**A**:
```bash
# Ensure virtual environment is active
source venv/bin/activate  # or venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Q: API rate limit errors

**A**: 
- **OpenAI**: Free tier has limits. Upgrade or wait.
- **Anthropic**: Similar rate limits apply.
- **Solution**: Switch to Ollama for unlimited local use.

### Q: Progress file corrupted

**A**:
```bash
# Backup current progress
cp progress/user_progress.json progress/user_progress.json.backup

# Reset progress
python mentor_agent.py reset

# Or manually fix the JSON file
```

## Content Questions

### Q: Some curriculum days are missing content

**A**: The bootcamp includes detailed content for key days as examples. You can:
1. Use the CURRICULUM.md overview for all topics
2. Ask the AI mentor for specific day content
3. Reference the learning objectives and create your own notes
4. Contribute by adding missing content!

### Q: Are there video tutorials?

**A**: Currently, the bootcamp is text-based. However, the resources section (`resources/links.md`) includes curated video tutorials and courses for each topic.

### Q: Can I use this to prepare for certifications?

**A**: Yes! The bootcamp covers topics in:
- AWS Solutions Architect Associate
- Certified Kubernetes Administrator (CKA)
- Terraform Associate

However, you'll need additional certification-specific study materials for exam-specific formats and questions.

## Community

### Q: Is there a community or forum?

**A**: Currently, use GitHub Discussions and Issues. Consider joining:
- DevOps Discord servers
- Kubernetes Slack
- Cloud Native Computing Foundation (CNCF) communities
- Reddit: r/devops, r/kubernetes, r/aws

### Q: Can I contribute to the bootcamp?

**A**: Yes! Contributions welcome:
- Add curriculum content
- Create exercises
- Improve documentation
- Fix bugs
- Share your learning experience

See CONTRIBUTING.md for guidelines.

### Q: How do I get help if stuck?

**A**: 
1. Ask the AI mentor: `python mentor_agent.py ask "your question"`
2. Review documentation and curriculum
3. Search online (Stack Overflow, documentation)
4. Open a GitHub issue
5. Join community forums

## Miscellaneous

### Q: Can I use this for teaching others?

**A**: Yes! The bootcamp is open-source (MIT License). You can:
- Use it to teach students
- Adapt it for corporate training
- Share with study groups
- Modify for your needs

Please retain attribution and share improvements with the community.

### Q: How often is the content updated?

**A**: The bootcamp aims to stay current with cloud engineering best practices. Check GitHub for updates and new releases.

### Q: Is this bootcamp affiliated with any company?

**A**: No, this is an independent, open-source project. It's not affiliated with AWS, Google, Microsoft, or any certification body.

### Q: Can I do this bootcamp with friends?

**A**: Absolutely! Study groups are encouraged:
- Share progress and tips
- Work on projects together
- Practice interview questions
- Review each other's code

---

**Still have questions? Ask your AI mentor or open an issue on GitHub! 🚀**
