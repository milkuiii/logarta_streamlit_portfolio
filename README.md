# Sophia Gabrielle Logarta — Streamlit Portfolio Application

An interactive, responsive personal portfolio built with **Streamlit**, featuring academic background storytelling, data-driven skills visualization, curated projects, dynamic GitHub REST API integration, and contact/feedback handling.

---

## 🚀 Features

- **About Me Hero Section:** Highlights student name, degree program, academic year, campus, and profile photograph.
- **Autobiography:** Structured first-person narrative exploring personal background, STEM education at PSHS-CVisC, milestones, hobbies, and career goals organized in clean tabs.
- **Skills & Proficiency:** Comprehensive skills matrix categorized by programming languages, frameworks, databases, and soft skills with interactive proficiency threshold slider, bar chart visualization, and detailed data table.
- **Curated Projects:** Showcases featured projects (MyCloset Blazor, Wildkatseye HCI Prototype, Streamlit Portfolio, and Information Management Capstone) with roles, tech stack pills, outcomes, and expandable implementation deep dives.
- **Dynamic GitHub Repository Feed:** Real-time integration with GitHub's REST API (`@milkuiii`) featuring search, language filtering, sorting, caching (`@st.cache_data`), error handling, and manual cache refresh.
- **Contact & Feedback Form:** Structured contact form with real-time field and email format validation, feedback options, session state persistence, and clear submission acknowledgment.
- **Additional Streamlit Features:** Profile image handling, tabbed views, key metric callouts, session state tracking, downloadable résumé summary, and custom theme styling.

---

## 📦 Project Structure

```text
logarta_streamlit_portfolio/
├── .streamlit/
│   └── config.toml          # Custom theme configuration (colors, font)
├── assets/
│   ├── profile.png          # Profile avatar
│   └── resume_summary.txt   # Downloadable résumé summary
├── app.py                   # Main Streamlit application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Getting Started Locally

### 1. Prerequisites
- Python 3.9+ (Python 3.10 - 3.14 compatible)
- `pip` or virtual environment

### 2. Setup Virtual Environment
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/milkuiii/logarta_streamlit_portfolio.git
cd logarta_streamlit_portfolio

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

---

## ⚙️ Configuration & Placeholders to Customize

All key details are centralized at the top of [`app.py`](app.py):

| Variable | Current Value | Description |
|---|---|---|
| `DEFAULT_GITHUB_USERNAME` | `"milkuiii"` | Target GitHub username for live repository integration. |
| `STUDENT_NAME` | `"Sophia Gabrielle Logarta"` | Student's full name. |
| `STUDENT_SECTION` | `"CSIT349 - Section A1 / CSIT-3B"` | Class / course section code. Adjust to your specific class code if needed. |
| `STUDENT_PROGRAM` | `"Bachelor of Science in Computer Science (BSCS)"` | Degree program. |
| `STUDENT_YEAR` | `"2nd Year Undergraduate"` | Academic year level. |
| `STUDENT_SCHOOL` | `"Cebu Institute of Technology - University (CIT-U)"` | Current college/university. |

---

## ⚠️ Notes & Limitations

- **Contact Form Backend:** The contact form processes, validates, and records submissions in `st.session_state` for the duration of the user session. It does not send messages to external mail servers or store them in a persistent external database.
- **GitHub API Rate Limits:** Public unauthenticated GitHub API requests allow up to 60 requests per hour. Caching (`st.cache_data` with a 10-minute TTL) is active to conserve request limits.
