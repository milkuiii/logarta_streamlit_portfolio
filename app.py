"""
Personal Portfolio Application - Sophia Gabrielle Logarta
Course / Section: CSIT349 - Section F2
Institution: Cebu Institute of Technology - University (CIT-U)
"""

import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# ==============================================================================
# 0. CONFIGURATION & PAGE SETUP
# ==============================================================================

DEFAULT_GITHUB_USERNAME = "milkuiii"
STUDENT_NAME = "Sophia Gabrielle Logarta"
STUDENT_PROGRAM = "Bachelor of Science in Computer Science (BSCS)"
STUDENT_YEAR = "3rd Year Undergraduate"
STUDENT_SECTION = "CSIT349 - Section F2"
STUDENT_SCHOOL = "Cebu Institute of Technology - University (CIT-U)"
STUDENT_ALMA_MATER = "Philippine Science High School - Central Visayas Campus (PSHS-CVisC '24)"
STUDENT_LOCATION = "Cebu City, Philippines"

st.set_page_config(
    page_title=f"{STUDENT_NAME} | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for polished look, smooth scrolling, and sticky header
st.markdown(
    """
    <style>
    /* CSS Custom Properties - Design System (Maroon & Cream Palette) */
    :root {
        --color-primary: #B32F4E;         /* Core brand maroon */
        --color-primary-hover: #C93B5D;   /* Lighter vibrant maroon for hover */
        --color-primary-light: #5E1A31;   /* Muted dark maroon surface */
        --color-primary-muted: rgba(179, 47, 78, 0.25);
        --color-bg-base: #4A1426;         /* Deep Maroon primary page background */
        --color-bg-surface: #32101D;      /* Dark Burgundy surface (cards, sidebar, nav) */
        --color-bg-subtle: #3D1424;       /* Tonal dark burgundy variation */
        --color-bg-elevated: #56182D;     /* Slightly lighter burgundy for elevated states */
        --color-cream: #F4F1DE;           /* Primary text, headings, prominent labels */
        --color-cream-soft: #E8E1C8;      /* Secondary text, muted foreground, subtle borders */
        --color-cream-muted: #B8B09A;     /* Muted secondary labels and captions */
        --color-accent: #F4F7CD;          /* Accent cream for badges, highlights */
        --color-accent-border: #D8DC97;
        --color-accent-text: #2D3010;
        --color-border: #5C2236;          /* Muted burgundy border */
        --color-border-subtle: #451928;
        --color-border-cream: rgba(244, 241, 222, 0.2);
        --font-family: "Helvetica Now", "Helvetica Neue", Helvetica, Arial, sans-serif;
        --radius-sm: 6px;
        --radius-md: 10px;
        --radius-lg: 14px;
        --radius-pill: 9999px;
        --shadow-xs: 0 1px 3px rgba(0, 0, 0, 0.25);
        --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.35);
        --shadow-md: 0 6px 14px rgba(0, 0, 0, 0.45);
        --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.55);
        --transition-fast: 0.15s ease-in-out;
        --transition-normal: 0.25s ease-in-out;
    }

    /* Overall App Background & Typography */
    .stApp {
        background-color: var(--color-bg-base) !important;
        color: var(--color-cream) !important;
    }

    html, body, .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6,
    input, textarea, select {
        font-family: var(--font-family) !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    /* Preserve icon fonts from being overridden by custom font family */
    [class*="material-symbols"], [data-testid="stIconMaterial"], .material-symbols-rounded, .material-symbols-outlined, [data-testid="stExpanderToggleIcon"] {
        font-family: "Material Symbols Rounded", "Material Symbols Outlined", sans-serif !important;
        letter-spacing: normal !important;
    }

    /* Smooth native scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Headings Typography Hierarchy */
    h1, .stMarkdown h1, [data-testid="stHeader"] h1 {
        font-family: var(--font-family) !important;
        font-weight: 700 !important;
        color: var(--color-cream) !important;
        letter-spacing: -0.025em;
        line-height: 1.25;
    }

    h2, .stMarkdown h2 {
        font-family: var(--font-family) !important;
        font-weight: 700 !important;
        color: var(--color-cream) !important;
        letter-spacing: -0.02em;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        line-height: 1.3;
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 6px;
    }

    h3, .stMarkdown h3 {
        font-family: var(--font-family) !important;
        font-weight: 600 !important;
        color: var(--color-cream-soft) !important;
        letter-spacing: -0.015em;
        line-height: 1.35;
    }

    h4, .stMarkdown h4 {
        font-family: var(--font-family) !important;
        font-weight: 600 !important;
        color: var(--color-cream-soft) !important;
        line-height: 1.4;
    }

    /* General Body Text & Links */
    p, li, .stMarkdown p {
        color: var(--color-cream-soft);
        line-height: 1.65;
        font-size: 0.98rem;
    }

    strong, b {
        color: var(--color-cream) !important;
    }

    a {
        color: var(--color-accent);
        text-decoration: none;
        transition: color var(--transition-fast);
        font-weight: 500;
    }

    a:hover {
        color: #FFFFFF;
        text-decoration: underline;
    }

    /* Header styling */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* Section anchor offset for comfortable scrolling */
    .section-anchor {
        scroll-margin-top: 80px;
        padding-top: 24px;
        margin-top: 16px;
    }

    /* Section divider */
    .section-divider {
        margin: 36px 0 24px 0;
        border: 0;
        height: 1px;
        background: linear-gradient(to right, rgba(244, 241, 222, 0.05), rgba(179, 47, 78, 0.6), rgba(244, 241, 222, 0.05));
    }

    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, var(--color-bg-surface), var(--color-bg-subtle));
        border-radius: var(--radius-md);
        padding: 14px 20px;
        border: 1px solid var(--color-border);
        border-left: 4px solid var(--color-primary);
        box-shadow: var(--shadow-sm);
        transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        border-color: var(--color-primary);
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--color-cream) !important;
        font-weight: 700;
        font-size: 1.7rem;
    }
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: var(--color-cream-muted) !important;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: var(--color-accent) !important;
    }

    /* Card Container */
    .portfolio-card {
        background-color: var(--color-bg-surface);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-md);
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: var(--shadow-sm);
        transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
    }
    .portfolio-card:hover {
        box-shadow: var(--shadow-md);
        border-color: var(--color-primary);
        transform: translateY(-2px);
    }

    /* Student Section Badge */
    .student-badge {
        display: inline-block;
        padding: 4px 14px;
        background-color: var(--color-accent);
        color: var(--color-accent-text);
        border: 1px solid var(--color-accent-border);
        border-radius: var(--radius-pill);
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: 0.02em;
    }

    /* Topic Pill */
    .topic-pill {
        display: inline-block;
        padding: 4px 11px;
        background-color: var(--color-bg-subtle);
        color: var(--color-cream-soft);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-pill);
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 5px;
        margin-top: 5px;
        transition: all var(--transition-fast);
    }
    .topic-pill:hover {
        background-color: var(--color-primary);
        color: #FFFFFF;
        border-color: var(--color-primary);
    }

    /* Top Quick Links Bar */
    .quick-nav-bar {
        background: var(--color-bg-surface);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-md);
        padding: 12px 18px;
        margin-bottom: 24px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        box-shadow: var(--shadow-md);
        position: sticky;
        top: 2.875rem;
        z-index: 99;
    }
    .quick-nav-link {
        color: var(--color-cream) !important;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.88rem;
        padding: 6px 14px;
        border-radius: var(--radius-sm);
        background-color: var(--color-bg-subtle);
        border: 1px solid var(--color-border);
        transition: all var(--transition-fast);
    }
    .quick-nav-link:hover {
        background-color: var(--color-primary-hover);
        color: #FFFFFF !important;
        border-color: var(--color-primary-hover);
        text-decoration: none;
        transform: translateY(-1px);
        box-shadow: var(--shadow-xs);
    }
    .quick-nav-link.active {
        background-color: var(--color-primary) !important;
        color: #FFFFFF !important;
        border-color: var(--color-accent) !important;
        box-shadow: var(--shadow-sm);
    }

    /* Sidebar Direct Chapter Links */
    .sidebar-chapter-link {
        display: flex;
        align-items: center;
        padding: 6px 10px;
        border-radius: var(--radius-sm);
        color: var(--color-cream-soft);
        text-decoration: none;
        font-weight: 500;
        transition: all var(--transition-fast);
    }
    .sidebar-chapter-link:hover {
        background-color: var(--color-bg-elevated);
        color: var(--color-cream);
        text-decoration: none;
    }
    .sidebar-chapter-link.active {
        background-color: var(--color-primary) !important;
        color: #FFFFFF !important;
        font-weight: 600;
    }

    /* Streamlit Buttons Consistent Styling */
    .stButton > button, div[data-testid="stLinkButton"] > a {
        font-family: var(--font-family) !important;
        font-weight: 600 !important;
        border-radius: var(--radius-sm) !important;
        transition: all var(--transition-fast) !important;
        border: 1px solid var(--color-primary) !important;
        background-color: var(--color-primary) !important;
        color: var(--color-cream) !important;
        box-shadow: var(--shadow-xs);
    }
    .stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        border-color: var(--color-primary-hover) !important;
        color: #FFFFFF !important;
        background-color: var(--color-primary-hover) !important;
        box-shadow: var(--shadow-sm);
        transform: translateY(-1px);
    }
    .stButton > button:focus, div[data-testid="stLinkButton"] > a:focus {
        border-color: var(--color-accent) !important;
        box-shadow: 0 0 0 2px rgba(244, 247, 205, 0.4) !important;
    }

    /* Form Submit Button */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: var(--color-primary) !important;
        color: #FFFFFF !important;
        border: 1px solid var(--color-primary) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        padding: 8px 18px !important;
        box-shadow: var(--shadow-sm);
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: var(--color-primary-hover) !important;
        border-color: var(--color-primary-hover) !important;
        box-shadow: var(--shadow-md);
        transform: translateY(-1px);
    }

    /* Streamlit Tabs Styling */
    div[data-baseweb="tab-list"] {
        border-bottom: 1px solid var(--color-border) !important;
        background-color: transparent !important;
    }
    button[data-baseweb="tab"] {
        font-family: var(--font-family) !important;
        font-weight: 500 !important;
        color: var(--color-cream-muted) !important;
        padding: 10px 18px !important;
        border-bottom: 2px solid transparent !important;
        background-color: transparent !important;
        transition: all var(--transition-fast) !important;
    }
    button[data-baseweb="tab"]:hover {
        color: var(--color-cream) !important;
        background-color: rgba(179, 47, 78, 0.15) !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: var(--color-accent) !important;
        font-weight: 700 !important;
        border-bottom-color: var(--color-primary) !important;
        background-color: rgba(179, 47, 78, 0.2) !important;
    }

    /* Form Controls: Inputs, Textarea, Select */
    div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] > div {
        background-color: var(--color-bg-surface) !important;
        border-color: var(--color-border) !important;
        border-radius: var(--radius-sm) !important;
    }
    div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
        font-family: var(--font-family) !important;
        color: var(--color-cream) !important;
        background-color: var(--color-bg-surface) !important;
    }
    div[data-baseweb="input"] input::placeholder, div[data-baseweb="textarea"] textarea::placeholder {
        color: var(--color-cream-muted) !important;
        opacity: 0.7;
    }
    div[data-baseweb="input"]:focus-within, div[data-baseweb="textarea"]:focus-within, div[data-baseweb="select"] > div:focus-within {
        border-color: var(--color-primary) !important;
        box-shadow: 0 0 0 1px var(--color-primary) !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: var(--color-cream) !important;
    }
    /* Select dropdown popover */
    ul[role="listbox"] {
        background-color: var(--color-bg-surface) !important;
        border: 1px solid var(--color-border) !important;
    }
    li[role="option"] {
        color: var(--color-cream) !important;
        background-color: var(--color-bg-surface) !important;
    }
    li[role="option"]:hover, li[role="option"][aria-selected="true"] {
        background-color: var(--color-primary) !important;
        color: #FFFFFF !important;
    }

    /* Streamlit Expander styling */
    div[data-testid="stExpander"] {
        border: 1px solid var(--color-border) !important;
        border-radius: var(--radius-md) !important;
        background-color: var(--color-bg-surface) !important;
        box-shadow: var(--shadow-xs) !important;
    }
    div[data-testid="stExpander"] details summary {
        font-weight: 600 !important;
        color: var(--color-cream) !important;
        background-color: var(--color-bg-surface) !important;
    }
    div[data-testid="stExpander"] details summary:hover {
        color: var(--color-accent) !important;
        background-color: var(--color-bg-elevated) !important;
    }
    div[data-testid="stExpander"] details summary svg,
    div[data-testid="stExpander"] details summary span:has(svg),
    div[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"] {
        font-family: inherit !important;
        color: var(--color-cream-soft) !important;
    }
    div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        background-color: var(--color-bg-surface) !important;
        color: var(--color-cream-soft) !important;
        border-top: 1px solid var(--color-border) !important;
    }

    /* Streamlit Alert Boxes (Info, Success, Warning, Error) */
    div[data-testid="stAlert"] {
        background-color: var(--color-bg-surface) !important;
        color: var(--color-cream) !important;
        border: 1px solid var(--color-border) !important;
        border-radius: var(--radius-md) !important;
    }
    div[data-testid="stAlert"] p {
        color: var(--color-cream) !important;
    }

    /* Streamlit Dataframe dark mode styling */
    div[data-testid="stDataFrame"] {
        border: 1px solid var(--color-border) !important;
        border-radius: var(--radius-md) !important;
        background-color: var(--color-bg-surface) !important;
    }

    /* Sidebar Clean Styling */
    section[data-testid="stSidebar"] {
        background-color: var(--color-bg-surface) !important;
        border-right: 1px solid var(--color-border) !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4 {
        color: var(--color-cream) !important;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: var(--color-cream-soft) !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: var(--color-border) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 1. SESSION STATE INITIALIZATION
# ==============================================================================

if "contact_submitted" not in st.session_state:
    st.session_state.contact_submitted = False
if "submission_details" not in st.session_state:
    st.session_state.submission_details = {}
if "last_refresh_time" not in st.session_state:
    st.session_state.last_refresh_time = datetime.now().strftime("%I:%M %p")

# ==============================================================================
# 2. DATA DEFINITIONS (Skills, Projects, Profile Details)
# ==============================================================================

SKILLS_DATA = [
    # Programming Languages
    {"Category": "Programming Languages", "Skill": "Python", "Proficiency": 80, "Experience": "2+ Years", "Note": "Data analysis, Streamlit, scripting"},
    {"Category": "Programming Languages", "Skill": "Java", "Proficiency": 80, "Experience": "2 Years", "Note": "OOP, academic projects, GUI"},
    {"Category": "Programming Languages", "Skill": "JavaScript / TypeScript", "Proficiency": 80, "Experience": "2 Years", "Note": "Modern web frontend & DOM"},
    {"Category": "Programming Languages", "Skill": "C#", "Proficiency": 80, "Experience": "Under 1 Year", "Note": "Blazor web apps, .NET syntax"},
    {"Category": "Programming Languages", "Skill": "C / C++", "Proficiency": 80, "Experience": "2 Years", "Note": "Data structures and algorithms"},
    # Web & Frameworks
    {"Category": "Web & Frameworks", "Skill": "Streamlit", "Proficiency": 65, "Experience": "Under 1 Year", "Note": "Interactive dashboards & data apps"},
    {"Category": "Web & Frameworks", "Skill": "Blazor (.NET)", "Proficiency": 65, "Experience": "Under 1 Year", "Note": "C# web client components"},
    {"Category": "Web & Frameworks", "Skill": "HTML5 / CSS3", "Proficiency": 86, "Experience": "2+ Years", "Note": "Responsive layout & web styling"},
    {"Category": "Web & Frameworks", "Skill": "React", "Proficiency": 75, "Experience": "2 Years", "Note": "Component architecture fundamentals"},
    # Databases & Tools
    {"Category": "Databases & Tools", "Skill": "Git & GitHub", "Proficiency": 85, "Experience": "2+ Years", "Note": "Branching, PRs, version control"},
    {"Category": "Databases & Tools", "Skill": "VS Code & JetBrains", "Proficiency": 90, "Experience": "2+ Years", "Note": "Primary IDE & debugging workflows"},
    {"Category": "Databases & Tools", "Skill": "Figma", "Proficiency": 95, "Experience": "2+ Years", "Note": "UI/UX wireframing & prototyping"},
    {"Category": "Databases & Tools", "Skill": "Photoshop", "Proficiency": 95, "Experience": "2+ Years", "Note": "Graphic Design"},
    {"Category": "Databases & Tools", "Skill": "Illustrator", "Proficiency": 95, "Experience": "2+ Years", "Note": "Graphic Design"},
    # Soft & Professional Skills
    {"Category": "Soft Skills", "Skill": "Problem Solving", "Proficiency": 85, "Experience": "Ongoing", "Note": "Algorithmic thinking & debugging"},
    {"Category": "Soft Skills", "Skill": "Team Collaboration", "Proficiency": 85, "Experience": "Ongoing", "Note": "Agile peer programming & group projects"},
    {"Category": "Soft Skills", "Skill": "Technical Writing", "Proficiency": 80, "Experience": "Ongoing", "Note": "Documentation, project reports, slides"},
    {"Category": "Soft Skills", "Skill": "Adaptability", "Proficiency": 85, "Experience": "Ongoing", "Note": "Fast learner with emerging frameworks"},
]

CURATED_PROJECTS = [
    {
        "title": "tela&tulle website | cebu dress rentals",
        "category": "Web Applications",
        "role": "Lead UI/UX & Full-Stack Developer",
        "tech": ["ReactJS", "Tailwind CSS", "Supabase"],
        "description": (
            "A functional prototype for a local Cebu-based dress rental service, featuring a responsive ReactJS frontend, "
            "and a Supabase backend."
        ),
        "outcome": "Completed functional prototype with interactive rental grids and responsive filtering.",
        "repo_url": "https://tela-and-tulle-rental.vercel.app/home",
        "details": (
            "Key features include real-time dress availability viewing, dynamic price calculations, "
            "and reactive state handling using ReactJS."
        ),
    },
    {
        "title": "Wildkatseye - Interactive HCI Prototype",
        "category": "UI/UX & Frontend",
        "role": "Frontend Developer & Interaction Designer",
        "tech": ["TypeScript", "HTML5", "CSS3", "Figma"],
        "description": (
            "A course capstone prototype developed for the Human-Computer Interaction (HCI) subject, "
            "focusing on user-centric heuristics, accessible design, and responsive interaction."
        ),
        "outcome": "Presented as the final course project; received high appraisal for usability and consistency.",
        "repo_url": "https://github.com/milkuiii/wildkatseye-hci",
        "details": (
            "Demonstrated micro-interactions, accessibility-focused color schemes, "
            "and intuitive layout hierarchy evaluated through peer usability testing."
        ),
    },
    {
        "title": "Salamin at Bakal - DOST Game Jam Entry",
        "category": "Game Development",
        "role": "Asset Designer & UI/UX Contributor",
        "tech": ["Godot", "GDScript", "Aseprite"],
        "description": (
            "An educational card game that takes players through a fantasy world while teaching them about sign language."
        ),
        "outcome": "Successfully completed and awarded as the 4th runner up at the DOST Game Jam.",
        "repo_url": "https://github.com/binggbongg/dost-game-dev",
        "details": (
            "Fun gameplay!"
        ),
    },
    {
        "title": "Information Management Capstone",
        "category": "Database Systems",
        "role": "Database Designer & Backend Contributor",
        "tech": ["PHP", "MySQL", "Bootstrap", "Apache"],
        "description": (
            "A relational database management portal built for academic record tracking, featuring normalized database "
            "tables, structured SQL queries, and role-based user management."
        ),
        "outcome": "Fully operational academic CRUD portal with data validation and report generation.",
        "repo_url": "https://github.com/milkuiii/im-logarta-monceda",
        "details": (
            "Designed 3NF database schema, implemented stored procedures, and created secure authentication workflows."
        ),
    },
]

# Section IDs mapping for continuous single-page navigation
SECTION_ID_MAP = {
    "About Me": "about-me",
    "Autobiography": "autobiography",
    "Skills & Proficiency": "skills-proficiency",
    "Featured Projects": "featured-projects",
    "GitHub Repositories": "github-repositories",
    "Contact & Feedback": "contact-feedback",
}

# ==============================================================================
# 3. GITHUB API SERVICE (Cached with Graceful Error Handling)
# ==============================================================================

@st.cache_data(ttl=600, show_spinner=False)
def fetch_github_repositories(username: str) -> Dict[str, Any]:
    """
    Fetch public repositories from GitHub REST API.
    Cached for 10 minutes (600s) to respect API rate limits.
    """
    clean_username = username.strip()
    if not clean_username:
        return {"success": False, "error": "Username cannot be empty", "repos": []}

    api_url = f"https://api.github.com/users/{clean_username}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Streamlit-Portfolio-milkuiii",
    }
    params = {"per_page": 50, "sort": "updated", "type": "public"}

    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            repos_data = response.json()
            processed_repos = []
            for item in repos_data:
                processed_repos.append(
                    {
                        "name": item.get("name", "Untitled"),
                        "description": item.get("description") or "No description provided.",
                        "language": item.get("language") or "Other",
                        "stars": item.get("stargazers_count", 0),
                        "forks": item.get("forks_count", 0),
                        "updated_at": item.get("updated_at", ""),
                        "html_url": item.get("html_url", "#"),
                        "topics": item.get("topics", []),
                        "is_fork": item.get("fork", False),
                    }
                )
            return {"success": True, "error": None, "repos": processed_repos}
        elif response.status_code == 404:
            return {"success": False, "error": f"GitHub user '{clean_username}' was not found.", "repos": []}
        elif response.status_code == 403:
            return {
                "success": False,
                "error": "GitHub API rate limit exceeded. Please wait a few minutes or view GitHub directly.",
                "repos": [],
            }
        else:
            return {
                "success": False,
                "error": f"GitHub API responded with status code {response.status_code}.",
                "repos": [],
            }
    except requests.exceptions.Timeout:
        return {"success": False, "error": "Connection timed out while contacting GitHub API.", "repos": []}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Network error contacting GitHub API: {e}", "repos": []}


# ==============================================================================
# 4. SIDEBAR NAVIGATION & PORTFOLIO CONTROLS
# ==============================================================================

with st.sidebar:
    st.markdown(f"### 👩‍💻 {STUDENT_NAME}")
    st.markdown(
        f"""
        <div class="student-badge">{STUDENT_SECTION}</div>
        <p style="font-size: 0.88rem; color: var(--color-neutral-muted); margin-top: 4px;">
            <strong>Program:</strong> {STUDENT_PROGRAM}<br>
            <strong>Year:</strong> {STUDENT_YEAR}<br>
            <strong>Campus:</strong> {STUDENT_SCHOOL}
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("#### 🧭 Table of Contents")

    # STREAMLIT-OPTION-MENU NAVIGATION
    nav_options = [
        "About Me",
        "Autobiography",
        "Skills & Proficiency",
        "Featured Projects",
        "GitHub Repositories",
        "Contact & Feedback",
    ]
    nav_icons = [
        "person-badge",
        "book",
        "bar-chart-steps",
        "laptop",
        "github",
        "envelope-paper",
    ]

    selected_menu = option_menu(
        menu_title=None,
        options=nav_options,
        icons=nav_icons,
        default_index=0,
        styles={
            "container": {"padding": "4px 0", "background-color": "transparent"},
            "icon": {"color": "#F4F7CD", "font-size": "15px"},
            "nav-link": {
                "font-family": '"Helvetica Now", "Helvetica Neue", Helvetica, Arial, sans-serif',
                "font-size": "14px",
                "text-align": "left",
                "margin": "3px 0",
                "padding": "8px 12px",
                "border-radius": "8px",
                "color": "#E8E1C8",
                "--hover-color": "#5E1A31",
            },
            "nav-link-selected": {
                "background-color": "#B32F4E",
                "color": "#F4F1DE",
                "font-weight": "600",
            },
        },
    )

    # Clickable Chapter Hyperlinks in Sidebar
    # st.markdown(
    #     f"""
    #     <div style="margin-top: 6px; padding: 10px 12px; background-color: #3D1424; border-radius: 8px; border: 1px solid #5C2236;">
    #         <p style="font-size: 0.78rem; font-weight: 700; color: #E8E1C8; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.04em;">Direct Chapter Links:</p>
    #         <div style="display: flex; flex-direction: column; gap: 4px; font-size: 0.85rem;">
    #             <a href="#about-me" data-section="about-me" class="sidebar-chapter-link">📌 #about-me</a>
    #             <a href="#autobiography" data-section="autobiography" class="sidebar-chapter-link">📌 #autobiography</a>
    #             <a href="#skills-proficiency" data-section="skills-proficiency" class="sidebar-chapter-link">📌 #skills-proficiency</a>
    #             <a href="#featured-projects" data-section="featured-projects" class="sidebar-chapter-link">📌 #featured-projects</a>
    #             <a href="#github-repositories" data-section="github-repositories" class="sidebar-chapter-link">📌 #github-repositories</a>
    #             <a href="#contact-feedback" data-section="contact-feedback" class="sidebar-chapter-link">📌 #contact-feedback</a>
    #         </div>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # st.markdown("---")
    # st.markdown("#### ⚙️ GitHub Integration Config")
    github_user_input = st.text_input(
        "GitHub Username:",
        value=DEFAULT_GITHUB_USERNAME,
        help="Update this username to dynamically load any public GitHub profile's repositories.",
    )

    # refresh_clicked = st.button("🔄 Refresh GitHub Data", use_container_width=True)
    # if refresh_clicked:
    #     fetch_github_repositories.clear()
    #     st.session_state.last_refresh_time = datetime.now().strftime("%I:%M %p")
    #     st.toast("GitHub cache cleared and refreshed!", icon="✅")

    # st.caption(f"Last updated cache: {st.session_state.last_refresh_time}")

    # st.markdown("---")
    # st.markdown("#### 📄 Résumé Summary")
    # resume_path = os.path.join(os.path.dirname(__file__), "assets", "resume_summary.txt")
    # if os.path.exists(resume_path):
    #     with open(resume_path, "r", encoding="utf-8") as f:
    #         resume_bytes = f.read()
    #     st.download_button(
    #         label="📥 Download Résumé (TXT)",
    #         data=resume_bytes,
    #         file_name=f"{STUDENT_NAME.replace(' ', '_')}_Resume.txt",
    #         mime="text/plain",
    #         use_container_width=True,
    #     )

    st.markdown("---")
    # show_fun_facts = st.checkbox("Show quick fun facts in sidebar", value=True)
    # if show_fun_facts:
    st.markdown("💡 **Fun Fact:** Alumna of Philippine Science High School (PSHS-CVisC) and enthusiastic about web technologies!")


# Auto-scroll helper and ScrollSpy synchronizer
target_anchor_id = SECTION_ID_MAP.get(selected_menu, "about-me")
components.html(
    f"""
    <script>
    (function() {{
        const targetId = "{target_anchor_id}";
        const parentDoc = window.parent.document;
        const parentWin = window.parent;

        // 1. Smooth scroll to target anchor when sidebar menu item is clicked
        setTimeout(() => {{
            const el = parentDoc.getElementById(targetId);
            if (el) {{
                el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}, 150);

        // 2. ScrollSpy: Listen to scroll events on parent window to highlight the current chapter
        const sectionIds = [
            "about-me",
            "autobiography",
            "skills-proficiency",
            "featured-projects",
            "github-repositories",
            "contact-feedback"
        ];

        function updateActiveSection() {{
            let currentActive = sectionIds[0];
            const scrollPos = parentWin.scrollY || parentDoc.documentElement.scrollTop || 0;
            const windowHeight = parentWin.innerHeight || parentDoc.documentElement.clientHeight;
            const fullHeight = parentDoc.documentElement.scrollHeight;

            // If user has scrolled near bottom of page, activate the last chapter (contact-feedback)
            if (scrollPos + windowHeight >= fullHeight - 120) {{
                currentActive = sectionIds[sectionIds.length - 1];
            }} else {{
                for (let i = 0; i < sectionIds.length; i++) {{
                    const el = parentDoc.getElementById(sectionIds[i]);
                    if (el) {{
                        const rect = el.getBoundingClientRect();
                        // Section is considered active if its top is near or past the top trigger line
                        if (rect.top <= 200) {{
                            currentActive = sectionIds[i];
                        }}
                    }}
                }}
            }}

            // Highlight in Top Quick Nav Bar
            const quickLinks = parentDoc.querySelectorAll('.quick-nav-link');
            quickLinks.forEach(link => {{
                const target = link.getAttribute('data-section') || (link.getAttribute('href') || '').replace('#', '');
                if (target === currentActive) {{
                    link.classList.add('active');
                }} else {{
                    link.classList.remove('active');
                }}
            }});

            // Highlight in Sidebar Direct Chapter Links
            const sidebarLinks = parentDoc.querySelectorAll('.sidebar-chapter-link');
            sidebarLinks.forEach(link => {{
                const target = link.getAttribute('data-section') || (link.getAttribute('href') || '').replace('#', '');
                if (target === currentActive) {{
                    link.classList.add('active');
                }} else {{
                    link.classList.remove('active');
                }}
            }});

            // Synchronize streamlit-option-menu in sidebar if present
            const optionMenuLinks = parentDoc.querySelectorAll('section[data-testid="stSidebar"] [data-baseweb="tab"], section[data-testid="stSidebar"] .nav-link');
            const sectionIndexMap = {{
                "about-me": 0,
                "autobiography": 1,
                "skills-proficiency": 2,
                "featured-projects": 3,
                "github-repositories": 4,
                "contact-feedback": 5
            }};
            const activeIdx = sectionIndexMap[currentActive];
            if (optionMenuLinks && optionMenuLinks.length > 0 && typeof activeIdx === 'number') {{
                optionMenuLinks.forEach((link, idx) => {{
                    if (idx === activeIdx) {{
                        link.style.setProperty('background-color', '#B32F4E', 'important');
                        link.style.setProperty('color', '#FFFFFF', 'important');
                        const icon = link.querySelector('i, svg');
                        if (icon) icon.style.setProperty('color', '#FFFFFF', 'important');
                    }} else {{
                        link.style.removeProperty('background-color');
                        link.style.removeProperty('color');
                        const icon = link.querySelector('i, svg');
                        if (icon) icon.style.removeProperty('color');
                    }}
                }});
            }}
        }}

        // Attach listeners
        parentWin.removeEventListener('scroll', updateActiveSection);
        parentWin.addEventListener('scroll', updateActiveSection, {{ passive: true }});
        
        // Initial invocation to set the state immediately
        setTimeout(updateActiveSection, 300);
        setTimeout(updateActiveSection, 800);
    }})();
    </script>
    """,
    height=0,
    width=0,
)


# ==============================================================================
# 5. SECTION RENDERING FUNCTIONS (CONTINUOUS PAGE WITH HYPERLINKS)
# ==============================================================================

def render_top_quick_links():
    """Renders a responsive hyperlinked jump bar at the top of the single continuous page."""
    st.markdown(
        """
        <div class="quick-nav-bar">
            <span style="font-size: 0.85rem; font-weight: 700; color: var(--color-neutral-muted); letter-spacing: 0.02em;">📑 Jump to Chapter:</span>
            <a href="#about-me" data-section="about-me" class="quick-nav-link">👋 About Me</a>
            <a href="#autobiography" data-section="autobiography" class="quick-nav-link">📖 Autobiography</a>
            <a href="#skills-proficiency" data-section="skills-proficiency" class="quick-nav-link">⚡ Skills & Proficiency</a>
            <a href="#featured-projects" data-section="featured-projects" class="quick-nav-link">💻 Projects</a>
            <a href="#github-repositories" data-section="github-repositories" class="quick-nav-link">🐙 GitHub Repos</a>
            <a href="#contact-feedback" data-section="contact-feedback" class="quick-nav-link">📬 Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_about_me():
    """Renders the About Me hero section with anchor hyperlink."""
    st.markdown('<div id="about-me" class="section-anchor"></div>', unsafe_allow_html=True)
    
    st.title(f"👋 Hello, I'm {STUDENT_NAME}!")
    st.markdown(
        f'<div class="student-badge">Section: {STUDENT_SECTION}</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        profile_img_path = os.path.join(os.path.dirname(__file__), "assets", "profile.png")
        if os.path.exists(profile_img_path):
            st.image(
                profile_img_path,
                caption=f"{STUDENT_NAME} — GitHub: @{DEFAULT_GITHUB_USERNAME}",
                use_container_width=True,
            )
        else:
            st.info("📸 Profile image placeholder: Add photo to `assets/profile.png`")

        # Key Quick Links
        st.markdown(
            f"""
            - 🌐 **Location:** {STUDENT_LOCATION}
            - 🐙 **GitHub:** [{DEFAULT_GITHUB_USERNAME}](https://github.com/{DEFAULT_GITHUB_USERNAME})
            - 💼 **LinkedIn:** [Sophia Logarta](https://www.linkedin.com/in/sophialogarta/)
            - ✉️ **Email:** `snlogarta@gmail.com`
            """
        )

    with col2:
        st.header("About Me")
        st.write(
            f"""
            Welcome to my interactive portfolio website! I am an undergraduate student currently enrolled in 
            the **{STUDENT_PROGRAM}** program at **{STUDENT_SCHOOL}**. 
            
            With a solid science and research foundation developed during my high school years at 
            **{STUDENT_ALMA_MATER}**, I am passionate about crafting responsive, user-friendly 
            applications and exploring modern software engineering workflows. Outside of technical projects,
            I enjoy creative projects that combine technology with artistry. My current pursuits focus on 
            full-stack development, graphic design, and intuitive data visualization tools.
            """
        )

        # Additional Streamlit Feature: Metrics
        st.subheader("Key Portfolio Highlights")
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Current Academic Year", value="3rd Year", delta="CIT-U BSCS")
        m2.metric(label="Curated Projects", value=f"{len(CURATED_PROJECTS)}", delta="Showcased")
        m3.metric(label="Public Repositories", value="13+", delta="Live on GitHub")

        st.markdown("---")
        # Meaningful button interaction to toggle quick spotlight
        if "reveal_motto" not in st.session_state:
            st.session_state.reveal_motto = False

        btn_col1, btn_col2 = st.columns([1, 2])
        with btn_col1:
            if st.button("✨ Reveal My Guiding Motto", key="btn_motto", use_container_width=True):
                st.session_state.reveal_motto = not st.session_state.reveal_motto

        with btn_col2:
            if st.session_state.reveal_motto:
                st.success("🌱 *'If it's meant for you, it will happen at the right time.'*")


def render_autobiography():
    """Renders the comprehensive first-person autobiography section with anchor hyperlink."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div id="autobiography" class="section-anchor"></div>', unsafe_allow_html=True)
    
    st.header("📖 My Autobiography")
    st.write(
        "Here is a deeper look into who I am, where my journey began, what drives me, "
        "and where I hope to go in the future."
    )

    # Streamlit Feature: Tabs for organizing autobiography facets cleanly
    tab_personal, tab_education, tab_milestones, tab_aspirations = st.tabs(
        ["🌱 Background & Journey", "🎓 Education", "🏆 Milestones & Hobbies", "🚀 Aspirations & Goals"]
    )

    with tab_personal:
        st.subheader("Personal Background")
        st.write(
            f"""
            Born and raised in Cebu City, Philippines, I have always been captivated by how digital systems and 
            interactive experiences shape everyday living. From starting with creating Powerpoints on my Mom's work laptop,
            to helping my dad build computers, to creating applications for my organization's outreaches, and now running local AI agents on my personal setup. 
            I've always loved how tech can improve our daily lives and initiatives.
            
            Studying in Argao and living in Cebu City has given me 
            access to diverse communities of student developers, mentors, and creators who continually inspire 
            me to develop practical software solutions.
            """
        )

    with tab_education:
        st.subheader("Educational Journey")
        st.markdown(
            f"""
            - **Philippine Science High School - Central Visayas Campus (PSHS-CVisC '24)**  
              *Secondary Education (Biology Core, DMT Elective, Computer Science Elective)*  
              Immersed in an intensive science and mathematics curriculum. My time at Pisay fortified my discipline 
              in analytical reasoning, research methodologies, and scientific inquiry. It also introduced me to 
              foundational computing principles that sparked my ambition to pursue Computer Science at the college level.

            - **Cebu Institute of Technology - University (CIT-U)**  
              *Bachelor of Science in Computer Science (BSCS) | 3rd Year*  
              Currently active in core computer science coursework, including data structures and algorithms, 
              object-oriented programming (Java/C#), web development, and database systems. CIT-U has provided 
              valuable opportunities for collaborative coursework and hands-on system building.
            """
        )

    with tab_milestones:
        st.subheader("Important Milestones & Hobbies")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown(
                """
                **Memorable Milestones:**
                1. **Graduating from PSHS-CVisC (Class of 2024):** 6 years away from home is an experience that has shaped my character and resilience. Pisay has forged me in a 
                way that's cultivated my love for inquiry, the Philippine's incredible biodiversity, and our country's scientific community.
                2. **Creating Various Game Development Projects:** From the *Wildkatseye* HCI project to our winning *UPCSG Game Development* project, I've gained valuable experience 
                and built memorable moments in game design and development.
                3. **4+ Years of Creative Freelance Work:** Creating for various clients and platforms gave me a different perspective on user needs and design challenges. This experience
                allowed me to refine my skills in UI/UX design, client communication, and project management.
                4. **Leadership Roles:** Being a student leader has helped me gauge my strengths and weaknesses in collaboration, communication, and mentorship. 
                It has also taught me how to adapt when working with a diverse team of individuals with different skill sets and perspectives. From starting out as a KALFI Leader,
                to being a Supreme Student Government (SSG) officer, and now the GDGoC Chief Operations Officer, these various roles taught me how to lead with empathy and intention.
                """
            )
        with col_m2:
            st.markdown(
                """
                **Interests & Hobbies:**
                - 🎨 **User-Centered Design:** Creating designs that prioritize user needs and experiences through Figma, Photoshop, Illustrator, and other design tools.
                - 🧩 **Logical Problem Solving:** Leetcode. Warcraft III. VALORANT with rage-baiting teammates.
                - ☕ **Lifestyle:** I love to keep myself active through regular exercise.
                """
            )

    with tab_aspirations:
        st.subheader("Future Aspirations & Career Interests")
        st.write(
            """
            As I progress in my undergraduate program, I hope to gain deeper expertise in applying technology
            to solve real-world problems. I would love to bring value and contribute meaningfully to projects. Whether it be through full-stack development, data visualization, or AI integration, I aim to contribute to projects that
            have a meaningful impact on communities. My long-term goal is to work in a collaborative environment where I can continue to learn, innovate, and mentor 
            others :)
            """
        )


def render_skills():
    """Renders the Skills section with organized categories, dataframe table, and interactive chart."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div id="skills-proficiency" class="section-anchor"></div>', unsafe_allow_html=True)

    st.header("⚡ Technical & Personal Competencies")
    st.write(
        "A breakdown of my current proficiency across programming languages, development frameworks, "
        "database tools, and professional soft skills. These numbers are based of self-assessment. Use the interactive controls below to filter and inspect."
    )

    df_skills = pd.DataFrame(SKILLS_DATA)

    # Streamlit Selectbox Component
    categories = ["All Categories"] + sorted(list(df_skills["Category"].unique()))
    selected_category = st.selectbox("Filter Skills by Category:", options=categories, index=0)

    # Streamlit Slider Component: proficiency threshold
    min_proficiency = st.slider(
        "Filter by Minimum Proficiency Score (%):",
        min_value=50,
        max_value=100,
        value=65,
        step=5,
        help="Adjust this slider to only display skills meeting or exceeding the selected threshold.",
    )

    # Apply filters
    filtered_df = df_skills[df_skills["Proficiency"] >= min_proficiency]
    if selected_category != "All Categories":
        filtered_df = filtered_df[filtered_df["Category"] == selected_category]

    st.markdown(f"**Showing {len(filtered_df)} of {len(df_skills)} skills** (Threshold: ≥ {min_proficiency}%)")

    # Layout: Table alongside Interactive Chart
    col_chart, col_table = st.columns([1.1, 1], gap="medium")

    with col_chart:
        st.subheader("📊 Skill Proficiency Visualization")
        if not filtered_df.empty:
            chart_data = filtered_df[["Skill", "Proficiency"]].set_index("Skill")
            st.bar_chart(chart_data, color="#B32F4E", use_container_width=True)
            st.caption("Bar chart showing self-assessed proficiency scores on a 0-100 scale.")
        else:
            st.warning("No skills match the selected filter criteria. Try adjusting the slider or category.")

    with col_table:
        st.subheader("📋 Detailed Skills Table")
        if not filtered_df.empty:
            st.dataframe(
                filtered_df[["Category", "Skill", "Proficiency", "Experience"]],
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No records to display.")

    with st.expander("ℹ️ How These Scores Are Evaluated"):
        st.write(
            """
            - **85 - 100%:** High familiarity; regularly used in academic projects, personal tools, or daily coursework.
            - **70 - 84%:** Solid working competence; capable of independent debugging, API usage, and feature implementation.
            - **50 - 69%:** Foundational familiarity; comfortable reading documentation, syntax, and building standard components.
            """
        )


def render_curated_projects():
    """Renders the curated projects with category filtering and expandable technical details."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div id="featured-projects" class="section-anchor"></div>', unsafe_allow_html=True)

    st.header("💻 Curated Academic & Personal Projects")
    st.write(
        "A selection of key academic and personal projects demonstrating full-stack engineering, "
        "UI/UX prototyping, and software development methodologies."
    )

    all_categories = sorted(list({p["category"] for p in CURATED_PROJECTS}))
    selected_tech_filter = st.multiselect(
        "Filter projects by category:",
        options=all_categories,
        default=all_categories,
    )

    filtered_projects = [p for p in CURATED_PROJECTS if p["category"] in selected_tech_filter]

    if not filtered_projects:
        st.warning("No curated projects match your selected category filter.")
        return

    # Render projects using columns
    for project in filtered_projects:
        with st.container():
            st.markdown(
                f"""
                <div class="portfolio-card">
                    <h3 style="margin-top:0; color:var(--color-primary);">{project['title']}</h3>
                    <p style="color:var(--color-neutral-muted); font-size:0.9rem; margin-bottom:8px;">
                        <strong>Category:</strong> {project['category']} &nbsp;|&nbsp; 
                        <strong>Role:</strong> {project['role']}
                    </p>
                    <p style="color:var(--color-neutral-text);">{project['description']}</p>
                    <p style="color:var(--color-neutral-text);"><strong>Outcome / Status:</strong> {project['outcome']}</p>
                    <div>
                        {''.join([f'<span class="topic-pill">{t}</span>' for t in project['tech']])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            p_col1, p_col2 = st.columns([1, 3])
            with p_col1:
                if project.get("repo_url"):
                    st.link_button("🔗 View Repository", project["repo_url"], use_container_width=True)
            with p_col2:
                with st.expander(f"🔍 Implementation Details: {project['title']}"):
                    st.write(project["details"])


def render_github_section(username: str):
    """Renders the dynamic GitHub repositories retrieved via the GitHub REST API."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div id="github-repositories" class="section-anchor"></div>', unsafe_allow_html=True)

    st.header("🐙 Dynamic GitHub Repositories")
    # st.write(
    #     f"Live repository feed retrieved dynamically from GitHub for account: **[@{username}](https://github.com/{username})**. "
    #     "This data updates automatically via GitHub's REST API and utilizes Streamlit caching (`st.cache_data`) for efficiency."
    # )

    with st.spinner(f"Fetching latest repositories for '{username}'..."):
        api_result = fetch_github_repositories(username)

    if not api_result["success"]:
        st.error(f"⚠️ {api_result['error']}")
        st.info("You can change the username in the sidebar or check if the configured profile is public.")
        return

    repos = api_result["repos"]
    if not repos:
        st.info(f"User '@{username}' has no public repositories available to display.")
        return

    # Extract all programming languages for filtering
    languages = sorted(list({r["language"] for r in repos if r["language"]}))
    languages_options = ["All Languages"] + languages

    # Interactive controls row
    c_search, c_lang, c_sort = st.columns([2, 1.5, 1.5])
    with c_search:
        search_query = st.text_input("🔍 Search Repositories:", placeholder="Search by name or description...")
    with c_lang:
        selected_lang = st.selectbox("Filter by Language:", options=languages_options, index=0)
    with c_sort:
        sort_by = st.selectbox("Sort By:", options=["Recently Updated", "Repository Name", "Stars Count"], index=0)

    # Filter logic
    filtered_repos = repos
    if search_query:
        query_clean = search_query.strip().lower()
        filtered_repos = [
            r for r in filtered_repos
            if query_clean in r["name"].lower() or query_clean in r["description"].lower()
        ]

    if selected_lang != "All Languages":
        filtered_repos = [r for r in filtered_repos if r["language"] == selected_lang]

    # Sort logic
    if sort_by == "Recently Updated":
        filtered_repos = sorted(filtered_repos, key=lambda x: x["updated_at"], reverse=True)
    elif sort_by == "Repository Name":
        filtered_repos = sorted(filtered_repos, key=lambda x: x["name"].lower())
    elif sort_by == "Stars Count":
        filtered_repos = sorted(filtered_repos, key=lambda x: x["stars"], reverse=True)

    st.caption(f"Showing **{len(filtered_repos)}** of **{len(repos)}** repositories.")

    if not filtered_repos:
        st.warning("No repositories matched your filter criteria.")
        return

    # Render repos in 2-column cards layout
    for i in range(0, len(filtered_repos), 2):
        row_cols = st.columns(2, gap="medium")
        for j in range(2):
            if i + j < len(filtered_repos):
                repo = filtered_repos[i + j]
                with row_cols[j]:
                    updated_date_str = repo["updated_at"]
                    if updated_date_str:
                        try:
                            dt = datetime.strptime(updated_date_str, "%Y-%m-%dT%H:%M:%SZ")
                            formatted_date = dt.strftime("%b %d, %Y")
                        except Exception:
                            formatted_date = updated_date_str
                    else:
                        formatted_date = "N/A"

                    topics_html = "".join([f'<span class="topic-pill">#{t}</span>' for t in repo.get("topics", [])])

                    st.markdown(
                        f"""
                        <div class="portfolio-card">
                            <h4 style="margin-top:0;">
                                <a href="{repo['html_url']}" target="_blank" style="text-decoration:none; color:var(--color-primary); font-weight: 700;">
                                    📦 {repo['name']}
                                </a>
                            </h4>
                            <p style="font-size:0.9rem; color:var(--color-neutral-muted); min-height: 42px;">{repo['description']}</p>
                            <p style="font-size:0.8rem; color:var(--color-neutral-light); margin-bottom:6px;">
                                <strong>Language:</strong> {repo['language']} &nbsp;•&nbsp; 
                                ⭐ {repo['stars']} &nbsp;•&nbsp; 
                                🍴 {repo['forks']} &nbsp;•&nbsp; 
                                🕒 {formatted_date}
                            </p>
                            <div>{topics_html}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.link_button(f"Visit {repo['name']}", repo["html_url"], use_container_width=True)


def render_contact_form():
    """Renders the Contact & Feedback form with validation and clear submission handling."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div id="contact-feedback" class="section-anchor"></div>', unsafe_allow_html=True)

    st.header("📬 Get in Touch & Feedback")
    st.write(
        "Have a question, collaboration inquiry, or feedback on this portfolio application? "
        "Please fill out the form below."
    )

    # Show previous submission details if in session state
    if st.session_state.contact_submitted:
        st.success("✅ Thank you! Your submission was successfully processed in this session.")
        st.info(
            f"""
            **Recorded Details:**
            - **Sender:** {st.session_state.submission_details.get('name')} (`{st.session_state.submission_details.get('email')}`)
            - **Purpose:** {st.session_state.submission_details.get('purpose')}
            - **Consent Acknowledged:** {'Yes' if st.session_state.submission_details.get('consent') else 'No'}
            - **Submission Time:** {st.session_state.submission_details.get('timestamp')}
            
            *Notice: This form responds dynamically within this running Streamlit application. Since no external database or email relay is attached, the message has been acknowledged in session state rather than delivered externally.*
            """
        )
        if st.button("📝 Submit Another Response"):
            st.session_state.contact_submitted = False
            st.session_state.submission_details = {}
            st.rerun()
        return

    # Contact Form using st.form
    with st.form("portfolio_contact_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            name_input = st.text_input("Your Full Name *", placeholder="e.g. John Doe")
        with c2:
            email_input = st.text_input("Email Address *", placeholder="e.g. john.doe@example.com")

        purpose_input = st.selectbox(
            "Purpose of Contact *",
            options=[
                "Academic Inquiry / Collaboration",
                "Project Feedback / Critique",
                "Internship / Career Opportunity",
                "General Greeting & Networking",
            ],
            index=0,
        )

        contact_pref = st.radio(
            "Preferred Follow-Up Method:",
            options=["Email response", "No follow-up needed (feedback only)"],
            horizontal=True,
        )

        message_input = st.text_area(
            "Your Message or Feedback *",
            placeholder="Type your message here (minimum 10 characters)...",
            height=130,
        )

        consent_check = st.checkbox(
            "I understand that this form is part of a Streamlit portfolio demonstration.",
            value=True,
        )

        submit_button = st.form_submit_button("🚀 Send Message", use_container_width=True)

    if submit_button:
        # Form Validation
        errors = []
        if not name_input.strip():
            errors.append("Please enter your name.")
        
        email_clean = email_input.strip()
        email_regex = r"^[^@]+@[^@]+\.[^@]+$"
        if not email_clean:
            errors.append("Please enter your email address.")
        elif not re.match(email_regex, email_clean):
            errors.append("Please enter a valid email format (e.g., name@domain.com).")

        if not message_input.strip() or len(message_input.strip()) < 10:
            errors.append("Please provide a message with at least 10 characters.")

        if errors:
            for err in errors:
                st.error(f"⚠️ {err}")
        else:
            # Store submission in session state
            st.session_state.contact_submitted = True
            st.session_state.submission_details = {
                "name": name_input.strip(),
                "email": email_clean,
                "purpose": purpose_input,
                "pref": contact_pref,
                "consent": consent_check,
                "timestamp": datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"),
            }
            st.toast("Message received successfully!", icon="🎉")
            st.rerun()


# ==============================================================================
# 6. MAIN APPLICATION: ONE CONTINUOUS PAGE WITH HYPERLINKED CHAPTERS
# ==============================================================================

def main():
    # 1. Quick Navigation Bar with hyperlinks
    render_top_quick_links()

    # 2. Continuous Chapter Layout (All sections rendered seamlessly in one page)
    render_about_me()
    render_autobiography()
    render_skills()
    render_curated_projects()
    render_github_section(github_user_input)
    render_contact_form()

    # 3. Footer with back-to-top link
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align: center; color: var(--color-cream-muted); font-size: 0.85rem; padding: 24px 0;">
            <a href="#about-me" style="color: var(--color-accent); text-decoration: none; font-weight: 600;">⬆️ Back to Top</a><br><br>
            <strong style="color: var(--color-cream);">{STUDENT_NAME}</strong> • {STUDENT_SECTION} • {STUDENT_SCHOOL}<br>
            Powered by Streamlit, streamlit-option-menu, Python & GitHub REST API
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()