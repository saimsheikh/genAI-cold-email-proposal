

# Cold Mail Generator 📧

## Overview

The Cold Mail Generator is a web application that helps users generate personalized cold emails based on job descriptions extracted from URLs. Utilizing the Groq API with Meta Llama 3 (70B), this app leverages advanced language processing to craft effective outreach emails.

## Features

- **Job Description Extraction**: Fetches job descriptions from provided URLs.
- **Email Generation**: Creates tailored cold emails based on extracted job details.
- **Skill Matching**: Suggests relevant skills and resources for each job.

## Technologies Used

- **Streamlit**: Framework for building the web application.
- **Groq API**: Used for processing text with the Meta Llama 3 (70B) model.
- **Chroma DB**: Database for storing and querying job-related data.
- **LangChain**: Document loaders for fetching web content.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/saimsheikh/genAI-cold-email-proposal
   cd genAI-cold-email-proposal
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (if necessary for API keys or database connection).

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

3. Enter a URL of a job description from a reputable platform and click "Generate Email".

4. Review the generated emails based on the job details.

## Note

This tool works best with professional job descriptions that are comprehensive and detailed. Ensure the job posting includes essential information for optimal results.

## Contributing

Feel free to contribute to the project! You can submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for creating an easy-to-use web framework.
- [Meta Llama](https://huggingface.co/models?search=Llama) for powerful language processing capabilities.
- [Chroma DB](https://chroma.com/) for efficient data handling.

## GitHub

If you find this project useful, please give it a star on GitHub!

[GitHub Repository](https://github.com/saimsheikh/genAI-cold-email-proposal)

---

Feel free to customize the README further, especially the sections on installation and usage, to fit your project's specific needs. You can also add any additional sections you think would be helpful!