# Job Finder Application

A Django-based web application that allows users to upload their resumes, scan them for key skills, and perform a web search to find relevant job listings matching their profile. The application leverages web scraping techniques and job board APIs to display tailored job opportunities.

---

## Features
- **Resume Upload**: Users can upload their resumes in PDF format.
- **Resume Parsing**: Extracts key skills and information from the uploaded resume using libraries like `PyPDF2` and `spaCy`.
- **Job Search**: Performs a web search or integrates with job board APIs (e.g., LinkedIn, Indeed, Google Jobs) to fetch relevant job postings.
- **Job List Display**: Presents job opportunities in a clean, user-friendly interface.

---

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for styling)
- **Database**: SQLite (default Django database)
- **APIs**: Optional integration with job APIs like LinkedIn API, Indeed API, or Google Jobs API.
- **Libraries**:
  - `PyPDF2` for parsing PDF resumes.
  - `spaCy` for extracting skills and text processing.
  - `BeautifulSoup` for web scraping (optional).
  - `Requests` for API calls.

---

## Installation

### Prerequisites
- Python (version 3.8 or above)
- Pip (Python package manager)
- Django (version 4.0 or above)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/job-finder.git
   cd job-finder
