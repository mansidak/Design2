import streamlit as st
import os
import openai
from streamlit_extras.switch_page_button import switch_page
import PyPDF2
import datetime
import requests
from streamlit_option_menu import option_menu

import extra_streamlit_components as stx
from st_btn_select import st_btn_select
import pyrebase

st.set_page_config(page_title="19th Street | Resume Builder", page_icon="⓵⓽", layout="wide", initial_sidebar_state="collapsed")


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
    def main(user: object):
        coldash1, coldash2, coldash3 = st.columns([1, 2, 1])
        with coldash1:
            st.write("")
        with coldash2:
            selected2 = option_menu(None, ["Home", "Search", "Build", 'Dashboard'],
                                    icons=['house', 'search', "file-earmark-font", 'stack'],
                                    menu_icon="cast", default_index=2, orientation="horizontal",
                                    styles={
                                        "container": {"padding": "0!important", "background-color": "#0f0f0f"},
                                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px",
                                                     "--hover-color": "#0f0f0f", "color": "white",
                                                     "background-color": "#0f0f0f"},
                                        "nav-link-selected": {"font-weight": "bold", "background-color": "#0f0f0f",
                                                              "color": "#F63366"},
                                    })

            if selected2 == "Home":
                switch_page("home")
            elif selected2 == "Search":
                switch_page("betaa")
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


                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(7){
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
                if st.button("Upload old resume →", key="Old Resume Begin Button"):
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

                             Most importantly, you don't change any of the contents of the description. Report it as is.
                             """},
                            {"role": "user",
                             "content": f"Here's the resume:\n{ResumeToCorrectContent}"}])
                    st.session_state['OldExperiences'] = responseExperiences["choices"][0]["message"]["content"]

                    responseBasicInfo = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system",
                             "content": """
                                         You are an AI Assistant that is able to recognize the Full Name, Phone Number and Email address from a job seeker's resume if they're provided. 
                                         Your response is in the following format:
                                         1a. Full Name
                                         2a. Phone Number (if listed)
                                         3a. Email Address (if listed)

                                         Most importantly, you don't change any of the contents of the description. Report it as is. And you don't any extra fluff to your response.
                                         """},
                            {"role": "user",
                             "content": f"Here's the resume:\n{ResumeToCorrectContent}"}])
                    st.session_state['BasicInfo'] = responseBasicInfo["choices"][0]["message"]["content"]

                    switch_page("airesumebuilder")

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
                    switch_page("manualresumebuilder")
            with col333:
                st.write("")

        with col5:
            st.write("")


@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()


def set_code(code: str):
    st.experimental_set_query_params(code=code)
    cookie = "queryParamCode"
    val = str(code)
    cookie_manager.set(cookie, val, expires_at=datetime.datetime(year=2024, month=2, day=2))


col1form, col2form, col3form = st.columns([0.25, 1, 0.25])
with col1form:
    st.write("")
with col2form:
    def login_form(auth):

        st.subheader("All Cookies:")
        cookies = cookie_manager.get_all()
        st.write(cookies)
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
        code = cookie_manager.get(cookie="queryParamCode")

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