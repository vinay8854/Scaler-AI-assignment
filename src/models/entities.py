from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    """Represents a registered employee in the system."""
    user_id: str
    org_id: str
    name: str
    email: str
    role: str
    created_at: datetime

@dataclass
class Project:
    """Represents a workspace project."""
    project_id: str
    team_id: str
    name: str
    status: str  # 'on_track', 'at_risk', etc.
    due_date: datetime

@dataclass
class Task:
   
    task_id: str
    project_id: str
    name: str
    description: str
    assignee_id: Optional[str]
    priority: str = "medium"
    completed: bool = False