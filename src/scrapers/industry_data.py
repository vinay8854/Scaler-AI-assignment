def fetch_real_world_projects():
    """
    Simulates scraping project templates from public repositories.
    Returns a list of realistic project names and descriptions used in the industry.
    """
    return {
        "Engineering": [
            "Legacy Monolith Decomposition",
            "Kubernetes Cluster Upgrade v1.28",
            "OIDC Authentication Implementation",
            "GDPR Data Compliance Audit",
            "Real-time Notification Service Migration"
        ],
        "Marketing": [
            "Q3 Product Hunt Launch",
            "Customer Case Study Series: FinTech",
            "SEO Keyword Optimization - Landing Pages",
            "Competitor Analysis Report 2026",
            "Annual User Conference Logistics"
        ],
        # --- THIS WAS MISSING BEFORE ---
        "Operations": [
            "Quarterly Financial Close",
            "Employee Onboarding Revamp",
            "Vendor Contract Renegotiation",
            "Office Space Optimization",
            "Annual Budget Planning 2026"
        ]
    }

def fetch_competitor_names():
    """
    Returns a list of real competitor names for context injection.
    """
    return ["Jira", "Monday.com", "Trello", "ClickUp", "Linear"]