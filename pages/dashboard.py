import streamlit as st
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
from streamlit_option_menu import option_menu
import PyPDF2
import random
from streamlit_extras.switch_page_button import switch_page
import pdfkit
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
                                    menu_icon="cast", default_index=3, orientation="horizontal",
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
            elif selected2 == "Search":
                switch_page("search")
            elif selected2 == "Build":
                switch_page("PreResumeBuilder")

        with coldash3:
            st.write("")
        st.markdown("""
                    <style>

                    .css-1uhah0b.e8zbici2{
                    z-index:0;
                    }

                    header[data-testid="stHeader"] {
                    position: relative;
                    }

                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(6) {
                        margin-top:-90px;
                        min-width:100%;
                        margin-left:-90px;
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

        st.markdown(
            f"<center> <h1 style='font-family: Sans-Serif; font-weight:normal; color: white'><span style='background: -webkit-gradient(linear,left top,right bottom,from(#34C800), to(#FE0000));-webkit-background-clip:text;-webkit-text-fill-color: transparent;'>19th street</span> Dashboard</h1>",
            unsafe_allow_html=True)

        colLogin1, colLogin2, colLogin3 = st.columns([2, 1, 2])
        with colLogin2:
            st.write(f"You're logged in as {st.session_state['user']['email']}")


        AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
        firebase = pyrebase.initialize_app(firebaseconfig)
        db = firebase.database()
        localId = AccountInfo["localId"]
        set_code(code=user['refreshToken'])
        cookie_manager.set("userCookie", user['refreshToken'], expires_at=datetime.datetime(year=2024, month=2, day=2))
        FirebaseResumeContent = db.child("users").child(str(localId)).child("Resume").get().val()
        st.session_state['resumeContent'] = FirebaseResumeContent
        colResume1, colResume2, colResume3 = st.columns([0.8, 1, 0.8])
        with colResume1:
            st.write("")
        with colResume2:

            if FirebaseResumeContent:
                st.markdown(
                    f"<h6 style='text-align:center; font-weight:lighter;color:black'>Resume on file:<span style='color: green'>&nbsp &check;</span> </h6>",
                    unsafe_allow_html=True)
                colResumeSub1, colResumeSub2, colResumeSub3, colResumeSub4 = st.columns([0.8, 1.5, 1.3, 0.55])
                with colResumeSub2:
                    if st.button("Upload new resume"):
                        db.child("users").child(str(localId)).child("Resume").remove()
                        del st.session_state['resumeContent']
                        st.experimental_rerun()
                with colResumeSub3:
                    if st.button("Run New Search"):
                        switch_page("search")
            else:
                st.markdown(f"<h6 style='text-align:center; font-weight:lighter;color:black'>Upload new resume</h6>",
                            unsafe_allow_html=True)
                ResumePDF = st.file_uploader(
                    ''
                )
                if ResumePDF is not None:
                    pdfReader = PyPDF2.PdfReader(ResumePDF)
                    print(len(pdfReader.pages))
                    pageObj = pdfReader.pages[0]
                    resumeContent = pageObj.extract_text()
                    ResumePDF.close()
                    firebase = pyrebase.initialize_app(firebaseconfig)
                    AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
                    localId = AccountInfo["localId"]
                    db = firebase.database()
                    FirebaseResumeContent = db.child("users").child(localId).child("Resume").set(resumeContent)
                    st.experimental_rerun()
        with colResume3:
            st.write("")


        Saved, Archive = st.tabs(["Saved", "Arvice"])

        with Saved:
            SavedResults = db.child("users").child(str(localId)).child("Jobs").get().val()
            unique_links = {}

            for key, value in SavedResults.items():
                link = value['Link']
                if link not in unique_links:
                    unique_links[link] = value

            my_dict = unique_links
            colresult1, colresult2, colresult3 = st.columns([0.25, 1, 0.25])
            with colresult1:
                st.write("")
            with colresult2:
                for key, value in my_dict.items():
                    company_name = value['Company Name']
                    Full_Description = value['Full Description']
                    Link = value['Link']
                    Location = value['Location']
                    Short_Summary = value['Short Summary']
                    Skills = value['Skills']
                    Title = value['Title']

                    st.markdown(
                        f"<a href='{Link}' style='text-decoration: none; color: black;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{Title}→ </h4></a>",
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
                                                              key=f"{Link}+{Title}+{Short_Summary}+Generating",
                                                              disabled=True)
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

                    st.markdown("<hr  color=black style = 'margin-top:-5px;background-color:black'>", unsafe_allow_html=True)
            with colresult3:
                st.write("")

        with Archive:
            AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
            firebase = pyrebase.initialize_app(firebaseconfig)
            db = firebase.database()
            localId = AccountInfo["localId"]
            ArchivedResults = db.child("users").child(str(localId)).child("Archive").child("Archive1").get().val()

            unique_links = {}

            for key, value in ArchivedResults.items():
                link = value['Link']
                if link not in unique_links:
                    unique_links[link] = value

            my_dict = unique_links
            colresult1, colresult2, colresult3 = st.columns([0.25, 1, 0.25])
            with colresult1:
                st.write("")
            with colresult2:
                with st.expander("Archive1"):
                    for key, value in my_dict.items():
                        company_name = value['Company Name']
                        Full_Description = value['Full Description']
                        Link = value['Link']
                        Location = value['Location']
                        Short_Summary = value['Short Summary']
                        Skills = value['Skills']
                        Title = value['Title']
                        # with st.expander("Archive1"):
                        st.markdown(
                            f"<a href='{Link}' style='text-decoration: none; color: white;' target='_blank'><h5 style='font-family: Sans-Serif;margin-top:-20px;'>{Title}→ </h5></a>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px; color:white'>{company_name}</h6>",
                            unsafe_allow_html=True)
                        st.markdown("<hr  color=black style = 'margin-top:-5px;background-color:black'>",
                                    unsafe_allow_html=True)
            with colresult3:
                st.write("")



    st.markdown("""
    <style>
    .stAlert{
    visibility:hidden;
    height:0px;
    }
    
    button[data-baseweb="tab"] {
         background-color:#eeeeee;
    color:black
    }

    .css-c0yjmw.e1fqkh3o9{
    visibility:hidden;
    height:0px;
    }
    .css-1lamwuk.e1fqkh3o8{
    visibility:hidden;
    height:0px;
    }
    .css-vp3dme.e1tzin5v0{
    margin-left:-50px;
    margin-top:-70px;
    }

    button[title="View fullscreen"]{
                        visibility: hidden;}
                        
                    ul.streamlit-expander {
                                border: 0 None !important;
                                }
   .css-10trblm.e16nr0p30{
   color:black
   }
                                
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
                               z-index:99999;
                               width: 50%;
                             }
                               .stApp {
                               background-color: #eeeeee;
                               color:black
                               }
                               .element-container.css-l0vo1h.e1tzin5v3
                               {
                               color:black
                               }
                               div.stButton > button:first-child {
                               background-color: #eeeeee;
                               color:black;
                               border-color: black;
                               }
                               div.stButton > button:hover {
                               background-color: #eeeeee;
                               color: #F63366;
                               border-color: #F63366;
                               }
                               .stMarkdown{
                               color:black
                               }
                               .streamlit-expanderHeader{
                               color:black
                               }

                               .css-5y9es8.exg6vvm15{
                               border-radius:50px; 
                               }
                                   .css-5y9es8 {
                                       border-radius:100px;
                                   }
                                   .css-1db87p3{
                                       border-radius:100px;
                                   }
                                   .css-v1vwiw{
                                       border-radius:100px;
                                   }
                               .css-1db87p3.edgvbvh10{
                               border-radius:50px; 
                               }
                               .css-5y9es8.exg6vvm15{
                               filter:invert(1);
                               }
                               .css-1uhah0b.e8zbici2{
                               height:40px;
                               }
                               .css-13e20ss{
                               visibility: hidden;
                               height: 0%;
                               position: fixed;
                               }
                                div[class="stAlert"] {
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
    """, unsafe_allow_html=True)



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
        if st.button("Create New Account",  key = "create_account"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
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