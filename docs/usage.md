# Usage Guide - Cloud Engineer Bootcamp

## Getting Started

After installation, you're ready to begin your cloud engineering journey!

## Core Commands

### Starting the Bootcamp

```bash
python mentor_agent.py start
```

**First time**: You'll be prompted for your name and goals  
**Returning**: Continues from where you left off

### Asking Questions

```bash
python mentor_agent.py ask "What is Kubernetes?"
```

Get instant answers from your AI mentor about any topic.

### Checking Progress

```bash
python mentor_agent.py progress
```

View your:
- Current week and day
- Days completed
- Learning streak
- Earned badges
- Skill proficiency levels

### Taking Assessments

```bash
python mentor_agent.py assess --week 1
```

Take weekly assessments to test your knowledge.

### Daily Standup

```bash
python mentor_agent.py standup
```

Reflect on:
- What you learned yesterday
- What you'll focus on today
- Any challenges or blockers

Get personalized feedback and motivation!

### Interview Practice

```bash
python mentor_agent.py interview
```

Practice real platform engineering interview questions with feedback.

### Finding Resources

```bash
python mentor_agent.py resources
```

Access curated learning materials, cheat sheets, and documentation.

### Resetting Progress

```bash
python mentor_agent.py reset
```

⚠️ **Caution**: This erases all progress. Use only if starting over.

## Daily Workflow

### Recommended Daily Routine

```bash
# 1. Start your day (9:00 AM)
python mentor_agent.py standup

# 2. Begin morning session (9:00-11:00)
python mentor_agent.py start

# 3. During afternoon labs (14:00-17:00)
# - Work through hands-on exercises
# - Ask questions as needed:
python mentor_agent.py ask "How do I fix this error?"

# 4. Evening review (19:00-20:00)
# - Complete the day's quiz
# - Review progress:
python mentor_agent.py progress

# 5. Mark day as complete when asked by mentor
```

## Interactive Learning Session

When you run `start`, you enter an interactive session:

```
🤖 Mentor: Today we're learning about Docker containers...

You: What's the difference between a container and a VM?

🤖 Mentor: Great question! Let me explain...

You: Can you show me an example?

🤖 Mentor: Sure! Here's a practical example...

You: done
```

Type `done`, `exit`, or `quit` to finish the session.

## Tips for Success

### 1. Consistent Schedule
Stick to the daily schedule:
- **Morning (2 hours)**: Theory and concepts
- **Afternoon (3 hours)**: Hands-on labs
- **Evening (1 hour)**: Review and practice

### 2. Ask Lots of Questions
Your AI mentor is available 24/7:
```bash
python mentor_agent.py ask "Explain Docker networking"
python mentor_agent.py ask "How do I debug Kubernetes pods?"
python mentor_agent.py ask "What are Terraform modules?"
```

### 3. Complete Assessments
Don't skip weekly assessments. They:
- Validate your learning
- Identify gaps in knowledge
- Build confidence for interviews

### 4. Build Portfolio Projects
Throughout the bootcamp, work on portfolio projects:
- Containerized applications
- Kubernetes deployments
- CI/CD pipelines
- Cloud infrastructure

### 5. Take Notes
Create your own notes alongside the curriculum:
```bash
mkdir ~/bootcamp-notes
cd ~/bootcamp-notes
# Create notes for each topic
```

### 6. Practice Troubleshooting
Deliberately break things and fix them:
- Stop a container and restart it
- Misconfigure a deployment
- Debug network issues

This builds real-world skills!

## Working with the Curriculum

### Curriculum Structure

```
curriculum/
├── week1/
│   ├── day1.md  # Linux fundamentals
│   ├── day2.md  # File permissions
│   ├── day3.md  # Text processing
│   ├── day4.md  # Process management
│   └── day5.md  # Package management
├── week2/
│   └── ...
```

### Reading Curriculum Manually

You can also read curriculum files directly:

```bash
# View in terminal
cat curriculum/week1/day1.md

# View with formatting (if you have mdless)
mdless curriculum/week1/day1.md

# Open in editor
code curriculum/week1/day1.md  # VS Code
```

## Exercises and Labs

### Exercise Directory Structure

```
exercises/
├── week1/
│   ├── linux-basics/
│   ├── file-permissions/
│   └── text-processing/
├── week2/
│   └── ...
```

### Working on Exercises

1. Navigate to exercise directory
2. Read the README
3. Complete the tasks
4. Test your solutions
5. Ask mentor for review

Example:
```bash
cd exercises/week1/linux-basics
cat README.md
# Complete the exercise
python ../../../mentor_agent.py ask "Can you review my solution?"
```

## Assessment Process

### Weekly Assessment Flow

1. **Review the Week**
   ```bash
   python mentor_agent.py progress
   ```

2. **Take Assessment**
   ```bash
   python mentor_agent.py assess --week 1
   ```

3. **Complete Tasks**
   - Knowledge questions
   - Practical exercises
   - Troubleshooting scenarios

4. **Self-Grade** (answer key provided)

5. **If Passing (≥70%)**
   - Mentor marks week complete
   - Unlock next week
   - Update skill levels

6. **If Not Passing (<70%)**
   - Review weak areas
   - Ask mentor for help
   - Retry after practice

## Progress Tracking

Your progress is saved in `progress/user_progress.json`:

```json
{
  "current_week": 1,
  "current_day": 3,
  "days_completed": 2,
  "streak": 5,
  "badges": ["First Step", "Week Warrior"],
  "skills": {
    "Linux": 45.5,
    "Docker": 30.0
  }
}
```

### Badges You Can Earn

- 🏆 **First Step**: Complete your first day
- 🏆 **Week Warrior**: Complete a full week
- 🏆 **Month Master**: Complete 20 days
- 🏆 **Streak Starter**: 3-day streak
- 🏆 **Streak Master**: 7-day streak
- 🏆 **Dedication**: 14-day streak
- 🏆 **Foundation Expert**: Complete Week 2
- 🏆 **Container Captain**: Complete Week 4
- 🏆 **Pipeline Pro**: Complete Week 6
- 🏆 **Cloud Champion**: Complete Week 8

## Advanced Features

### Custom Learning Path

While the bootcamp follows a structured path, you can:
- Jump to specific topics with `ask`
- Review previous weeks anytime
- Deep dive into areas of interest

### Exporting Progress

```bash
# View progress report
python mentor_agent.py progress > my_progress.txt
```

### Integration with Your Workflow

```bash
# Add alias to your shell profile
alias bootcamp="python ~/cloud-engineer-bootcamp/mentor_agent.py"

# Now just use:
bootcamp start
bootcamp ask "Docker question"
```

## Troubleshooting

### Mentor Not Responding
- Check internet connection
- Verify API key in `.env`
- Check API rate limits

### Progress Not Saving
- Check file permissions on `progress/` directory
- Ensure disk space available
- Verify JSON file isn't corrupted

### Curriculum Not Loading
- Verify curriculum files exist
- Check file paths in error message
- Re-clone repository if needed

## Community and Support

### Getting Help

1. **Ask the Mentor First**
   ```bash
   python mentor_agent.py ask "I'm stuck on this error..."
   ```

2. **Check Documentation**
   - `docs/faq.md`
   - `docs/setup.md`

3. **Review Curriculum**
   - Previous days' content
   - Additional resources

4. **GitHub Issues**
   - Report bugs
   - Request features

## Next Steps

Ready to dive deeper?

1. **Review**: [Full Curriculum](../CURRICULUM.md)
2. **Explore**: Week 1 materials in `curriculum/week1/`
3. **Start**: `python mentor_agent.py start`

---

**Happy Learning! 🚀**
