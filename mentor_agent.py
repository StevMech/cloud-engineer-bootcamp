#!/usr/bin/env python3
"""
Cloud Engineer Bootcamp - AI Mentor Agent

An intelligent mentor agent that guides users through an 8-week
cloud platform engineering bootcamp with structured learning,
hands-on labs, and continuous assessment.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

import typer
import yaml
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from dotenv import load_dotenv

# Import AI providers
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

from progress_tracker import ProgressTracker

# Load environment variables
load_dotenv()

# Initialize Typer app and Rich console
app = typer.Typer(help="Cloud Engineer Bootcamp - AI Mentor Agent")
console = Console()

# Base directory
BASE_DIR = Path(__file__).parent


class MentorAgent:
    """Main mentor agent class handling AI interactions and curriculum delivery."""
    
    def __init__(self):
        """Initialize the mentor agent with configuration."""
        self.config = self._load_config()
        self.progress_tracker = ProgressTracker()
        self.ai_client = self._initialize_ai_client()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from config.yaml."""
        config_path = BASE_DIR / "config.yaml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _initialize_ai_client(self):
        """Initialize the appropriate AI client based on configuration."""
        provider = self.config.get('ai_provider', 'openai')
        
        if provider == 'openai' and OPENAI_AVAILABLE:
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                console.print("[yellow]Warning: OPENAI_API_KEY not set. AI features will be limited.[/yellow]")
                return None
            return OpenAI(api_key=api_key)
        
        elif provider == 'anthropic' and ANTHROPIC_AVAILABLE:
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                console.print("[yellow]Warning: ANTHROPIC_API_KEY not set. AI features will be limited.[/yellow]")
                return None
            return Anthropic(api_key=api_key)
        
        else:
            console.print(f"[yellow]AI provider '{provider}' not available. Running in demo mode.[/yellow]")
            return None
    
    def get_ai_response(self, prompt: str, system_prompt: str = None) -> str:
        """Get response from AI provider."""
        if not self.ai_client:
            return self._get_fallback_response(prompt)
        
        provider = self.config.get('ai_provider', 'openai')
        
        try:
            if provider == 'openai':
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": prompt})
                
                response = self.ai_client.chat.completions.create(
                    model=self.config.get('openai_model', 'gpt-4'),
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000
                )
                return response.choices[0].message.content
            
            elif provider == 'anthropic':
                response = self.ai_client.messages.create(
                    model=self.config.get('anthropic_model', 'claude-3-sonnet-20240229'),
                    system=system_prompt or "You are a helpful cloud engineering mentor.",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000
                )
                return response.content[0].text
        
        except Exception as e:
            console.print(f"[red]Error getting AI response: {e}[/red]")
            return self._get_fallback_response(prompt)
    
    def _get_fallback_response(self, prompt: str) -> str:
        """Provide fallback responses when AI is not available."""
        return (
            "I'm currently running in demo mode without AI capabilities. "
            "Please set up your API key in the .env file to enable full AI mentoring features. "
            "For now, please refer to the curriculum files in the curriculum/ directory."
        )
    
    def display_welcome(self):
        """Display welcome message and ASCII art."""
        ascii_art = """
   _____ _                 _   ______             _                         
  / ____| |               | | |  ____|           (_)                        
 | |    | | ___  _   _  __| | | |__   _ __   __ _ _ _ __   ___  ___ _ __   
 | |    | |/ _ \\| | | |/ _` | |  __| | '_ \\ / _` | | '_ \\ / _ \\/ _ \\ '__|  
 | |____| | (_) | |_| | (_| | | |____| | | | (_| | | | | |  __/  __/ |     
  \\_____|_|\\___/ \\__,_|\\__,_| |______|_| |_|\\__, |_|_| |_|\\___|\\___|_|     
                                              __/ |                          
      ____              _   _____            |___/                           
     |  _ \\            | | / ____|                                           
     | |_) | ___   ___ | || |     __ _ _ __ ___  _ __                      
     |  _ < / _ \\ / _ \\| || |    / _` | '_ ` _ \\| '_ \\                     
     | |_) | (_) | (_) | || |___| (_| | | | | | | |_) |                    
     |____/ \\___/ \\___/|_| \\_____\\__,_|_| |_| |_| .__/                     
                                                  | |                         
                                                  |_|                         
        """
        
        if self.config.get('show_ascii_art', True):
            console.print(ascii_art, style="bold cyan")
        
        welcome_panel = Panel(
            "[bold green]Welcome to the Cloud Engineer Bootcamp![/bold green]\n\n"
            "An AI-powered 8-week intensive program to transform you into a "
            "job-ready cloud platform engineer.\n\n"
            "✨ Features:\n"
            "  • Structured daily curriculum\n"
            "  • Hands-on labs and exercises\n"
            "  • AI mentor available 24/7\n"
            "  • Weekly assessments\n"
            "  • Portfolio projects\n\n"
            "[cyan]Let's begin your journey to cloud engineering mastery! 🚀[/cyan]",
            title="🎓 Cloud Engineer Bootcamp",
            border_style="cyan"
        )
        console.print(welcome_panel)
    
    def load_curriculum_day(self, week: int, day: int) -> Optional[str]:
        """Load curriculum content for a specific day."""
        curriculum_file = BASE_DIR / "curriculum" / f"week{week}" / f"day{day}.md"
        
        if curriculum_file.exists():
            with open(curriculum_file, 'r') as f:
                return f.read()
        return None
    
    def start_learning_session(self):
        """Start a new learning session."""
        progress = self.progress_tracker.get_progress()
        current_week = progress.get('current_week', 1)
        current_day = progress.get('current_day', 1)
        
        console.print(f"\n[bold cyan]📅 Current Progress: Week {current_week}, Day {current_day}[/bold cyan]\n")
        
        # Load curriculum for current day
        curriculum_content = self.load_curriculum_day(current_week, current_day)
        
        if curriculum_content:
            console.print(Panel(Markdown(curriculum_content), title=f"Week {current_week} - Day {current_day}", border_style="green"))
        else:
            console.print(f"[yellow]Curriculum content for Week {current_week}, Day {current_day} is being prepared...[/yellow]")
            self._show_day_outline(current_week, current_day)
        
        # Interactive session
        self._run_interactive_session(current_week, current_day)
    
    def _show_day_outline(self, week: int, day: int):
        """Show a general outline when specific content isn't available."""
        outline = f"""
## Week {week}, Day {day}

### 🌅 Morning Session (09:00-11:00): Theory & Concepts
- Learning objectives for today
- Conceptual explanations
- Best practices and patterns
- Q&A with your AI mentor

### ☀️ Afternoon Session (14:00-17:00): Hands-On Practice
- Guided lab exercises
- Progressive challenges
- Real-world scenarios
- Troubleshooting practice

### 🌙 Evening Session (19:00-20:00): Review & Reinforcement
- Summary of key learnings
- Quick quiz or challenge
- Preview of tomorrow's topics
        """
        console.print(Markdown(outline))
    
    def _run_interactive_session(self, week: int, day: int):
        """Run an interactive learning session with the AI mentor."""
        console.print("\n[bold green]💬 Interactive Session Started[/bold green]")
        console.print("Ask me anything about today's topics, or type 'done' to finish.\n")
        
        system_prompt = f"""You are an expert cloud platform engineering mentor. 
You are teaching Week {week}, Day {day} of an 8-week bootcamp. 
Be encouraging, provide clear explanations with examples, and guide the student 
through concepts progressively. If they struggle, offer simpler explanations or analogies.
Focus on practical, hands-on learning."""
        
        while True:
            question = Prompt.ask("[bold cyan]You[/bold cyan]")
            
            if question.lower() in ['done', 'exit', 'quit']:
                break
            
            console.print("\n[bold magenta]🤖 Mentor[/bold magenta]: ", end="")
            
            with console.status("[bold green]Thinking...", spinner="dots"):
                response = self.get_ai_response(question, system_prompt)
            
            console.print(Markdown(response))
            console.print()
        
        # Mark day as completed
        if Confirm.ask("\n[bold green]Did you complete today's learning?[/bold green]"):
            self.progress_tracker.complete_day(week, day)
            console.print("[bold green]✅ Great job! Progress saved.[/bold green]")
            
            if day < 5:
                if Confirm.ask("Would you like to continue to the next day?"):
                    self.progress_tracker.advance_to_next_day()


# CLI Commands

@app.command()
def start():
    """Start the bootcamp or continue from where you left off."""
    agent = MentorAgent()
    agent.display_welcome()
    
    progress = agent.progress_tracker.get_progress()
    
    if not progress.get('started'):
        console.print("\n[bold cyan]Let's get you started![/bold cyan]\n")
        name = Prompt.ask("What's your name?")
        agent.progress_tracker.initialize_progress(name)
        console.print(f"\n[bold green]Welcome aboard, {name}! 🎉[/bold green]\n")
    
    agent.start_learning_session()


@app.command()
def ask(question: str):
    """Ask the AI mentor a question about any topic."""
    agent = MentorAgent()
    
    console.print(f"\n[bold cyan]Question:[/bold cyan] {question}\n")
    console.print("[bold magenta]🤖 Mentor:[/bold magenta]\n")
    
    with console.status("[bold green]Thinking...", spinner="dots"):
        system_prompt = """You are an expert cloud platform engineering mentor. 
Provide clear, practical answers with examples. If relevant, include commands, 
code snippets, or step-by-step instructions."""
        response = agent.get_ai_response(question, system_prompt)
    
    console.print(Markdown(response))
    console.print()


@app.command()
def progress():
    """View your learning progress and statistics."""
    tracker = ProgressTracker()
    progress_data = tracker.get_progress()
    
    if not progress_data.get('started'):
        console.print("[yellow]You haven't started the bootcamp yet. Run 'python mentor_agent.py start' to begin![/yellow]")
        return
    
    # Create progress table
    table = Table(title="📊 Your Learning Progress", border_style="cyan")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    
    table.add_row("Current Week", str(progress_data.get('current_week', 1)))
    table.add_row("Current Day", str(progress_data.get('current_day', 1)))
    table.add_row("Total Days Completed", str(progress_data.get('days_completed', 0)))
    table.add_row("Current Streak", f"{progress_data.get('streak', 0)} days")
    table.add_row("Started On", progress_data.get('start_date', 'N/A'))
    
    console.print(table)
    
    # Show week-by-week completion
    weeks_table = Table(title="📅 Weekly Completion", border_style="green")
    weeks_table.add_column("Week", style="cyan")
    weeks_table.add_column("Status", style="green")
    
    for week in range(1, 9):
        completed = progress_data.get('completed_weeks', {}).get(str(week), False)
        status = "✅ Completed" if completed else "⏳ In Progress" if week == progress_data.get('current_week') else "🔒 Locked"
        weeks_table.add_row(f"Week {week}", status)
    
    console.print(weeks_table)


@app.command()
def assess(week: int = typer.Option(1, help="Week number for assessment")):
    """Take a weekly assessment to test your knowledge."""
    assessment_file = BASE_DIR / "assessments" / f"week{week}_assessment.md"
    
    if not assessment_file.exists():
        console.print(f"[yellow]Assessment for Week {week} is being prepared...[/yellow]")
        return
    
    console.print(f"\n[bold cyan]📝 Week {week} Assessment[/bold cyan]\n")
    
    with open(assessment_file, 'r') as f:
        content = f.read()
        console.print(Markdown(content))
    
    console.print("\n[bold green]Complete the assessment and check your answers.[/bold green]")
    
    if Confirm.ask("\nDid you pass the assessment (score >= 70%)?"):
        tracker = ProgressTracker()
        tracker.complete_week_assessment(week, 100)  # Simplified for now
        console.print("[bold green]✅ Congratulations! Assessment completed.[/bold green]")


@app.command()
def standup():
    """Daily standup - reflect on your progress and set goals."""
    agent = MentorAgent()
    
    console.print("\n[bold cyan]📅 Daily Standup[/bold cyan]\n")
    
    yesterday = Prompt.ask("What did you learn yesterday?")
    today = Prompt.ask("What will you focus on today?")
    blockers = Prompt.ask("Any challenges or blockers?")
    
    console.print("\n[bold magenta]🤖 Mentor Feedback:[/bold magenta]\n")
    
    prompt = f"""
Daily Standup Summary:
- Yesterday: {yesterday}
- Today's Focus: {today}
- Blockers: {blockers}

Provide encouraging feedback and actionable advice for today's learning.
    """
    
    with console.status("[bold green]Analyzing...", spinner="dots"):
        response = agent.get_ai_response(prompt)
    
    console.print(Markdown(response))


@app.command()
def interview():
    """Practice platform engineering interview questions."""
    agent = MentorAgent()
    
    console.print("\n[bold cyan]🎯 Interview Practice[/bold cyan]\n")
    
    topics = [
        "Linux and system administration",
        "Docker and containerization",
        "Kubernetes orchestration",
        "CI/CD pipelines",
        "Infrastructure as Code (Terraform)",
        "Cloud platforms (AWS/Azure/GCP)",
        "Monitoring and observability",
        "Security best practices"
    ]
    
    console.print("[bold green]Choose a topic:[/bold green]\n")
    for i, topic in enumerate(topics, 1):
        console.print(f"  {i}. {topic}")
    
    choice = Prompt.ask("\nEnter topic number", default="1")
    topic = topics[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(topics) else topics[0]
    
    console.print(f"\n[bold magenta]🤖 Interviewer:[/bold magenta]\n")
    
    prompt = f"Generate a realistic platform engineering interview question about {topic}. Make it practical and scenario-based."
    
    with console.status("[bold green]Preparing question...", spinner="dots"):
        question = agent.get_ai_response(prompt)
    
    console.print(Markdown(question))
    console.print("\n[bold cyan]Take your time to answer...[/bold cyan]\n")
    
    answer = Prompt.ask("Your answer")
    
    console.print("\n[bold magenta]🤖 Feedback:[/bold magenta]\n")
    
    feedback_prompt = f"""
Interview Question: {question}
Candidate's Answer: {answer}

Provide constructive feedback on this answer. Highlight strengths and areas for improvement.
    """
    
    with console.status("[bold green]Evaluating...", spinner="dots"):
        feedback = agent.get_ai_response(feedback_prompt)
    
    console.print(Markdown(feedback))


@app.command()
def resources(topic: str = typer.Option("", help="Specific topic to find resources for")):
    """Get curated learning resources for a topic."""
    resources_file = BASE_DIR / "resources" / "links.md"
    
    if resources_file.exists():
        with open(resources_file, 'r') as f:
            content = f.read()
            console.print(Markdown(content))
    else:
        console.print("[yellow]Resources are being curated... Check back soon![/yellow]")


@app.command()
def reset():
    """Reset your progress (use with caution!)."""
    if Confirm.ask("[bold red]⚠️  Are you sure you want to reset all progress?[/bold red]"):
        tracker = ProgressTracker()
        tracker.reset_progress()
        console.print("[bold green]✅ Progress reset. Start fresh with 'python mentor_agent.py start'[/bold green]")


if __name__ == "__main__":
    app()
