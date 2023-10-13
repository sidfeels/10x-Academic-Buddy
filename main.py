import os
import streamlit as st
import requests
from PyPDF2 import PdfFileReader
from io import BytesIO


# Set your Nova AI API key
nova_api_key = st.secrets["nova"]["api_key"]

from pdfreader import SimplePDFViewer

def extract_text_from_pdf(file):
    viewer = SimplePDFViewer(file)
    viewer.navigate(1)
    viewer.render()
    text = " ".join(viewer.canvas.strings)
    return text

def summarize_text_with_nova_ai(text):
    
    system_prompt = (
        "Dear AI Model, your task is to create detailed notes from the provided text:"
        
        "1. Thoroughly read the text. If it's long, break it down into manageable sections."
        "2. Identify the structure for the notes, incorporate key details in fitting sections."
        "3. Ensure the notes align with the original text's order of ideas, make it engaging by using emojis at start of every topic, headings, etc."
        "4. Re-read the text with the structure in mind to optimize the notes."
        

        "These notes should be comprehensive to function as study guides suited for undergraduate level, BTech engineering, or high-level Biology content in atleast 500 words"

        "Prioritize enhancing readability, utilizing tools such as bolding, italicising, underlining. Lastly, The notes should cover all the critical details from the text for the best comprehension of content."
    )
    return get_ai_response(text, system_prompt)

def generate_questions_with_nova_ai(text):
    system_prompt = ("Dear AI model, create a set of potential question and answer pairs based on the provided text: "
                     "Ensure that the questions are relevant to the content and its difficulty level aligns with BTech engineering or MBBS studies also dont forget to provide the answer for the question."
                    "The format of question and answer should be like" 
                    "Que: and then answer on the next line Ans: "
    
    )
    return get_ai_response(text, system_prompt)


def get_ai_response(text, system_prompt):

    nova_api_url = 'https://api.naga.ac/v1/chat/completions'
    data = {
        "model": "gpt-3.5-turbo", #suggested model for faster response
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": text,
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {nova_api_key}"
    }
    response = requests.post(nova_api_url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data:
            assistant_message = response_data['choices'][0]['message']
            if 'content' in assistant_message:
                completion_message = assistant_message['content']
                return completion_message

    return "Could not generate summary."  # Return a message if no summary is available

# Streamlit web app
def main():

    st.set_page_config(page_title='📓10x-Academic Buddy', layout='wide', initial_sidebar_state = 'auto')

    # Create a two-column layout
    col1, col2 = st.columns([1, 5])

    # Display the image in the first column
    col1.image('note taking.jpg', width = 160)  
    # replace 'note taking.jpg' with the path to your image file.

    # Display the title and description in the second column
    with col2:
        st.title('📓10x-Academic Buddy')
        st.write('_Upload your Academic Notes and get comprehensive, ordered notes, and question and answers generated out of it._')
        st.write('Made with <3 by *[Siddhant Panpatil](https://github.com/liticx/10x-Academic-Buddy)*')
    uploaded_file = st.sidebar.file_uploader("### **Hello there, Human :)**", type="pdf")

    


    chunks = []
    if uploaded_file is not None:
        if st.sidebar.button("Generate Notes"):  # moved to sidebar
            with st.spinner("Extracting Text from the Pdf..."):
                pdf_text = extract_text_from_pdf(BytesIO(uploaded_file.read()))
                words = pdf_text.split()
                chunks = [" ".join(words[i:i+5000]) for i in range(0, len(words), 5000)]
            st.sidebar.success("Text Extraction Complete!")

            if len(chunks) > 0:
                with st.spinner('AI is preparing your Notes...'):
                    summaries = [summarize_text_with_nova_ai(chunk) for chunk in chunks if summarize_text_with_nova_ai(chunk) is not None]
                    formatted_summary = "\n\n".join(summaries)

                st.sidebar.success("Summary generation complete!")
                st.header('Generated Notes:')
                st.write(formatted_summary)

        if st.sidebar.button("Generate Questions & Answers"):
            with st.spinner("AI is preparing your Question & Answers..."):
                pdf_text = extract_text_from_pdf(BytesIO(uploaded_file.read()))
                words = pdf_text.split()
                chunks = [" ".join(words[i:i+5000]) for i in range(0, len(words), 5000)]
            st.sidebar.success("Text Extraction Complete!")

            if len(chunks) > 0:
                with st.spinner('AI is preparing the Questions & Answers...'):
                    qna_pairs = [generate_questions_with_nova_ai(chunk) for chunk in chunks if generate_questions_with_nova_ai(chunk) is not None]
                    formatted_questions = "\n\n".join(qna_pairs)
                st.sidebar.success("Questions & Answers generation complete!")
                st.header('Generated Questions & Answers:')
                st.write(formatted_questions)

if __name__ == '__main__':
    main()