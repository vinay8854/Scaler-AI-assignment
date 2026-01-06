-- 1. Organizations
CREATE TABLE organizations (
    org_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- 2. Teams
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY(org_id) REFERENCES organizations(org_id)
);

-- 3. Users
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'member', 'guest')),
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY(org_id) REFERENCES organizations(org_id)
);

-- 4. Team Memberships
CREATE TABLE team_memberships (
    membership_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    team_id TEXT NOT NULL,
    joined_at TIMESTAMP NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 5. Projects
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    owner_id TEXT NOT NULL,
    name TEXT NOT NULL,
    status TEXT CHECK(status IN ('on_track', 'at_risk', 'off_track', 'on_hold', 'complete')),
    due_date DATE,
    created_at TIMESTAMP NOT NULL,
    archived BOOLEAN DEFAULT 0,
    FOREIGN KEY(team_id) REFERENCES teams(team_id),
    FOREIGN KEY(owner_id) REFERENCES users(user_id)
);

-- 6. Sections
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position_order INTEGER NOT NULL,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

-- 7. Tasks
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    parent_task_id TEXT,
    assignee_id TEXT,
    created_by_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    due_date DATE,
    created_at TIMESTAMP NOT NULL,
    completed BOOLEAN DEFAULT 0,
    completed_at TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id),
    FOREIGN KEY(section_id) REFERENCES sections(section_id),
    FOREIGN KEY(parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY(assignee_id) REFERENCES users(user_id),
    FOREIGN KEY(created_by_id) REFERENCES users(user_id)
);

-- 8. Stories
CREATE TABLE stories (
    story_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    text_content TEXT,
    story_type TEXT CHECK(story_type IN ('comment', 'system')),
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY(task_id) REFERENCES tasks(task_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- 9. Tags
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    color TEXT,
    FOREIGN KEY(org_id) REFERENCES organizations(org_id)
);

-- 10. Task Tags
CREATE TABLE task_tags (
    id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    FOREIGN KEY(task_id) REFERENCES tasks(task_id),
    FOREIGN KEY(tag_id) REFERENCES tags(tag_id)
);