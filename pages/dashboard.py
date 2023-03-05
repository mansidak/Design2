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
entryResults = db.child("users").child(str(user["localId"])).child("Jobs").get().val()[0]
st.write(entryResults)
SavedResults = db.child("users").child(str(user["localId"])).child("Jobs").get().val()
st.write(SavedResults)

# for item in SavedResults:
#     for key in item.keys():
#         company_name = item[key]["Company Name"]
#         link = item[key]["Link"]
#         location = item[key]["Location"]
#         short_summary = item[key]["Short Summary"]
#         skills = item[key]["Skills"]
#         title = item[key]["Title"]
#         st.write(company_name)
#         st.write(link)
#         st.write(location)
#         st.write(short_summary)
#         st.write(skills)
#         st.write(title)