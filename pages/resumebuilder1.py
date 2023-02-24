import streamlit as st
st.set_page_config(page_title="19th Street | Resume Builder 1", page_icon="⓵⓽",  initial_sidebar_state='collapsed')
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

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
            .st-br{
            border-radius:20px;
            -moz-border-radius:20px;
            -webkit-border-radius:20px;
            min-height:500px;
            outline: none;
            }
              </style>
              """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Does everything look good?")
st.subheader("Experiences")
st.text_area(label="",value = st.session_state['OldExperiences'])
st.subheader("Projects")
st.text_area(label="",value = st.session_state['OldProjects'])