import uuid
import random
import os
from groq import Groq
from datetime import datetime, timedelta

# 1. Setup Groq Client
api_key = os.getenv('GROQ_API_KEY')
if api_key:
    client = Groq(api_key=api_key)
else:
    print(" WARNING: No GROQ_API_KEY found. Using static text.")
    client = None

def generate_llm_description(task_name, project_name):
    """
    Asks Groq (Llama3) to write a business description.
    """
    if not client:
        return "Standard task description for compliance and tracking."

    prompt = f"""
    You are a project manager. Write a 2-sentence professional description for a task named '{task_name}' 
    inside a project named '{project_name}'. 
    Direct answer only. No quotes. No "Here is the description".
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            
            model="llama-3.3-70b-versatile", 
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"API ERROR: {e}")
        return f"Review requirements for {task_name} and update the team."

def generate_tasks(conn):
    print(f" Generating Tasks using Groq/Llama3...")
    cursor = conn.cursor()

    # 1. Fetch Projects & Users
    cursor.execute("SELECT project_id, name as project_name FROM projects")
    projects = cursor.fetchall()

    cursor.execute("SELECT user_id FROM users")
    users = [row['user_id'] for row in cursor.fetchall()]

    cursor.execute("SELECT section_id, project_id FROM sections")
    all_sections = cursor.fetchall()
    
    def get_project_sections(pid):
        return [s['section_id'] for s in all_sections if s['project_id'] == pid]

    tasks_data = []
    
    # 2. Generate Tasks
    for proj in projects:
        project_id = proj['project_id']
        project_name = proj['project_name']
        sections = get_project_sections(project_id)
        
        # Create 3-4 tasks per project
        for i in range(random.randint(3, 4)):
            task_id = str(uuid.uuid4())
            task_name = f"Phase {i+1}: {project_name.split()[0]} Implementation"
            
            # CALL GROQ HERE
            description = generate_llm_description(task_name, project_name)
            
            assignee_id = random.choice(users)
            created_by_id = random.choice(users)
            section_id = random.choice(sections) if sections else None
            
            created_at = datetime.now() - timedelta(days=random.randint(10, 50))
            due_date = created_at + timedelta(days=random.randint(5, 20))
            
            tasks_data.append((
                task_id, project_id, section_id, None, assignee_id, created_by_id,
                task_name, description, 'medium', due_date, created_at
            ))

    # 3. Save to DB
    cursor.executemany(
        """INSERT INTO tasks (
            task_id, project_id, section_id, parent_task_id, assignee_id, created_by_id,
            name, description, priority, due_date, created_at
           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        tasks_data
    )
    
    conn.commit()
    print(f" Successfully generated {len(tasks_data)} AI-enriched tasks.")