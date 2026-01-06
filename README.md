# Asana RL Seed Data Simulation

## Overview

This project generates a realistic synthetic dataset that simulates how a mid-to-large B2B SaaS company uses Asana for project and task management. The generated data is intended to be used as seed data for reinforcement learning (RL) environments, especially for evaluating computer-use AI agents.

The simulated organization includes Engineering, Marketing, and Operations teams, with realistic users, projects, sections, and tasks. The focus is on realism, logical consistency, and enterprise-style workflows rather than producing toy or placeholder data.

---

## Project Structure

.
├── output/
│   └── asana_simulation.sqlite
├── src/
│   ├── generators/
│   │   ├── users.py
│   │   ├── teams.py
│   │   ├── projects.py
│   │   └── tasks.py
│   ├── models/
│   │   └── entities.py
│   ├── scrapers/
│   │   └── industry_data.py
│   ├── utils/
│   │   └── database.py
│   └── main.py
├── schema.sql
├── requirements.txt
└── README.md

---

## What Data Is Generated

- Users: Realistic employee profiles with names, roles, emails, and join dates
- Teams: Engineering, Marketing, and Operations teams
- Projects: Multiple projects per team with industry-inspired names and realistic status distributions
- Sections: Standard workflow stages such as To Do, In Progress, Review, and Done
- Tasks: Action-oriented tasks with due dates, completion status, and professional descriptions
- Text Content: Task descriptions can optionally be generated using an LLM for higher realism

---

## LLM Usage (Groq – Optional)

Task descriptions can optionally be generated using Groq (Llama 3) to produce natural, professional language.

Important points:
- LLM usage is limited strictly to text fields (task descriptions only)
- No structural or relational data depends on the LLM
- If a Groq API key is not provided, the system automatically falls back to static template-based descriptions
- The project runs fully without any API key

---

## How to Get a Groq API Key (Optional)

1. Go to https://console.groq.com
2. Sign in using Google or GitHub
3. Navigate to API Keys in the dashboard
4. Create a new API key
5. Copy the key

---

## How to Set the Groq API Key

Option 1: Using a .env file 

Create a file named .env in the project root and add:

GROQ_API_KEY=your_api_key_here

---

## How to Run the Project

1. Install dependencies:
pip install -r requirements.txt

2. Run the generator:
python src/main.py

This will:
- Recreate the SQLite database using schema.sql
- Generate users, teams, projects, sections, and tasks
- Save the final database to output/asana_simulation.sqlite

---

## Output

The final output is a populated SQLite database file:
output/asana_simulation.sqlite

You can open this file using any SQLite browser or query it programmatically.

---

## Notes

- Referential integrity and temporal consistency are enforced
- The database is rebuilt from scratch on each run
- The data is designed to resemble real-world Asana usage patterns rather than synthetic toy examples
