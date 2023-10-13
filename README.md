<h1 align="center">📓10x-Academic Buddy</h1>

<p align="center">
Streamlit web application that uses AI to generate comprehensive notes and question-answer pairs from PDFs.
</p>

<p align="center">
  <img src="note_taking.jpg" alt="Dashboard Screenshot" width="80%">
</p>

---

## Table of Contents

- [Application Features](#application-features)
- [Technology Used](#technology-used)
- [Project Installation and Setup](#project-installation-and-setup)
- [How to Use the Application](#how-to-use-the-application)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
  
---

## Application Features

- **Text Extraction from PDF:** The application is capable of extracting text data from uploaded PDF files.

- **Note Generation with AI:** Utilizing the power of OpenAI, it creates comprehensive and detailed notes, breaking down any lengthy document into understandable portions.

- **Question-Answer Generation:** Besides notes, the application can also generate potential question-answer pairs from the content being fed. This is a handy feature for students using this application to study.

- **Interactive Web Interface:** The Streamlit framework provides an interactive configuration for users to smoothly operate the application.

---

## Technology Used

- Streamlit
- OpenAI
- Python3
- PyPDF2
- pdfreader

---

## Project Installation and Setup

Start by cloning this repository to your local machine using:

```bash
git clone https://github.com/liticx/📓10x-Academic Buddy.git
```

Make sure you meet the prerequisites before moving to the installation. You must have Python 3.7 or higher installed on your machine, and 'pip' must be configured.

Now, install the dependencies required for the project using the following command:

```bash
pip install streamlit numpy PyPDF2 pdfreader requests
```

---

## How to Use the Application

Navigate to the project directory, and then type `streamlit run app.py` to launch the application in your web browser.

Use the PDF upload button to upload your chosen PDF file. Then, hit 'Generate Notes' to allow the AI to process the text and generate notes, or select 'Generate Questions & Answers' to generate a list of potential question-and-answer pairs.

---

## Contribution Guidelines

If you're interested in contributing to this project, I'm glad to have you! Please open an issue or submit a pull request to discuss potential changes/additions.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 
  

---