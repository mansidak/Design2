import streamlit as st
st.set_page_config(page_title="19th Street | Resulsts", page_icon="⓵⓽")
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

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.write("")

with col2:
    image = Image.open('PenManLogo.png')
    st.image(image)

with col3:
    st.write("")

st.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{st.session_state['Name']}</h2>", unsafe_allow_html=True)
st.markdown( f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Tip: You can ask 19th Street to write custom cover letters for each job.</h6>", unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
    ul.streamlit-expander {
            border: 0 None !important;
            }
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

with st.sidebar:
    if st.button("Run Again"):
        switch_page("streamlit_app")


st.write("")
st.write("")

col111, col222 = st.columns([1,1])
with col111:
    options = st.multiselect('Filter through location', set([item[5] for item in st.session_state['FinalResults']]), None, key="option1")
with col222:
    options2 = st.multiselect('Skills you want to use', set([item[6] for item in st.session_state['FinalResults']]), None, key = "option2")


st.write("")
st.write("")
st.write("")
st.write("")

for element in st.session_state['FinalResults']:
    if element[5] in options and element[6] in options2:
        link = element[0]
        title = element[1]
        companyName = element[2]
        shortSummary = element[3]
        fullDescription = element[4]
        location = element[5]
        skills = element[6]

        st.markdown(
            f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
            unsafe_allow_html=True)

        with st.expander(f"{location}"):
            st.markdown(f"[Apply]({link})")
            st.write(f"{shortSummary}")
            st.write(f"{skills}")

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                container_2 = st.empty()
                button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                if button_A:
                    container_2.empty()
                    button_B = container_2.button('Generating... Please wait.', key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
                    responseJob = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"summarize the job: {fullDescription}",
                        temperature=0.7,
                        max_tokens=556,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    jobSummary = responseJob["choices"][0]["text"]
                    CoverLetterResponse = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"I have a cover letter format for you:\n\nFirst paragraph: Write about why the candidate is applying to this job. give one of the candidate's skills and relate it to the job requirements. Then give another skill of the job candidate and relate it to the job requirements. \n\nSecond Paragraph: Pick candidate's strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nThird Paragraph:  Pick candidate's second strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nFourth Paragraph: Conclude with how the candidate is excited to be able to contribute to the job and the company and grow more in a very mature way. \n\n\nHere's the job description:\n{jobSummary}\n\nHere's the resume data content:\n\n {st.session_state['resumeContent']}",
                        temperature=0.7,
                        max_tokens=563,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    cover_letter_file = CoverLetterResponse["choices"][0]["text"]
                    st.download_button('Download Cover Letter', cover_letter_file)

            with col2:
                st.write("")
                # if st.button("Apply", key=f"{link}+{title}+Apply"):
                #     js = f"window.open('{link}')"  # New tab or window

            with col3:
                st.write("")

        st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

    elif not options and element[6] in options2:
        link = element[0]
        title = element[1]
        companyName = element[2]
        shortSummary = element[3]
        fullDescription = element[4]
        location = element[5]
        skills = element[6]

        st.markdown(
            f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
            unsafe_allow_html=True)

        with st.expander(f"{location}"):
            st.markdown(f"[Apply]({link})")
            st.write(f"{shortSummary}")
            st.write(f"{skills}")

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                container_2 = st.empty()
                button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                if button_A:
                    container_2.empty()
                    button_B = container_2.button('Generating... Please wait.', key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
                    responseJob = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"summarize the job: {fullDescription}",
                        temperature=0.7,
                        max_tokens=556,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    jobSummary = responseJob["choices"][0]["text"]
                    CoverLetterResponse = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"I have a cover letter format for you:\n\nFirst paragraph: Write about why the candidate is applying to this job. give one of the candidate's skills and relate it to the job requirements. Then give another skill of the job candidate and relate it to the job requirements. \n\nSecond Paragraph: Pick candidate's strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nThird Paragraph:  Pick candidate's second strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nFourth Paragraph: Conclude with how the candidate is excited to be able to contribute to the job and the company and grow more in a very mature way. \n\n\nHere's the job description:\n{jobSummary}\n\nHere's the resume data content:\n\n {st.session_state['resumeContent']}",
                        temperature=0.7,
                        max_tokens=563,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    cover_letter_file = CoverLetterResponse["choices"][0]["text"]
                    st.download_button('Download Cover Letter', cover_letter_file)

            with col2:
                st.write("")
                # if st.button("Apply", key=f"{link}+{title}+Apply"):
                #     js = f"window.open('{link}')"  # New tab or window

            with col3:
                st.write("")

        st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

    elif not options2 and element[5] in options:
        link = element[0]
        title = element[1]
        companyName = element[2]
        shortSummary = element[3]
        fullDescription = element[4]
        location = element[5]
        skills = element[6]

        st.markdown(
            f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
            unsafe_allow_html=True)

        with st.expander(f"{location}"):
            st.markdown(f"[Apply]({link})")
            st.write(f"{shortSummary}")
            st.write(f"{skills}")

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                container_2 = st.empty()
                button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                if button_A:
                    container_2.empty()
                    button_B = container_2.button('Generating... Please wait.', key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
                    responseJob = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"summarize the job: {fullDescription}",
                        temperature=0.7,
                        max_tokens=556,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    jobSummary = responseJob["choices"][0]["text"]
                    CoverLetterResponse = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"I have a cover letter format for you:\n\nFirst paragraph: Write about why the candidate is applying to this job. give one of the candidate's skills and relate it to the job requirements. Then give another skill of the job candidate and relate it to the job requirements. \n\nSecond Paragraph: Pick candidate's strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nThird Paragraph:  Pick candidate's second strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nFourth Paragraph: Conclude with how the candidate is excited to be able to contribute to the job and the company and grow more in a very mature way. \n\n\nHere's the job description:\n{jobSummary}\n\nHere's the resume data content:\n\n {st.session_state['resumeContent']}",
                        temperature=0.7,
                        max_tokens=563,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    cover_letter_file = CoverLetterResponse["choices"][0]["text"]
                    st.download_button('Download Cover Letter', cover_letter_file)

            with col2:
                st.write("")
                # if st.button("Apply", key=f"{link}+{title}+Apply"):
                #     js = f"window.open('{link}')"  # New tab or window

            with col3:
                st.write("")

        st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

    elif not options and not options2:
        link = element[0]
        title = element[1]
        companyName = element[2]
        shortSummary = element[3]
        fullDescription = element[4]
        location = element[5]
        skills = element[6]

        st.markdown(
            f"<a href='{link}' style='text-decoration: none; color: white;' target='_blank'><h4 style='font-family: Sans-Serif;margin-top:-20px;'>&nbsp;&nbsp;{title}→ </h4></a>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h6 style='font-family: Sans-Serif;font-weight: bold;margin-top:-20px;'>&nbsp;&nbsp;&nbsp;{companyName}</h6>",
            unsafe_allow_html=True)

        with st.expander(f"{location}"):
            st.markdown(f"[Apply]({link})")
            st.write(f"{shortSummary}")
            st.write(f"{skills}")

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                container_2 = st.empty()
                button_A = container_2.button('Generate Cover Letter', key=f"{link}+{title}+{shortSummary}")
                if button_A:
                    container_2.empty()
                    button_B = container_2.button('Generating... Please wait.', key=f"{link}+{title}+{shortSummary}+Generating", disabled=True)
                    responseJob = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"summarize the job: {fullDescription}",
                        temperature=0.7,
                        max_tokens=556,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    jobSummary = responseJob["choices"][0]["text"]
                    CoverLetterResponse = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"I have a cover letter format for you:\n\nFirst paragraph: Write about why the candidate is applying to this job. give one of the candidate's skills and relate it to the job requirements. Then give another skill of the job candidate and relate it to the job requirements. \n\nSecond Paragraph: Pick candidate's strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nThird Paragraph:  Pick candidate's second strongest skills and elaborate on it giving exmaples of their past experiences. Write at least 100 words. Make sure to relate it to the job description\n\nFourth Paragraph: Conclude with how the candidate is excited to be able to contribute to the job and the company and grow more in a very mature way. \n\n\nHere's the job description:\n{jobSummary}\n\nHere's the resume data content:\n\n {st.session_state['resumeContent']}",
                        temperature=0.7,
                        max_tokens=563,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    cover_letter_file = CoverLetterResponse["choices"][0]["text"]
                    st.download_button('Download Cover Letter', cover_letter_file)

            with col2:
                st.write("")
                # if st.button("Apply", key=f"{link}+{title}+Apply"):
                #     js = f"window.open('{link}')"  # New tab or window

            with col3:
                st.write("")

        st.markdown("<hr style = 'margin-top:-5px;'>", unsafe_allow_html=True)

