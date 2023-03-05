import streamlit as st
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
import random
from streamlit_extras.switch_page_button import switch_page
import pdfkit
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import pyrebase
import os

st.set_page_config(page_title="19th Street | Dashboard", page_icon="⓵⓽", initial_sidebar_state="collapsed", layout="wide")

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

                div[data-testid="stSidebarNav"] {
                height: 0%;
                position: fixed;
                }



                .css-13e20ss{
                visibility: hidden;
                height: 0%;
                position: fixed;
                }

                div[class="stException"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }

              </style>
              """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



firebaseconfig = {
            "apiKey": "AIzaSyDCHY-GB5WCd0V6o4psrasOYZL_F7xcODM",
            "authDomain": "nineteenth-street.firebaseapp.com",
            "projectId": "nineteenth-street",
            "storageBucket": "nineteenth-street.appspot.com",
            "messagingSenderId": "964724806859",
            "appId": "1:964724806859:web:010841fc337f30b50cb74e",
            "measurementId": "G-N3TMC7M1WT",
            "databaseURL": "https://nineteenth-street-default-rtdb.firebaseio.com"
        }

firebase = pyrebase.initialize_app(firebaseconfig)
db = firebase.database()
user = st.session_state['user']






SavedResults = db.child("users").child(str(user["localId"])).child("Jobs").get().val()
unique_links = {}
for key, value in SavedResults.items():
    link = value['Link']
    if link not in unique_links:
        unique_links[link] = value

my_dict = unique_links
colresult1, colresult2, colresult3 = st.columns([0.25,1,0.25])
with colresult1:
    st.write("")
with colresult2:
    for key, value in my_dict.items():
        # st.write(key)
        # st.write(value)
        company_name = value['Company Name']
        Full_Description = value['Full Description']
        Link = value['Link']
        Location = value['Location']
        Short_Summary = value['Short Summary']
        Skills = value['Skills']
        Title = value['Title']

        st.markdown(
            f"<a href='{Link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{Title}→ </h4></a>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{company_name}</h6>",
            unsafe_allow_html=True)
        with st.expander(f"{Location}"):
            st.markdown(f"[Apply]({Link})")
            st.write(f"{Short_Summary}")

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                container_2 = st.empty()
                button_A = container_2.button('Generate Cover Letter', key=f"{Link}+{Title}+{Short_Summary}")
                if button_A:
                    container_2.empty()
                    button_B = container_2.button('Generating... Please wait.',
                                                  key=f"{Link}+{Title}+{Short_Summary}+Generating", disabled=True)
                    responseJob = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system",
                             "content": "You are an AI Assistant that summarizes job postings in less than a paragraph."},
                            {"role": "user",
                             "content": f"The following is a job posting I want you to summarize \n\n{Full_Description}\n\n"}])

                    jobSummary = responseJob["choices"][0]["message"]["content"]
                    CoverLetterResponse = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system",
                             "content": "You are an AI Assistant that writes highly customized cover letters from a first-person point of view. I have a cover letter format for you:\n\nFirst paragraph: Write about why the candidate is applying to this job. give one of the candidate's skills and relate it to the job requirements. Then give another skill of the job candidate and relate it to the job requirements. \n\nSecond Paragraph: Pick candidate's strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nThird Paragraph:  Pick candidate's second strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nFourth Paragraph: Conclude with how the candidate is excited to be able to contribute to the job and the company and grow more in a very mature way. "},
                            {"role": "user",
                             "content": f"Here's the job description:\n{jobSummary}\n\nHere's the resume data content:\n\n {st.session_state['resumeContent']}"}])
                    cover_letter_file = CoverLetterResponse["choices"][0]["message"]["content"]
                    st.download_button('Download Cover Letter', cover_letter_file)

            with col2:
                st.write("")

            with col3:
                st.write("")

        st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)
with colresult3:
    st.write("")