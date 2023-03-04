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
              
            .st-bi.st-b3.st-bj.st-b8.st-bk.st-bl.st-bm.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-b1.st-bt.st-au.st-ax.st-av.st-aw.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bu.st-bv.st-bw.st-bx.st-by.st-bz.st-c0{
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