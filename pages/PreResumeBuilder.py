import streamlit as st
import os

col1, col2, col3, col4 = st.columns[(1,2,2,1)]

with col1:
    st.write("")

with col2:
    ResumePDF = st.file_uploader(
        ''
    )
with col3:
    st.subheader("Or go manually")
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


with col4:
    st.write("")