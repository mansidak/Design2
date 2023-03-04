import streamlit as st
st.set_page_config(page_title="19th Street | Resume Builder 1", page_icon="⓵⓽",  initial_sidebar_state='collapsed', layout="wide")
# st.title("CoverLetter")
import openai
from docx import Document
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import pdfkit

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

st.header("Does everything look good?")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["\u2001Basics\u2001", "\u2001\u2001Experience\u2001\u2001", "\u2001\u2001Projects\u2001\u2001","\u2001\u2001Skills\u2001\u2001", "\u2001\u2001Result\u2001\u2001"])
with tab1:
    CandidateName = st.text_input(
        'Name',
        placeholder='Name ',
        key='Name'
    )

    CandidatePhone = st.text_input(
        'Phone',
        placeholder='Phone Number',
        key='Phone'
    )

    CandidateEmail = st.text_input(
        'Email',
        placeholder='Email ',
        key='Email'
    )
with tab2:
    st.text_area(label="", value=st.session_state['OldExperiences'])

    with st.expander("Experience 1", expanded=False):
        Experience1Name = st.text_input(
            '',
            placeholder='Position at Company',
            key='Experience1',
            value= {st.session_state['OldExperiences'].split('1a.')[1].split('2a.')[0]}
        )

        Experience1Description = st.text_area(
            '',
            placeholder='Description',
            key='Experience 1 Detail',
            value = {st.session_state['OldExperiences'].split('1b.')[1].split('2b.')[0]}

        )
    with st.expander("Experience 2", expanded=False):
        Experience2Name = st.text_input(
            '',
            placeholder='Position at Company',
            key='Experience2',
            value={st.session_state['OldExperiences'].split('2a.')[1].split('3a.')[0]}
        )
        Experience2Description = st.text_area(
            '',
            placeholder='Description',
            key='Experience 2 Detail',
            value={st.session_state['OldExperiences'].split('2b.')[1].split('3b.')[0]}

        )
    with st.expander("Experience 3", expanded=False):
        Experience3Name = st.text_input(
            '',
            placeholder='Position at Company',
            key='Experience3',
            value={st.session_state['OldExperiences'].split('3a.')[1].split('4a.')[0]}

        )
        Experience3Description = st.text_area(
            '',
            placeholder='Description',
            key='Experience 3 Detail',
            value={st.session_state['OldExperiences'].split('3b.')[1].split('4b.')[0]}

        )
    with st.expander("Experience 4", expanded=False):
        Experience4Name = st.text_input(
            '',
            placeholder='  Position at Company',
            key='Experience4',
            value={st.session_state['OldExperiences'].split('4a.')[1].split('1b.')[0]}

        )
        Experience4Description = st.text_area(
            '',
            placeholder='Description',
            key='Experience 4 Detail',
            value={st.session_state['OldExperiences'].split('4b.')[1]}

        )
    with st.expander("Experience 5", expanded=False):
        Experience5Name = st.text_input(
            '',
            placeholder='Position at Company',
            key='Experience5'
        )
        Experience5Description = st.text_area(
            '',
            placeholder='Description',
            key='Experience 5 Detail'
        )



with tab3:
    st.text_area(label="", value=st.session_state['OldProjects'])
with tab4:
    if 'Skills' not in st.session_state:
        if st.button("Add Skills"):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"The following is some experience of a job seeker.\n\n{Experience1Name}\n{Experience1Description}\n\n{Experience2Name}\n{Experience2Description}\n\n{Experience3Name}\n{Experience3Description}\n\n{Experience4Name}\n{Experience4Description} \n What kind of technical skills they have? List them as spearated by commas.\n",
                temperature=0.7,
                max_tokens=80,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            PreSkills= response["choices"][0]["text"].split(",")
            st.session_state['Skills'] = ','.join(PreSkills)

            FinalSkills = st.text_input(
            'Caption goes here',
            placeholder='Placeholder goes here',
            help='Help message goes here',
            value= st.session_state['Skills']
            )
with tab5:
    st.write("")