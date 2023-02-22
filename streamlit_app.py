import os
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="9th Street", layout="wide")

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
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.markdown(f"<h1 style='font-family: Sans-Serif; font-weight:lighter; color: black'>ChatGPT can't find you real-time jobs, <br> but <span style='background: -webkit-gradient(linear,left top,right bottom,from(#34C800), to(#FE0000));-webkit-background-clip:text;-webkit-text-fill-color: transparent;'>9th street</span> can.</h1>", unsafe_allow_html=True)

st.markdown(f"<h4 style='font-family: Sans-Serif; font-weight:lighter; color: black'>Introducing world’s first AI-powered job matching platform.</h4>", unsafe_allow_html=True)
st.text("")
st.text("")

if st.button("Find Best-Fit Roles"):
    switch_page("app")

st.text("")
st.text("")

st.markdown(f"<h6 style='font-family: Sans-Serif; font-weight:bold; color: black'>How it works</h6>", unsafe_allow_html=True)
st.markdown(f"<h6 style='font-family: Sans-Serif; font-weight:lighter; color: black'>Drop your resume → Get tailored jobs & cover letters for positions you qualify for.</h6>", unsafe_allow_html=True)
