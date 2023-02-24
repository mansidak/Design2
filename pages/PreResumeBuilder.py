import streamlit as st
import os
st.set_page_config(page_title="19th Street | Resume Builder", page_icon="⓵⓽", layout = "wide")


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
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")



col1, col2, col3, col4, col5 = st.columns([1, 2, 0.1, 2, 1])

with col1:
    st.write("")

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    ResumePDF = st.file_uploader(
        ''
    )
    col11, col22, col33 = st.columns([1,1.75,1])
    with col11:
       st.write("")
    with col22:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.button("Start with your old resume →", key="Old Resume Begin Button")

    with col33:
        st.write("")

with col3:
    st.markdown("<hr style = 'width:0px; border-left: 2px solid grey; height: 300px;'>", unsafe_allow_html=True)
with col4:
    st.write("")
    st.write("")
    st.write("")
    CandidateName = st.text_input(
        'Name',
        placeholder='Name ',
        key='Name'
    )
    st.session_state['CandidateName'] = CandidateName

    CandidatePhone = st.text_input(
        'Phone',
        placeholder='Phone Number',
        key='Phone'
    )
    st.session_state['CandidatePhone'] = CandidatePhone

    CandidateEmail = st.text_input(
        'Email',
        placeholder='Email ',
        key='Email'
    )
    st.session_state['CandidateEmail'] = CandidateEmail

    col111, col222, col333 = st.columns([1, 1.75, 1])

    with col111:
        st.write("")
    with col222:
        st.write("")
        st.button("Go Manually →", key="Go Manually")
    with col333:
        st.write("")

with col5:
    st.write("")