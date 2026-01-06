import uuid
import random
from datetime import datetime, timedelta
from scrapers.industry_data import fetch_real_world_projects


PROJECT_TEMPLATES = fetch_real_world_projects()

def generate_projects(conn, team_map):
    
    print(f"Generating projects for {len(team_map)} teams...")
    cursor = conn.cursor()
    
    # 1. Fetch potential project owners (users)
    cursor.execute("SELECT user_id FROM users")
    users = [row['user_id'] for row in cursor.fetchall()]
    
    projects_data = []
    sections_data = []
    
    # 2. Iterate through teams and create their specific projects
    for team_name, team_id in team_map.items():
        # Get templates for this team (default to Ops if not found)
        templates = PROJECT_TEMPLATES.get(team_name, PROJECT_TEMPLATES["Operations"])
        
        # Create 3-5 projects per team
        for _ in range(random.randint(3, 5)):
            project_id = str(uuid.uuid4())
            owner_id = random.choice(users)
            name = random.choice(templates)
            
            # Status logic: 70% on track, 20% at risk, 10% off track
            status = random.choices(
                ['on_track', 'at_risk', 'off_track', 'complete'], 
                weights=[60, 15, 5, 20], k=1
            )[0]
            
            # Dates
            created_at = datetime.now() - timedelta(days=random.randint(30, 120))
            due_date = datetime.now() + timedelta(days=random.randint(10, 60))
            
            projects_data.append((
                project_id, team_id, owner_id, name, status, due_date, created_at
            ))
            
           
            standard_sections = ["To Do", "In Progress", "Review", "Done"]
            for index, section_name in enumerate(standard_sections):
                sections_data.append((
                    str(uuid.uuid4()), project_id, section_name, index
                ))

    # Bulk Insert Projects
    cursor.executemany(
        """INSERT INTO projects (project_id, team_id, owner_id, name, status, due_date, created_at) 
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        projects_data
    )
    
    # Bulk Insert Sections
    cursor.executemany(
        "INSERT INTO sections (section_id, project_id, name, position_order) VALUES (?, ?, ?, ?)",
        sections_data
    )
    
    conn.commit()
    print(f"    Created {len(projects_data)} projects and {len(sections_data)} sections.")
    return projects_data # Return for task generation