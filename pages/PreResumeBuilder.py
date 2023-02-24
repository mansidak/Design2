import streamlit as st
import os
import openai
from streamlit_extras.switch_page_button import switch_page
import PyPDF2
from PIL import Image


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

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")
with col2:
    col11, col22, col33 = st.columns([2, 1, 2])
    with col11:
        image = Image.open('ResumeBold.png')
        st.image(image)
        if st.button("Start with old resume", key="Start with old resume"):
            switch_page("resumebuilder1")
    with col22:
        st.markdown("<hr style = 'width:0px; border-left: 2px solid grey; height: 300px;'>", unsafe_allow_html=True)
    with col33:
        image = Image.open(' ManualBold.png')
        st.image(image)
        if st.button("Fill details manually", key = "filll detials"):
            switch_page("resumebuilder1")
with col3:
    st.write("")