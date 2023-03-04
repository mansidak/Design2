import streamlit as st
st.set_page_config(page_title="19th Street | Resulsts", page_icon="⓵⓽", initial_sidebar_state="expanded", layout="wide")
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




unique_results = set(st.session_state['FinalResults'])
with st.sidebar:

    st.subheader("")
    st.subheader("")

    options = st.multiselect('Filter by location', set([item[5] for item in st.session_state['FinalResults']]), None, key="option1")
    options2 = st.multiselect('Filter by your strongest skills', set([item[6].replace('-', '') for item in st.session_state['FinalResults']]), None, key="option2")
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
                       key = 'downloadingjobspdf',
                       mime='application/octet-stream')


colresult1, colresult2, colresult3 = st.columns([0.25,1,0.25])
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

    if 'Name' not in st.session_state:
        switch_page("app")
    st.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{st.session_state['Name']}</h2>",
                unsafe_allow_html=True)
    st.markdown(
        f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Tip: You can ask 19th Street to write custom cover letters for each job.</h6>",
        unsafe_allow_html=True)

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
                    button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                    if button_A:
                        container_2.empty()
                        button_B = container_2.button('Generating... Please wait.',
                                                      key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
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
                    if st.button("Save to my account", key="Savetoaccount"):
                        firebase = pyrebase.initialize_app(firebaseconfig)
                        db = firebase.database()
                        user = st.session_state['user']
                        data = {
                            'str(f"{link}")' : {
                                "Link": str(link),
                                "Title": str(title),
                                "Company Name": str(companyName),
                                "Short Summary": str(shortSummary),
                                "Full Description": str(fullDescription),
                                "Location": str(location),
                                "Skills": str(skills)

                            }
                        }
                        results = db.child("users").child(str(user["localId"])).child("Jobs").set(data)
                        st.write(user["localId"])

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
                    button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                    if button_A:
                        container_2.empty()
                        button_B = container_2.button('Generating... Please wait.',
                                                      key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
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
                    # if st.button("Apply", key=f"{link}+{title}+Apply"):
                    #     js = f"window.open('{link}')"  # New tab or window

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
                    button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                    if button_A:
                        container_2.empty()
                        button_B = container_2.button('Generating... Please wait.',
                                                      key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
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
                    # if st.button("Apply", key=f"{link}+{title}+Apply"):
                    #     js = f"window.open('{link}')"  # New tab or window

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
                    button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                    if button_A:
                        container_2.empty()
                        button_B = container_2.button('Generating... Please wait.',
                                                      key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
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

                    # if st.button("Apply", key=f"{link}+{title}+Apply"):
                    #     js = f"window.open('{link}')"  # New tab or window

                with col3:
                    st.write("")

            st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)



    colconclusion1, colconclusion2 = st.columns([1,1])
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
            switch_page("betaa")

        data = {}
        for list in unique_results:
            data[list[0]] = {
                'title': list[1],
                'companyName': list[2],
                'shortSummary': list[3],
                'fullDescription': list[4],
                'location': list[5],
                'skills': list[6]
            }

        if st.button("Save to my account", key="Savetoaccount"):
            firebase = pyrebase.initialize_app(firebaseconfig)
            db = firebase.database()
            user = st.session_state['user']
            results = db.child("users").child(str(user["localId"])).child("Jobs").set(data)
            st.write(user["localId"])



with colresult3:
    st.write("")