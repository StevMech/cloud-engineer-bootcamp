"""
Progress Tracker for Cloud Engineer Bootcamp

Tracks user progress, completion status, streaks, and skill development.
"""

import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, Any, List


class ProgressTracker:
    """Manages user progress throughout the bootcamp."""
    
    def __init__(self, progress_file: str = "progress/user_progress.json"):
        """Initialize progress tracker."""
        self.progress_file = Path(progress_file)
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_progress_file()
    
    def _ensure_progress_file(self):
        """Ensure progress file exists with default structure."""
        if not self.progress_file.exists():
            default_progress = {
                "started": False,
                "user_name": "",
                "start_date": "",
                "current_week": 1,
                "current_day": 1,
                "days_completed": 0,
                "streak": 0,
                "last_activity_date": "",
                "completed_weeks": {},
                "completed_days": {},
                "assessment_scores": {},
                "skills": {},
                "badges": [],
                "portfolio_projects": [],
                "total_hours": 0,
                "notes": {}
            }
            self._save_progress(default_progress)
    
    def _load_progress(self) -> Dict[str, Any]:
        """Load progress from JSON file."""
        with open(self.progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_progress(self, progress: Dict[str, Any]):
        """Save progress to JSON file."""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress, f, indent=2)
    
    def initialize_progress(self, user_name: str):
        """Initialize progress for a new user."""
        progress = self._load_progress()
        progress.update({
            "started": True,
            "user_name": user_name,
            "start_date": str(date.today()),
            "last_activity_date": str(date.today()),
            "streak": 1
        })
        self._save_progress(progress)
    
    def get_progress(self) -> Dict[str, Any]:
        """Get current progress."""
        return self._load_progress()
    
    def complete_day(self, week: int, day: int, hours_spent: float = 6.0):
        """Mark a day as completed."""
        progress = self._load_progress()
        
        day_key = f"week{week}_day{day}"
        if day_key not in progress.get("completed_days", {}):
            progress["days_completed"] = progress.get("days_completed", 0) + 1
        
        progress["completed_days"][day_key] = {
            "completed_date": str(date.today()),
            "hours_spent": hours_spent
        }
        
        progress["total_hours"] = progress.get("total_hours", 0) + hours_spent
        progress["last_activity_date"] = str(date.today())
        
        # Update streak
        self._update_streak(progress)
        
        # Check for badges
        self._check_and_award_badges(progress)
        
        self._save_progress(progress)
    
    def advance_to_next_day(self):
        """Advance to the next day in the curriculum."""
        progress = self._load_progress()
        
        current_day = progress.get("current_day", 1)
        current_week = progress.get("current_week", 1)
        
        if current_day < 5:
            progress["current_day"] = current_day + 1
        else:
            progress["current_day"] = 1
            progress["current_week"] = min(current_week + 1, 8)
        
        self._save_progress(progress)
    
    def complete_week_assessment(self, week: int, score: float):
        """Record week assessment completion and score."""
        progress = self._load_progress()
        
        progress["assessment_scores"][f"week{week}"] = {
            "score": score,
            "date": str(date.today()),
            "passed": score >= 70
        }
        
        if score >= 70:
            progress["completed_weeks"][str(week)] = True
            # Award skill points based on week
            self._update_skills(progress, week, score)
        
        self._save_progress(progress)
    
    def _update_skills(self, progress: Dict[str, Any], week: int, score: float):
        """Update skill proficiency based on completed week."""
        skills_by_week = {
            1: ["Linux", "Command Line"],
            2: ["Networking", "Scripting", "Git"],
            3: ["Docker", "Containerization"],
            4: ["Kubernetes", "Orchestration"],
            5: ["CI/CD", "GitHub Actions"],
            6: ["Terraform", "IaC", "GitOps"],
            7: ["Cloud Platforms", "AWS/Azure/GCP"],
            8: ["Monitoring", "Security", "Production"]
        }
        
        if "skills" not in progress:
            progress["skills"] = {}
        
        for skill in skills_by_week.get(week, []):
            current_level = progress["skills"].get(skill, 0)
            # Increase skill level based on assessment score
            increase = (score / 100) * 20  # Max 20 points per week
            progress["skills"][skill] = min(current_level + increase, 100)
    
    def _update_streak(self, progress: Dict[str, Any]):
        """Update learning streak."""
        today = date.today()
        last_activity = progress.get("last_activity_date", "")
        
        if not last_activity:
            progress["streak"] = 1
            return
        
        last_date = date.fromisoformat(last_activity)
        days_diff = (today - last_date).days
        
        if days_diff == 0:
            # Same day, no change
            pass
        elif days_diff == 1:
            # Consecutive day, increase streak
            progress["streak"] = progress.get("streak", 0) + 1
        else:
            # Streak broken
            progress["streak"] = 1
    
    def _check_and_award_badges(self, progress: Dict[str, Any]):
        """Check and award achievement badges."""
        badges = progress.get("badges", [])
        days_completed = progress.get("days_completed", 0)
        streak = progress.get("streak", 0)
        
        badge_criteria = {
            "First Step": ("Complete your first day", lambda p: p["days_completed"] >= 1),
            "Week Warrior": ("Complete a full week", lambda p: p["days_completed"] >= 5),
            "Month Master": ("Complete 20 days", lambda p: p["days_completed"] >= 20),
            "Streak Starter": ("Maintain a 3-day streak", lambda p: p["streak"] >= 3),
            "Streak Master": ("Maintain a 7-day streak", lambda p: p["streak"] >= 7),
            "Dedication": ("Maintain a 14-day streak", lambda p: p["streak"] >= 14),
            "Foundation Expert": ("Complete Week 2", lambda p: p["completed_weeks"].get("2", False)),
            "Container Captain": ("Complete Week 4", lambda p: p["completed_weeks"].get("4", False)),
            "Pipeline Pro": ("Complete Week 6", lambda p: p["completed_weeks"].get("6", False)),
            "Cloud Champion": ("Complete Week 8", lambda p: p["completed_weeks"].get("8", False)),
        }
        
        for badge_name, (description, criteria) in badge_criteria.items():
            if badge_name not in badges and criteria(progress):
                badges.append(badge_name)
                progress["badges"] = badges
    
    def add_portfolio_project(self, project_name: str, description: str, 
                             technologies: List[str], repository: str = ""):
        """Add a portfolio project to tracking."""
        progress = self._load_progress()
        
        project = {
            "name": project_name,
            "description": description,
            "technologies": technologies,
            "repository": repository,
            "completed_date": str(date.today())
        }
        
        if "portfolio_projects" not in progress:
            progress["portfolio_projects"] = []
        
        progress["portfolio_projects"].append(project)
        self._save_progress(progress)
    
    def add_note(self, week: int, day: int, note: str):
        """Add a note for a specific day."""
        progress = self._load_progress()
        
        if "notes" not in progress:
            progress["notes"] = {}
        
        day_key = f"week{week}_day{day}"
        progress["notes"][day_key] = {
            "note": note,
            "date": str(date.today())
        }
        
        self._save_progress(progress)
    
    def get_skill_summary(self) -> Dict[str, float]:
        """Get summary of skill proficiency levels."""
        progress = self._load_progress()
        return progress.get("skills", {})
    
    def get_badges(self) -> List[str]:
        """Get list of earned badges."""
        progress = self._load_progress()
        return progress.get("badges", [])
    
    def reset_progress(self):
        """Reset all progress (use with caution!)."""
        default_progress = {
            "started": False,
            "user_name": "",
            "start_date": "",
            "current_week": 1,
            "current_day": 1,
            "days_completed": 0,
            "streak": 0,
            "last_activity_date": "",
            "completed_weeks": {},
            "completed_days": {},
            "assessment_scores": {},
            "skills": {},
            "badges": [],
            "portfolio_projects": [],
            "total_hours": 0,
            "notes": {}
        }
        self._save_progress(default_progress)
    
    def export_progress_report(self) -> str:
        """Export a formatted progress report."""
        progress = self._load_progress()
        
        report = f"""
# Progress Report for {progress.get('user_name', 'Student')}

## Overview
- Started: {progress.get('start_date', 'N/A')}
- Current Position: Week {progress.get('current_week', 1)}, Day {progress.get('current_day', 1)}
- Days Completed: {progress.get('days_completed', 0)}/40
- Total Hours: {progress.get('total_hours', 0)}
- Current Streak: {progress.get('streak', 0)} days

## Skills Proficiency
"""
        skills = progress.get('skills', {})
        for skill, level in sorted(skills.items(), key=lambda x: x[1], reverse=True):
            report += f"- {skill}: {level:.1f}%\n"
        
        report += "\n## Badges Earned\n"
        for badge in progress.get('badges', []):
            report += f"- 🏆 {badge}\n"
        
        report += "\n## Portfolio Projects\n"
        for project in progress.get('portfolio_projects', []):
            report += f"- **{project['name']}**: {project['description']}\n"
            report += f"  Technologies: {', '.join(project['technologies'])}\n"
        
        return report
