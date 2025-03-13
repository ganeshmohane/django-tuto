import streamlit as st
import requests

st.title("🎓 Student Placement Predictor")

cgpa = st.slider("CGPA (out of 10)", 0.0, 10.0, 7.5)
projects = st.slider("Number of Technical Projects", 0, 10, 2)
certifications = st.slider("Relevant Certifications", 0, 5, 2)
soft_skills = st.slider("Soft Skills (1-5)", 1, 5, 3)
linkedin_connections = st.slider("LinkedIn Connections", 0, 1000, 250)
hackathons = st.slider("Hackathons Attended", 0, 5, 1)
interview_attempts = st.slider("Interview Attempts", 0, 10, 3)

if st.button("Predict Placement"):
    data = {
        "cgpa": cgpa,
        "projects": projects,
        "certifications": certifications,
        "soft_skills": soft_skills,
        "linkedin_connections": linkedin_connections,
        "hackathons": hackathons,
        "interview_attempts": interview_attempts
    }
    response = requests.post("http://127.0.0.1:8000/api/predict/", json=data)
    result = response.json()["message"]
    
    st.success(f"Prediction: {result}")
