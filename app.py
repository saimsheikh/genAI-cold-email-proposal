import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from pipeline import clean_text, write_mail, extract_jobs
from db import DB

def create_streamlit_app(clean_text):
    st.title("📧 Cold Mail Generator")
    
    # Sidebar for additional info
    st.sidebar.header("About this App")
    st.sidebar.markdown("""
    This app helps you generate cold emails based on job descriptions.
    It works best with comprehensive job postings from major platforms.
    """)
    
    st.sidebar.markdown("[GitHub Repository](https://github.com/saimsheikh/genAI-cold-email-proposal) :star:")  # Replace with your GitHub link

    # Main input area
    st.markdown("""
    **Instructions:** 
    - Enter a job URL from a reputable platform.
    - Ensure the job description is detailed for best results.
    """)

    url_input = st.text_input("Enter a URL:", value="")
    submit_button = st.button("Generate Email")

    if submit_button:
        with st.spinner("Fetching job details..."):
            try:
                loader = WebBaseLoader([url_input])
                page_content = loader.load().pop().page_content
                
                # # Check for a valid job description
                # if "job title" not in page_content.lower():  # Example check
                #     st.error("Job description seems invalid. Please check the URL.")
                #     return

                data = clean_text(page_content)

                st.spinner("Extracting job details...")
                db.load_portfolio()
                jobs = extract_jobs(data)

                if not jobs:
                    st.warning("No jobs found in the provided description.")
                    return

                st.spinner("Generating emails...")
                for job in jobs:
                    skills = job.get('skills', [])
                    links = db.query_links(skills)
                    email = write_mail(job, links)
                    st.code(email, language='markdown')

            except Exception as e:
                st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    db = DB()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(clean_text)
