import uuid
from datetime import datetime

DEPARTMENTS = [
    {"name": "Engineering", "desc": "Product development and infrastructure"},
    {"name": "Marketing", "desc": "Growth, branding, and social media"},
    {"name": "Operations", "desc": "HR, Finance, and internal processes"}
]

def generate_teams(conn, org_id):
    
    print(f"Setting up {len(DEPARTMENTS)} core teams...")
    cursor = conn.cursor()
    
    team_ids = {} # Store names to IDs for later use

    for dept in DEPARTMENTS:
        tid = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO teams (team_id, org_id, name, description, created_at) VALUES (?, ?, ?, ?, ?)",
            (tid, org_id, dept["name"], dept["desc"], datetime.now())
        )
        team_ids[dept["name"]] = tid
    
    conn.commit()
    return team_ids