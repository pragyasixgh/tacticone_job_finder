import requests
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from io import BytesIO
from PyPDF2 import PdfReader
from django.shortcuts import render
from .forms import ResumeForm

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from PDF and find skills
def extract_skills_from_pdf(file):
    # Extract text from PDF
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Tokenize and clean the text
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Sample skills list (you can extend this as needed)
    skills = [
    # Programming languages
    "python", "java", "javascript", "c", "c++", "c#", "ruby", "php", "swift", "kotlin", "r", "go", "perl", 
    "typescript", "matlab", "shell scripting", 

    # Web development
    "html", "css", "sass", "bootstrap", "react", "angular", "vue.js", "node.js", "express.js", "flask", 
    "web development", "wordpress", "graphql", 

    # Databases and related
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sqlite", "nosql", "database administration", 
    "data modeling", "hadoop", 

    # Data science and analytics
    "machine learning", "deep learning", "data analysis", "data visualization", "data mining", "data engineering", 
    "pandas", "numpy", "scikit-learn", "tensorflow", "keras", "pytorch", "matplotlib", "seaborn", "big data", 
    "statistics", 

    # Cloud platforms and DevOps
    "aws", "azure", "google cloud", "devops", "docker", "kubernetes", "jenkins", "terraform", "ansible", 
    "ci/cd pipelines", "cloud computing", 

    # Office and productivity tools
    "excel", "microsoft office", "powerpoint", "word", "google sheets", "outlook", "sharepoint", 

    # Cybersecurity
    "cybersecurity", "ethical hacking", "penetration testing", "network security", "cryptography", "firewalls", 
    "vulnerability assessment", 

    # Software development and testing
    "software development", "agile", "scrum", "jira", "git", "github", "bitbucket", "version control", 
    "unit testing", "integration testing", "selenium", 

    # Design and multimedia
    "ui/ux design", "adobe photoshop", "adobe illustrator", "figma", "adobe xd", "3d modeling", "autocad", 
    "blender", "premiere pro", "video editing", 

    # Networking and IT support
    "networking", "network administration", "it support", "troubleshooting", "linux", "windows server", 
    "active directory", "tcp/ip", "dns", "vpn", 

    # Other technical skills
    "blockchain", "cryptocurrency", "iot", "robotics", "arduino", "raspberry pi", "embedded systems", 

    # Soft skills and project management
    "project management", "leadership", "team collaboration", "time management", "problem-solving", 
    "critical thinking", "public speaking", "technical writing", "business analysis", 

    # Marketing and sales
    "digital marketing", "seo", "content writing", "social media marketing", "google analytics", 
    "email marketing", "salesforce", "crm", 

    # Specialized domains
    "biotechnology", "genomics", "financial analysis", "accounting", "supply chain management", 
    "human resources", "education technology", "game development", 
]
    # Find matching skills
    matched_skills = list(set(filtered_words).intersection(skills))
    return matched_skills

# Function to call the Indeed API for matching jobs
def fetch_matching_jobs(skills):
    if not skills:
        return []

    # Join skills to form a query string for the API search
    query = "+".join(skills)
    
    # Define the base URL and headers for the API request
    url = "https://indeed12.p.rapidapi.com/jobs/search"
    headers = {
        'x-rapidapi-key': "a272abf70cmshb16f65d5421a491p12536bjsneb5fafd5194f",
        'x-rapidapi-host': "indeed12.p.rapidapi.com"
    }

    # Query parameters
    querystring = {
    "query": query,                # The skill-based search query
    "location": "india",           # Search across all of India
    "page_id": "1",                # Start at the first page of results
    "locality": "in",              # Specify Indian locality
    "fromage": "30",               # Jobs posted within the last 30 days
    "radius": "0",                 # No radius restriction (entire India)
    "sort": "relevance",           # Sort results by relevance
}

    # Send GET request to the API
    response = requests.get(url, headers=headers, params=querystring)

    # Parse and return the job results from the response
    jobs = response.json()
    return jobs.get("results", [])
# Print parsed results for debugging
# View for handling the resume upload and job search
def job_list(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract skills from uploaded resume
            resume_file = request.FILES['resume']
            skills = extract_skills_from_pdf(resume_file)

            # Fetch matching jobs based on extracted skills
            jobs = fetch_matching_jobs(skills)

            return render(request, 'jobs/job_list.html', {'form': form, 'skills': skills, 'jobs': jobs})

    else:
        form = ResumeForm()

    return render(request, 'jobs/job_list.html', {'form': form})
