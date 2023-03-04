import streamlit as st
import os
import openai
from streamlit_extras.switch_page_button import switch_page
import PyPDF2

st.set_page_config(page_title="19th Street | Resume Builder", page_icon="⓵⓽", layout="wide")

hide_menu_style = """
         <style>
         #MainMenu {visibility: hidden;}
         .css-j7qwjs {visibility: hidden;}
         footer {visibility: hidden;}
         </style>
         """
st.markdown(hide_menu_style, unsafe_allow_html=True)
hide_streamlit_style = """
              <style>
              div[class='css-4z1n4l ehezqtx5']{
                background: rgba(0, 0, 0, 0.3);
                color: #fff;
                border-radius: 10px;
                backdrop-filter: blur(10px);
                height: 40px;
                max-width: 200px;
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 50%;
              }



              </style>
              """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

col1, col2, col3, col4, col5 = st.columns([1, 2, 0.1, 2, 1])

with col1:
    st.write("")

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    ResumeToCorrect = st.file_uploader(
        ''
    )

    col11, col22, col33 = st.columns([1, 1.75, 1])
    with col11:
        st.write("")
    with col22:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        if st.button("Start with your old resume →", key="Old Resume Begin Button"):
            pdfReader = PyPDF2.PdfReader(ResumeToCorrect)
            txtFile = open('sample.txt', 'w')
            num_pages = len(pdfReader.pages)
            for page_num in range(num_pages):
                pageObj = pdfReader.pages[page_num]
                txtFile.write(pageObj.extract_text())
                ResumeToCorrectContent = pageObj.extract_text()

            responseExperiences = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": """
                     You are an AI Assistant that is able to recognize the Experiences section of a resume when given the data of a resume. 
                     Your response is in the following format:
                     1a. Experience 1 name and company name (put semicolon at end)
                     2a. Experience 2 name and company name (put semicolon at end)
                     3a. Experience 3 name and company name (put semicolon at end)
                     4a. Experience 4 name and company name (put semicolon at end)
                     
                     1b. Experience 1 Description (put semicolon at end)
                     2b. Experience 2 Description (put semicolon at end)
                     3b. Experience 3 Description (put semicolon at end)
                     4b. Experience 4 Description (put semicolon at end)
                     
                     """},
                    {"role": "user",
                     "content": f"Here's the resume:\n{ResumeToCorrectContent}"}])
            st.session_state['OldExperiences'] = responseExperiences["choices"][0]["message"]["content"]

            responseProjects = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": """
                     You are an AI Assistant that is able to recognize the Projects section of a resume when given the data of a resume. 
                     
                     Your response is in the following format:
                     1a. Project 1 name (put semicolon at end)
                     2a. Project 2 name (put semicolon at end)
                     3a. Project 3 name (put semicolon at end)
                     4a. Project 4 name (put semicolon at end)
                     
                     1b. Project 1 Description (put semicolon at end)
                     2b. Project 2 Description (put semicolon at end)
                     3b. Project 3 Description (put semicolon at end)
                     4b. Project 4 Description (put semicolon at end)
                                          """},
                    {"role": "user",
                     "content": f"Here's the resume:\n{ResumeToCorrectContent}"}])
            st.session_state['OldProjects'] = responseProjects["choices"][0]["message"]["content"]





            switch_page("resumebuilder1")

    with col33:
        st.write("")

with col3:
    st.markdown("<hr style = 'width:0px; border-left: 2px solid grey; height: 300px;'>", unsafe_allow_html=True)
with col4:
    st.write("")
    st.write("")
    st.write("")
    CandidateName = st.text_input(
        'Name',
        placeholder='Name ',
        key='Name'
    )
    st.session_state['CandidateName'] = CandidateName

    CandidatePhone = st.text_input(
        'Phone',
        placeholder='Phone Number',
        key='Phone'
    )
    st.session_state['CandidatePhone'] = CandidatePhone

    CandidateEmail = st.text_input(
        'Email',
        placeholder='Email ',
        key='Email'
    )
    st.session_state['CandidateEmail'] = CandidateEmail

    col111, col222, col333 = st.columns([1, 1, 1])

    with col111:
        st.write("")
    with col222:
        st.subheader("")
        if st.button("Go Manually →", key="Go Manually"):
            switch_page("resumebuilder")
    with col333:
        st.write("")

with col5:
    st.write("")