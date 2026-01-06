import uuid
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_users(conn, num_users=50):
    
    print(f"Generating {num_users} users...")
    cursor = conn.cursor()

   
    cursor.execute("SELECT org_id FROM organizations LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        org_id = row['org_id']
    else:
        org_id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO organizations (org_id, name, domain, created_at) VALUES (?, ?, ?, ?)",
            (org_id, "TechFlow Solutions", "techflow.io", datetime.now())
        )
    
  
    users_data = []
    
    # Create 1 Admin
    admin_id = str(uuid.uuid4())
    users_data.append((
        admin_id, org_id, "Admin User", "admin@techflow.io", "admin", datetime.now() - timedelta(days=365)
    ))

    # Create Employees
    for _ in range(num_users - 1):
        uid = str(uuid.uuid4())
        name = fake.name()
        first_name = name.split()[0].lower()
        email = f"{first_name}@techflow.io"
        
        # Random join date within last 2 years
        joined_at = datetime.now() - timedelta(days=random.randint(1, 700))
        
        users_data.append((uid, org_id, name, email, "member", joined_at))

    cursor.executemany(
        "INSERT INTO users (user_id, org_id, name, email, role, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        users_data
    )
    conn.commit()
    return org_id