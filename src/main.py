# File: src/main.py
import sys
import os
from dotenv import load_dotenv

load_dotenv()
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from utils.database import init_database, get_connection
from generators.users import generate_users
from generators.teams import generate_teams 
from generators.projects import generate_projects
from generators.tasks import generate_tasks 

def main():
    print(" Starting Asana Data Simulation ")
    
    print("\n Initializing Database")
    init_database()
    
    conn = get_connection()
    
    try:
        print("\n Generating Organization & Users")
        org_id = generate_users(conn, num_users=50)
        
        print("\n Generating Teams")
        team_map = generate_teams(conn, org_id)
        
        print("\n Generating Projects & Sections")
        generate_projects(conn, team_map)
        
        # --- NEW STEP ---
        print("\n Generating AI Tasks")
        generate_tasks(conn)
        # ----------------
        
        print("\n SIMULATION COMPLETE. Database ready at output/asana_simulation.sqlite")

    except Exception as e:
        print(f"\n Error during simulation: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == "__main__":
    main()