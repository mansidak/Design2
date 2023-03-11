import time

import streamlit as st
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
import random
from streamlit_extras.switch_page_button import switch_page
import pdfkit
from streamlit_option_menu import option_menu
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import pyrebase
from st_btn_select import st_btn_select
import extra_streamlit_components as stx
import datetime
import requests
import os

st.set_page_config(page_title="19th Street | Dashboard", page_icon="⓵⓽", initial_sidebar_state="collapsed", layout="wide")

@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
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

hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
        ul.streamlit-expander {
                border: 0 None !important;
                }
    </style>
    '''

st.markdown(hide_img_fs, unsafe_allow_html=True)

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


if __name__ == "__main__":
    cookies = cookie_manager.get_all()
    # st.write(cookies)
    def main(user: object):
        coldash1, coldash2, coldash3 = st.columns([1, 2, 1])
        with coldash1:
            st.write("")
        with coldash2:
            selected2 = option_menu(None, ["Home", "Search", "Build", 'Dashboard'],
                                    icons=['house', 'search', "file-earmark-font", 'stack'],
                                    menu_icon="cast", default_index=1, orientation="horizontal",
                                    styles={
                                        "container": {"padding": "0!important", "background-color": "#0f0f0f"},
                                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px",
                                                     "--hover-color": "#0f0f0f", "color": "white",
                                                     "background-color": "#0f0f0f"},
                                        "nav-link-selected": {"font-weight": "bold", "background-color": "#0f0f0f",
                                                              "color": "#F63366"},
                                    })

            if selected2 == "Home":
                switch_page("streamlit_app")
            elif selected2 == "Dashboard":
                switch_page("dashboard")
            elif selected2 == "Build":
                switch_page("PreResumeBuilder")

        with coldash3:
            st.write("")

        st.markdown("""
                                <style>


                                .css-ocqkz7.e1tzin5v4{
                                margin-top:-30px;
                                }
                                
                                .row-widget.stButton{
                                margin-top: 30px;
                                }


                                .css-1uhah0b.e8zbici2{
                                z-index:0;
                                }
                                header[data-testid="stHeader"] {
                                position: relative;
                                }
                                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(8) {
                                    margin-top:-90px;
                                    margin-left:-90px;
                                    min-width:100%;
                                    position:fixed;
                                    z-index:1;
                                    }

                                  .dark{
                                        background-color: #eeeeee;
                                        color:black;
                                        border-color: black;
                                        }

                                   .dark:hover{
                                        background-color: #eeeeee;
                                        color: #F63366;
                                        border-color: #F63366;
                                        }

                                    .button.dark {
                                      background-color: #4CAF50; /* Green */
                                      border: none;
                                      color: white;
                                      padding: 15px 32px;
                                      text-align: center;
                                      text-decoration: none;
                                      display: inline-block;
                                      font-size: 16px;
                                    }
                                </style>
                                """, unsafe_allow_html=True)
        st.markdown("""

                <style>
                .stAlert{
                height:0px;
                visibility:hidden
                }
                </style>""", unsafe_allow_html=True)
        AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
        firebase = pyrebase.initialize_app(firebaseconfig)
        db = firebase.database()
        localId = AccountInfo["localId"]
        set_code(code=user['refreshToken'])
        cookie_manager.set("userCookie", user['refreshToken'], expires_at=datetime.datetime(year=2024, month=2, day=2))


        # unique_results = set(st.session_state['FinalResults'])

        unique_results = set(db.child("users").child(str(localId)).child("Archive").child("FinalResults").get().val())
        with st.sidebar:

            st.subheader("")
            st.subheader("")

            options = st.multiselect('Filter by location',
                                     set([item[5] for item in st.session_state['FinalResults']]), None,
                                     key="option1")
            options2 = st.multiselect('Filter by your strongest skills',
                                      set([item[6].replace('-', '') for item in st.session_state['FinalResults']]),
                                      None, key="option2")
            html_string = "<ul>"
            for list in unique_results:
                link = list[0]
                title = list[1]
                companyName = list[2]
                shortSummary = list[3]
                fullDescription = list[4]
                location = list[5]
                skills = list[6]
                html_string += "<li><a href='" + link + "'>" + title + " at " + companyName + "</a><ul><li>" + shortSummary + "</li></ul></li>"
            html_string += "</ul>"

            # generate the pdf
            PDFFile = pdfkit.from_string(html_string, "output.pdf")

            with open("output.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            # st.download_button(label='Download PDF', data= PDFFile)

            st.download_button(label="Download All Jobs",
                               data=PDFbyte,
                               file_name="test.pdf",
                               key='downloadingjobspdf',
                               mime='application/octet-stream')

        colresult1, colresult2, colresult3 = st.columns([0.25, 1, 0.25])
        with colresult1:
            st.write("")
        with colresult2:
            col1, col2, col3 = st.columns([2, 1, 2])

            with col1:
                st.write("")

            with col2:
                image = Image.open('PenManLogo.png')
                st.image(image)

            with col3:
                st.write("")

            # if 'Name' not in st.session_state:
            #     switch_page("app")
            st.markdown(
                f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{st.session_state['Name']}</h2>",
                unsafe_allow_html=True)
            st.markdown(
                f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Tip: You can ask 19th Street to write custom cover letters for each job.</h6>",
                unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            # unique_results = set(st.session_state['FinalResults'])

            for element in unique_results:
                if element[5] in options and element[6].replace('-', '') in options2:
                    link = element[0]
                    title = element[1]
                    companyName = element[2]
                    shortSummary = element[3]
                    fullDescription = element[4]
                    location = element[5]
                    skills = element[6]

                    st.markdown(
                        f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
                        unsafe_allow_html=True)

                    with st.expander(f"{location}"):
                        st.markdown(f"[Apply]({link})")
                        st.write(f"{shortSummary}")

                        col1, col2, col3 = st.columns([1, 1, 1])

                        with col1:
                            container_2 = st.empty()
                            button_A = container_2.button('Generate Cover Letter',
                                                          key=f"{link}+{title}+{shortSummary}")
                            if button_A:
                                container_2.empty()
                                button_B = container_2.button('Generating... Please wait.',
                                                              key=f"{link}+{title}+{shortSummary}+Generating",
                                                              disabled=True)
                                responseJob = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system",
                                         "content": "You are an AI Assistant that summarizes job postings in less than a paragraph."},
                                        {"role": "user",
                                         "content": f"The following is a job posting I want you to summarize \n\n{fullDescription}\n\n"}])

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
                            if st.button("Save", key=f"{link}+{title}+{shortSummary}+{companyName}"):
                                firebase = pyrebase.initialize_app(firebaseconfig)
                                db = firebase.database()
                                # user = st.session_state['user']
                                data = {
                                    "Link": str(link),
                                    "Title": str(title),
                                    "Company Name": str(companyName),
                                    "Short Summary": str(shortSummary),
                                    "Full Description": str(fullDescription),
                                    "Location": str(location),
                                    "Skills": str(skills)
                                }
                                results = db.child("users").child(str(localId)).child("Jobs").push(data)
                                st.write("Saved!")

                        with col3:
                            st.write("")

                    st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

                elif not options and element[6].replace('-', '') in options2:
                    link = element[0]
                    title = element[1]
                    companyName = element[2]
                    shortSummary = element[3]
                    fullDescription = element[4]
                    location = element[5]
                    skills = element[6]

                    st.markdown(
                        f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
                        unsafe_allow_html=True)

                    with st.expander(f"{location}"):
                        st.markdown(f"[Apply]({link})")
                        st.write(f"{shortSummary}")

                        col1, col2, col3 = st.columns([1, 1, 1])

                        with col1:
                            container_2 = st.empty()
                            button_A = container_2.button('Generate Cover Letter',
                                                          key=f"{link}+{title}+{shortSummary}")
                            if button_A:
                                container_2.empty()
                                button_B = container_2.button('Generating... Please wait.',
                                                              key=f"{link}+{title}+{shortSummary}+Generating",
                                                              disabled=True)
                                responseJob = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system",
                                         "content": "You are an AI Assistant that summarizes job postings in less than a paragraph."},
                                        {"role": "user",
                                         "content": f"The following is a job posting I want you to summarize \n\n{fullDescription}\n\n"}])

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
                            if st.button("Save", key=f"{link}+{title}+{shortSummary}+{companyName}"):
                                firebase = pyrebase.initialize_app(firebaseconfig)
                                db = firebase.database()
                                # user = st.session_state['user']
                                data = {
                                    "Link": str(link),
                                    "Title": str(title),
                                    "Company Name": str(companyName),
                                    "Short Summary": str(shortSummary),
                                    "Full Description": str(fullDescription),
                                    "Location": str(location),
                                    "Skills": str(skills)
                                }
                                results = db.child("users").child(str(localId)).child("Jobs").push(data)
                                st.write("Saved!")

                        with col3:
                            st.write("")

                    st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

                elif not options2 and element[5] in options:
                    link = element[0]
                    title = element[1]
                    companyName = element[2]
                    shortSummary = element[3]
                    fullDescription = element[4]
                    location = element[5]
                    skills = element[6]

                    st.markdown(
                        f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
                        unsafe_allow_html=True)

                    with st.expander(f"{location}"):
                        st.markdown(f"[Apply]({link})")
                        st.write(f"{shortSummary}")

                        col1, col2, col3 = st.columns([1, 1, 1])

                        with col1:
                            container_2 = st.empty()
                            button_A = container_2.button('Generate Cover Letter',
                                                          key=f"{link}+{title}+{shortSummary}")
                            if button_A:
                                container_2.empty()
                                button_B = container_2.button('Generating... Please wait.',
                                                              key=f"{link}+{title}+{shortSummary}+Generating",
                                                              disabled=True)
                                responseJob = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system",
                                         "content": "You are an AI Assistant that summarizes job postings in less than a paragraph."},
                                        {"role": "user",
                                         "content": f"The following is a job posting I want you to summarize \n\n{fullDescription}\n\n"}])

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
                            if st.button("Save", key=f"{link}+{title}+{shortSummary}+{companyName}"):
                                firebase = pyrebase.initialize_app(firebaseconfig)
                                db = firebase.database()
                                # user = st.session_state['user']
                                data = {
                                    "Link": str(link),
                                    "Title": str(title),
                                    "Company Name": str(companyName),
                                    "Short Summary": str(shortSummary),
                                    "Full Description": str(fullDescription),
                                    "Location": str(location),
                                    "Skills": str(skills)
                                }
                                results = db.child("users").child(str(localId)).child("Jobs").push(data)
                                st.write("Saved!")

                        with col3:
                            st.write("")

                    st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)





                elif not options and not options2:
                    link = element[0]
                    title = element[1]
                    companyName = element[2]
                    shortSummary = element[3]
                    fullDescription = element[4]
                    location = element[5]
                    skills = element[6]
                    col1mark, col2mark = st.columns([1, 0.1])
                    with col1mark:
                        st.markdown(
                            f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
                            unsafe_allow_html=True)
                    with col2mark:
                        Save = st.empty()
                        if Save.button("Save", key=f"{link}+{title}+{shortSummary}+{companyName}"):
                            firebase = pyrebase.initialize_app(firebaseconfig)
                            db = firebase.database()
                            # user = st.session_state['user']
                            data = {
                                "Link": str(link),
                                "Title": str(title),
                                "Company Name": str(companyName),
                                "Short Summary": str(shortSummary),
                                "Full Description": str(fullDescription),
                                "Location": str(location),
                                "Skills": str(skills)
                            }
                            results = db.child("users").child(str(localId)).child("Jobs").push(data)
                            st.write("Saved!")
                            Save.empty()

                    with st.expander(f"{location}"):
                        st.markdown(f"[Apply]({link})")
                        st.write(f"{shortSummary}")

                        col1, col2, col3 = st.columns([1, 1, 1])

                        with col1:
                            container_2 = st.empty()
                            button_A = container_2.button('Generate Cover Letter',
                                                          key=f"{link}+{title}+{shortSummary}")
                            if button_A:
                                container_2.empty()
                                button_B = container_2.button('Generating... Please wait.',
                                                              key=f"{link}+{title}+{shortSummary}+Generating",
                                                              disabled=True)
                                responseJob = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system",
                                         "content": "You are an AI Assistant that summarizes job postings in less than a paragraph."},
                                        {"role": "user",
                                         "content": f"The following is a job posting I want you to summarize \n\n{fullDescription}\n\n"}])

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

            colconclusion1, colconclusion2 = st.columns([1, 1])
            with colconclusion1:

                html_string = "<ul>"
                for list in unique_results:
                    link = list[0]
                    title = list[1]
                    companyName = list[2]
                    shortSummary = list[3]
                    fullDescription = list[4]
                    location = list[5]
                    skills = list[6]
                    html_string += "<li><a href='" + link + "'>" + title + " at " + companyName + "</a><ul><li>" + shortSummary + "</li></ul></li>"
                html_string += "</ul>"

                # generate the pdf
                PDFFile = pdfkit.from_string(html_string, "output.pdf")

                with open("output.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                # st.download_button(label='Download PDF', data= PDFFile)

                st.download_button(label="Download All Jobs",
                                   data=PDFbyte,
                                   file_name="test.pdf",
                                   mime='application/octet-stream')
            with colconclusion2:
                if st.button("Not Satisfied? Run Again"):
                    switch_page("search")

        with colresult3:
            st.write("")

        # for job in unique_results:
        #     firebase = pyrebase.initialize_app(firebaseconfig)
        #     db = firebase.database()
        #     link = job[0]
        #     title = job[1]
        #     companyName = job[2]
        #     shortSummary = job[3]
        #     fullDescription = job[4]
        #     location = job[5]
        #     skills = job[6]
        #     data = {
        #         "Link": str(link),
        #         "Title": str(title),
        #         "Company Name": str(companyName),
        #         "Short Summary": str(shortSummary),
        #         "Full Description": str(fullDescription),
        #         "Location": str(location),
        #         "Skills": str(skills)
        #     }
        #     db.child("users").child(str(localId)).child("Archive").child("Archive1").push(data)



def set_code(code: str):
    st.experimental_set_query_params(code=code)


col1form, col2form, col3form = st.columns([0.25, 1, 0.25])
with col1form:
    st.write("")
with col2form:
    def login_form(auth):
        email = st.text_input(
            label="email", placeholder="fullname@gmail.com")
        password = st.text_input(
            label="password", placeholder="password", type="password")

        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['user'] = user
                st.experimental_rerun()
            except requests.HTTPError as exception:
                st.write(exception)
        if st.button("Forgot Password", key="forgotpassword"):
            auth.send_password_reset_email("email")


    def Signup_form(auth):
        email = st.text_input(
            label="email", placeholder="fullname@gmail.com")
        password = st.text_input(
            label="password", placeholder="password", type="password")

        if st.button("login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['user'] = user
                st.experimental_rerun()
            except requests.HTTPError as exception:
                st.write(exception)
        if st.button("Forgot Password", key="forgotpassword"):
            auth.send_password_reset_email("email")

with col3form:
    st.write("")


def logout():
    del st.session_state['user']
    st.experimental_set_query_params(code="/logout")


def get_user_token(auth, refreshToken: object):
    user = auth.get_account_info(refreshToken['idToken'])

    user = {
        "email": user['users'][0]['email'],
        "refreshToken": refreshToken['refreshToken'],
        "idToken": refreshToken['idToken']
    }

    st.session_state['user'] = user

    return user


def refresh_session_token(auth, code: str):
    try:
        return auth.refresh(code)
    except:
        return "fail to refresh"


firebase = pyrebase.initialize_app(firebaseconfig)

auth = firebase.auth()

# authentification
if "user" not in st.session_state:
    st.session_state['user'] = None

if st.session_state['user'] is None:
    try:
        # code = st.experimental_get_query_params()['code'][0]
        code = cookie_manager.get(cookie="userCookie")
        refreshToken = refresh_session_token(auth=auth, code=code)

        if refreshToken == 'fail to refresh':
            raise (ValueError)

        user = get_user_token(auth, refreshToken=refreshToken)

        main(user=user)
    except:
        st.title("Login")
        login_form(auth)

else:
    main(user=st.session_state['user'])