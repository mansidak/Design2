import streamlit as st
st.set_page_config(page_title="19th Street | Resume Builder", page_icon="📜", initial_sidebar_state='collapsed')
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


st.markdown(
    """
    <style>
    .stApp {
        background-color: #eeeeee
    }

    .css-hckj40{
        background-color: #eeeeee
    }
   .sidebar .sidebar-content {
        background: #eeeeee
    }
    </style>
    """,
    unsafe_allow_html=True
)
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

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.write("")

with col2:
    image = Image.open('Lighter.png')
    st.image(image)

with col3:
    st.write("")

st.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;color:black'>Coming Sooner</h2>", unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
    
    textarea { 
    background-color : #eeeeee; 
    }
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

st.text_area(
  'Enter Experience',
  placeholder="Write briefly about your experience in less than a paragraph. We'll take care of the rest. ",
  help='Help message goes here'
)