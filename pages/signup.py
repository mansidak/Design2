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


st.subheader("One last thing...")
with st.expander("Create a dashboard to save the jobs you're about to see"):
    email = st.text_input('Email', key='email', placeholder="Email")
    password = st.text_input('Password', key='password', placeholder="Email")
    col1Signup, col2Signup = st.columns([1, 1])
    with col1Signup:
        if st.button("Create New Account", key="NewAccount"):
            firebase = pyrebase.initialize_app(firebaseconfig)
            auth = firebase.auth()
            auth.create_user_with_email_and_password(email=email, password=password)
            user = auth.sign_in_with_email_and_password(email=email, password=password)
            st.session_state['user'] = user
            db = firebase.database()
            switch_page("results")
    with col2Signup:
        if st.button("Login", key="login"):
            firebase = pyrebase.initialize_app(firebaseconfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email=email, password=password)
            st.session_state['user'] = user
            db = firebase.database()
            switch_page("results")