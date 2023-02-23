import streamlit as st
st.set_page_config(page_title="19th Street | Resume Builder", page_icon="📜", layout="wide", initial_sidebar_state='collapsed')
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

#
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #eeeeee
#     }
#
#     .css-hckj40{
#         background-color: #eeeeee
#     }
#    .sidebar .sidebar-content {
#         background: #eeeeee
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
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
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.text_input(
        'Caption goes here',
        placeholder='Placeholder goes here - Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ',
        help='Help message goes here',
        key = ''
        )
    with col2:
        st.text_input(
        'Caption goes here',
        placeholder='Placeholder goes here - Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ',
        help='Help message goes here',
        key = ''
        )
    with col3:
        st.text_input(
        'Caption goes here',
        placeholder='Placeholder goes here - Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ',
        help='Help message goes here',
        key = ''
        )
with tab2:
    st.header("Experiences")

with tab3:
    st.header("Projects")

with tab4:
    st.header("Interests")
#
# with col3:
#     st.write("")

