import streamlit as st

st.set_page_config(page_title="19th Street | Resulsts", page_icon="⓵⓽", initial_sidebar_state="expanded", layout="wide")
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
import extra_streamlit_components as stx
import datetime
import random
from streamlit_extras.switch_page_button import switch_page
import pdfkit
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import pyrebase
import requests
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

def main(user: object):
    st.write(f"You're logged in as {st.session_state['user']['email']}")
    set_code(code=user['refreshToken'])
    switch_page("results")

def get_manager():
    return stx.CookieManager()
cookie_manager = get_manager()

def set_code(code: str):
    st.experimental_set_query_params(code=code)
    cookie = "queryParamCode"
    val = str(code)
    cookie_manager.set(cookie, val, expires_at=datetime.datetime(year=2024, month=2, day=2))




def login_form(auth):
    email = st.text_input(
        label="email", placeholder="fullname@gmail.com")
    password = st.text_input(
        label="password", placeholder="password", type="password")

    if st.button("login"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.session_state['user'] = user
            st.experimental_rerun()
        except requests.HTTPError as exception:
            st.write(exception)
        switch_page("betaa")


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
        code = st.experimental_get_query_params()['code'][0]

        refreshToken = refresh_session_token(auth=auth, code=code)

        if refreshToken == 'fail to refresh':
            raise(ValueError)

        user = get_user_token(auth, refreshToken=refreshToken)

        main(user=user)
    except:
        st.title("Login")
        login_form(auth)

else:
    main(user=st.session_state['user'])
