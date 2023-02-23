import streamlit as st
import string
import random
st.set_page_config(page_title="19th Street | Resume Builder", page_icon="📜", layout="wide", initial_sidebar_state='collapsed')
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
              </style>
              """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif; color:black>Coming Sooner</h2>", unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
    

</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

st.markdown("""
    <style>

    css-17z41qg {
        background-color: #eeeeee;
    }
    </style>
    """,unsafe_allow_html=True)


# col1, col2, col3 = st.columns([2, 1, 2])
#
# with col1:
#     st.write("")
#
# with col2:
tab1, tab2, tab3, tab4 = st.tabs(["\u2001Basics\u2001", "\u2001\u2001Experience\u2001\u2001", "\u2001\u2001Projects\u2001\u2001","\u2001\u2001Interests\u2001\u2001"])

with tab1:
    st.header("Details")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.text_input(
        'Name',
        placeholder='Name ',
        help='Name',
        key = 'Name'
        )

        st.text_input(
            'Phone',
            placeholder='Phone Number',
            help='Phone Number',
            key='Phone'
        )
        st.text_input(
            'Email',
            placeholder='Email ',
            help='Email',
            key='Email'
        )
    with col2:
       st.write("")
    with col3:
        st.write("")

with tab2:
    st.header("Experiences")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.text_input(
            '',
            placeholder='Position at Company',
            help='Name',
            key='Experience1'
        )
        st.text_area(
            '',
            placeholder='Description',
            help='Name',
            key='Experience 1 Detail'
        )
        st.markdown("<hr>", unsafe_allow_html=True)

    with col2:
        st.write("")


with tab3:
    st.header("Projects")

with tab4:
    st.header("Interests")
#
# with col3:
#     st.write("")

