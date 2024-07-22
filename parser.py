import re
import spacy
from PyPDF2 import PdfReader

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "N/A"

def extract_email(text):
    email = re.findall(r'\S+@\S+', text)
    return email[0] if email else "N/A"

def extract_phone_number(text):
    phone = re.findall(r'\b\d{10}\b', text)
    return phone[0] if phone else "N/A"

def extract_github(text):
    github = re.findall(r'github\.com/[a-zA-Z0-9_-]+', text)
    return github[0] if github else "N/A"

def extract_summary(text):
    # Simple heuristic for demo purposes
    return text[:500]

def extract_projects(text):
    projects = re.findall(r'PROJECTS\n(.*?)\n\n', text, re.DOTALL)
    return projects[0] if projects else "N/A"

def extract_education(text):
    education = re.findall(r'EDUCATION\n(.*?)\n\n', text, re.DOTALL)
    return education[0] if education else "N/A"

def extract_certifications(text):
    certifications = re.findall(r'CERTIFICATIONS\n(.*?)\n\n', text, re.DOTALL)
    return certifications[0] if certifications else "N/A"

def extract_skills(text):
    skills = re.findall(r'SKILLS\n(.*?)\n\n', text, re.DOTALL)
    return skills[0] if skills else "N/A"

def parse_resume_file(file_path):
    text = extract_text_from_pdf(file_path)
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone Number": extract_phone_number(text),
        "GitHub": extract_github(text),
        "Summary": extract_summary(text),
        "Projects": extract_projects(text),
        "Education": extract_education(text),
        "Certifications": extract_certifications(text),
        "Skills": extract_skills(text),
    }

