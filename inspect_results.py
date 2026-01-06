import sqlite3
import pandas as pd


conn = sqlite3.connect('output/asana_simulation.sqlite')

print("DATABASE REPORT ")

tables = ["users", "teams", "projects", "sections", "tasks"]
for table in tables:
    count = pd.read_sql(f"SELECT COUNT(*) as count FROM {table}", conn).iloc[0]['count']
    print(f"Table '{table}': {count} rows")


query = """
SELECT 
    p.name as Project_Name,
    t.name as Task_Name,
    t.description as AI_Description
FROM tasks t
JOIN projects p ON t.project_id = p.project_id
LIMIT 5
"""
df = pd.read_sql(query, conn)


pd.set_option('display.max_colwidth', None)
print(df)

conn.close()