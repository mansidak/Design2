import os
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="19th Street", layout="wide", page_icon='🗽', initial_sidebar_state='collapsed')

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
hide_streamlit_style = """
                  <style>
                  div[class='css-4z1n4l ehezqtx5']{
                    background: rgba(0, 0, 0, 0.3);
                    color: #fff;
                    backdrop-filter: blur(10px);
                    border-radius: 10px;
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

hide_menu_style = """
             <style>
             #MainMenu {visibility: hidden;}
             .css-j7qwjs {visibility: hidden;}
             .css-1uhah0b {visibility: hidden;}
             .css-zmzbej {visibility: hidden;}
             .css-6qob1r {visibility: hidden;}
             .css-leojxt {visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             """
st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

st.markdown(hide_img_fs, unsafe_allow_html=True)
st.markdown(
        """
        <style>
            .css-5y9es8 {
                border-radius:100px;
            }
            .css-1db87p3{
                border-radius:100px;
            }
            .css-v1vwiw{
                border-radius:100px;
            }
        <style>
        """, unsafe_allow_html=True)
# fileup = st.file_uploader("Hello")
st.markdown(
        """
        <style>
            .css-9ycgxx::after {
                content: " as a single-page PDF";
            }
        <style>
        """, unsafe_allow_html=True)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: 0d0d0d;
color: 2A2A2A;
text-align: center;
}
</style>
<div class="footer" font-family: Sans-Serif;font-weight: lighter;>
<p>A Mansidak Singh Production</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.markdown(f"<h1 style='font-family: Sans-Serif; font-weight:lighter; color: black'>ChatGPT can't find you real-time jobs, <br> but <span style='background: -webkit-gradient(linear,left top,right bottom,from(#34C800), to(#FE0000));-webkit-background-clip:text;-webkit-text-fill-color: transparent;'>19th street</span> can.</h1>", unsafe_allow_html=True)

st.markdown(f"<h4 style='font-family: Sans-Serif; font-weight:lighter; color: black'>Introducing world’s first AI-powered job matching platform.</h4>", unsafe_allow_html=True)
st.text("")
st.text("")

col1, col2, col3 = st.columns([2, 1.25, 10])

with col1:
    if st.button("Find Best-Fit Roles"):
        switch_page("app")
with col2:
    st.write("")
    # if st.button("Build Resume"):
    #     switch_page("resumebuilder")

with col3:
    st.write("")


st.text("")
st.text("")

st.markdown(f"<h6 style='font-family: Sans-Serif; font-weight:bold; color: black'>How it works</h6>", unsafe_allow_html=True)
st.markdown(f"<h6 style='font-family: Sans-Serif; font-weight:lighter; color: black'>Drop your resume → Get tailored jobs & cover letters for positions you qualify for.</h6>", unsafe_allow_html=True)
