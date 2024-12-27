# Job Finder Application

A Django-based web application that allows users to upload their resumes, scan them for key skills, and perform a web search to find relevant job listings matching their profile. The application leverages web scraping techniques and job board APIs to display tailored job opportunities.

---

## Features
- **Resume Upload**: Users can upload their resumes in PDF format.
- **Resume Parsing**: Extracts key skills and information from the uploaded resume.
- **Job Search**: Performs a web search or integrates with Indeed API to fetch relevant job postings.
- **Job List Display**: Presents job opportunities.

---

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML
- **Database**: No database used for this application. The file was stored in temporary buffer. Althogh, SQLite is included since it is the default Django database
- **APIs**:  Indeed API.
| Library           | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `Django`          | Backend framework for building the web application.                   |
| `requests`        | To make HTTP requests to APIs like Indeed API.                         |
| `json`            | To parse API responses and work with JSON data.                       |
| `nltk`            | For natural language processing, tokenization, and stopword removal.  |
| `PyPDF2`          | To parse and extract text from PDF resumes.                           |
| `io`              | To handle file streams (e.g., uploaded files).  
---

## Installation
Install Dependencies:
pip install django requests nltk PyPDF2
Download NLTK Resources: Run the following commands to download required NLTK data:

python:
import nltk
nltk.download('punkt')
nltk.download('stopwords')

Run Migrations:
python manage.py makemigrations
python manage.py migrate

Start the Development Server:
python manage.py runserver

Access the Application: 
Open your browser and navigate to http://127.0.0.1:8000.

### Prerequisites
- Python (version 3.8 or above)
- Pip (Python package manager)
- Django (version 4.0 or above)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/job-finder.git
   cd job-finder
