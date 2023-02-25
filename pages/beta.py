import os
import random

import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading
from multiprocessing import Pool

import PyPDF2
from docx import Document
import openai
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

css = """
.uploadedFiles {
    display: none;
}
"""

options = Options()
options.add_argument("--headless")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument('--ignore-certificate-errors')


def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)

openai.api_key = os.environ.get("openai_api_key")


if __name__ == "__main__":
    # faviconImage = Image.open('Favicon.ico')
    st.set_page_config(page_title="19th Street", page_icon='⓵⓽',
                       initial_sidebar_state='collapsed')
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

    progress_text = "See your search progress here."
    progress_text_2 = "Hola"

    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


    with Pool(2) as p:


        @st.cache_data(show_spinner=False)
        def run_selenium1(jobTitle, skill1, undesired, pageNumber, resumeContent):
            name = str()
            Final_Array = []
            options = Options()
            options.add_argument("--headless")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-features=NetworkService")
            options.add_argument("--window-size=1920x1080")
            options.add_argument("--disable-features=VizDisplayCompositor")
            options.add_argument('--ignore-certificate-errors')

            # lock = threading.Lock()
            @st.cache_data(show_spinner=False)
            def get_links(i, resumeContent):
                Final_Links = []
                Final_Titles = []
                Final_Company = []
                Final_Description = []
                Final_Location = []
                shortened_summary = []
                Final_Skills = []
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(i)
                # time.sleep(2)
                elements = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[1]/a")
                for a in elements:
                    if str(a.get_attribute('href')).startswith("https://out.linkup.com/") and a.get_attribute(
                            'href') not in Final_Links:
                        Final_Links.append(a.get_attribute('href'))
                title = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[2]/div[1]/h2").text
                st.write(title)
                Final_Titles.append(title)
                location = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[1]/div/div/p[2]").text
                Final_Location.append(location)
                Final_Skills.append(skill1)
                company = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div/h6[1]").text
                Final_Company.append(company)

                description = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[3]").text
                Final_Description.append(description)
                words = description.split()
                description_length = len(words)
                if description_length > 950:
                    sliced_description = ''.join(words[:950])
                    response3 = openai.Completion.create(
                        model="text-curie-001",
                        prompt=f"The following a conversation between and a job summarization bot. \n\nHuman: Can you summarze the following job posting? Don't return empty completion. \nStart of job posting:\n\nPosition Summary: Teach esthetics curriculum at West Park Center located at 87th and Farley, Overland Park, Kansas. This program prepares students to take the Kansas Board of Cosmetology esthetics licensure examination while preparing students for a career in the esthetics industry.\n\nRequired Qualifications:\n\nAssociates Degree; if no degree, must have current Cosmetology or Esthetics Practitioner license and evidence of at least five years progressive continuing education in the Cosmetology field or any combination of education, training, and tested experience\nCurrent Cosmetology or Esthetics Instructors License\nMinimum of two years teaching experience (industry or academic) in one of the core areas: Esthetics, Cosmetology, or Nail Technology\nExcellent oral and written communication skills.\nPreferred Qualifications:\n\nSalon or service industry management experience\nKnowledge of Kansas Board of Cosmetology Regulations\nTo be considered for this position we will require an application, resume, and/or cover letter.\n\nBot: This job requires an individual to teach esthetics curriculum at West Park Center in Overland Park, Kansas. The individual must have an Associate's Degree or a current Cosmetology or Esthetics Practitioner License and at least five years of progressive continuing education in the Cosmetology field. They must also have a current Cosmetology or Esthetics Instructors License and at least two years of teaching experience in Esthetics, Cosmetology, or Nail Technology. Excellent oral and written communication skills are also required. Salon or service industry management experience and knowledge of Kansas Board of Cosmetology Regulations are preferred. An application, resume, and/or cover letter are required for consideration, as well as unofficial transcripts.\n\n\n\nHuman. Can you summarize the following job? Don't return empty completion. \n\nStart of job posting:\n\n{sliced_description}\n\nNow summarize it:\n\n\n",
                        temperature=0.31,
                        max_tokens=90,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    shortened_summary.append(response3["choices"][0]["text"])
                else:
                    response3 = openai.Completion.create(
                        model="text-curie-001",
                        prompt=f"The following a conversation between and a job summarization bot. \n\nHuman: Can you summarze the following job posting? Don't return empty completion. \nStart of job posting:\n\nPosition Summary: Teach esthetics curriculum at West Park Center located at 87th and Farley, Overland Park, Kansas. This program prepares students to take the Kansas Board of Cosmetology esthetics licensure examination while preparing students for a career in the esthetics industry.\n\nRequired Qualifications:\n\nAssociates Degree; if no degree, must have current Cosmetology or Esthetics Practitioner license and evidence of at least five years progressive continuing education in the Cosmetology field or any combination of education, training, and tested experience\nCurrent Cosmetology or Esthetics Instructors License\nMinimum of two years teaching experience (industry or academic) in one of the core areas: Esthetics, Cosmetology, or Nail Technology\nExcellent oral and written communication skills.\nPreferred Qualifications:\n\nSalon or service industry management experience\nKnowledge of Kansas Board of Cosmetology Regulations\nTo be considered for this position we will require an application, resume, and/or cover letter.\n\nBot: This job requires an individual to teach esthetics curriculum at West Park Center in Overland Park, Kansas. The individual must have an Associate's Degree or a current Cosmetology or Esthetics Practitioner License and at least five years of progressive continuing education in the Cosmetology field. They must also have a current Cosmetology or Esthetics Instructors License and at least two years of teaching experience in Esthetics, Cosmetology, or Nail Technology. Excellent oral and written communication skills are also required. Salon or service industry management experience and knowledge of Kansas Board of Cosmetology Regulations are preferred. An application, resume, and/or cover letter are required for consideration, as well as unofficial transcripts.\n\n\n\nHuman. Can you summarize the following job? Don't return empty completion. \n\nStart of job posting:\n\n{description}\n\nNow summarize it:\n\n\n",
                        temperature=0.31,
                        max_tokens=90,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    shortened_summary.append(response3["choices"][0]["text"])

                for links, titles, companies, summaries, descriptions, locations, skills in zip(Final_Links, Final_Titles, Final_Company, shortened_summary, Final_Description, Final_Location, Final_Skills):
                    Final_Array.append((links, titles, companies, summaries, descriptions, locations, skills))

                # driver.close()

            with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
                driver.get(
                    f"https://search.linkup.com/search/results/{jobTitle}-jobs?all={skill1}&none={undesired}&pageNum={pageNumber}")
                jobs_block = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]")
                time.sleep(1)
                links = []
                jobs_list1 = jobs_block[0].find_elements(By.CLASS_NAME, "job-listing")

                for job in jobs_list1:
                    all_links = job.find_elements(By.TAG_NAME, "a")
                    for a in all_links:
                        if str(a.get_attribute('href')).startswith(
                                "https://search.linkup.com/details/") and a.get_attribute('href') not in links:
                            links.append(a.get_attribute('href'))
                            print(links)
                        else:
                            pass
            # driver.close()
            # driver.quit()

            threads = []
            for i in links:
                t = threading.Thread(target=get_links, args=(i, resumeContent))
                threads.append(t)
                t.start()
            for t in threads:
                t.join()

            driver.quit()
            return Final_Array

        @st.cache_data(show_spinner=False)
        def openAIGetRelevantJobTitles(resumeContent):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"The following is the data from the resume of a job seeker. I want you to do four things:\n\n1. In addition to what they've already done, what jobs roles could they apply for? List 3 and separate them by commas.\n\n2. List only the top 3 of their strongest skills that they have extensive experience in as seen in their resume. Separate them by commas. \n\n 3. Their Full Name \n\n 4.Their top 3 soft skills  \n\n {resumeContent} \n",
                temperature=0.7,
                max_tokens=146,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            Titles = response["choices"][0]["text"]
            print(Titles)
            Jobtitles = Titles.split('1.')[1].split('2.')[0].split(',')
            Skills = Titles.split('2.')[1].split('3.')[0].split(',')
            Name = Titles.split('3.')[1].split('4.')[0]
            st.session_state["Name"] = Name
            softSkills = Titles.split('4.')[1]
            newJobtitles = [item.replace(" ", "-") for item in Jobtitles]
            newSkills = [item.replace(" ", "-") for item in Skills]
            return Name, newJobtitles, newSkills, softSkills

        col1, col2, col3 = st.columns([2, 1, 2])

        with col1:
            st.write("")

        with col2:
            image = Image.open('PenManLogo.png')
            st.image(image)

        with col3:
            st.write("")

        progressText = st.empty()
        my_bar = st.progress(0, text=progress_text)

        SubTitle = st.empty()
        SubTitle.markdown(
            f"<h4 style='text-align: center;  font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-weight:lighter'>Use AI to discover personalized real-time jobs — by simply scanning your resume.</h4>",
            unsafe_allow_html=True)
        Credits = st.empty()
        Credits.markdown(
            f"<h6 style='text-align: center;  font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-weight:lighter'> </h6>",
            unsafe_allow_html=True)
        holder = st.empty()
        ResumePDF = holder.file_uploader(
            ''
        )
        holder2 = st.empty()
        ExperienceLevel = holder2.selectbox(
            'Select Experience Level',
            (None, 'Intern', 'Entry-Level', 'Associate'),
            help='Experience Level'
        )


        with st.sidebar:
            undesired = st.text_input(
                'Enter upto one company you wish to be excluded',
                placeholder='Excluded Keywords[upto one]',
                help="As we develop this program more, we'll add more filter"
            )

        @st.cache_data(show_spinner=False)
        def extract_text_from_pdf(pdf_file):
            pdfReader = PyPDF2.PdfReader(pdf_file)
            txtFile = open('sample.txt', 'w')
            num_pages = len(pdfReader.pages)
            for page_num in range(num_pages):
                pageObj = pdfReader.pages[page_num]
                txtFile.write(pageObj.extract_text())
                resumeContent = pageObj.extract_text()
            return resumeContent

        if ResumePDF is not None and ExperienceLevel is not None:
            SubTitle.empty()
            Credits.empty()
            holder.empty()
            resumeContent = extract_text_from_pdf(ResumePDF)
            Name, newJobtitles, newSkills, softSkills = openAIGetRelevantJobTitles(resumeContent)
            if 'Name' not in st.session_state:
                st.session_state['Name'] = Name
            if 'resumeContent' not in st.session_state:
                st.session_state["resumeContent"] = resumeContent
            progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Great job, {str(Name).split(' ')[1]}! Your resume is being parsed. Choose your desired type of level</h6>",unsafe_allow_html=True)
            my_bar.progress(25, text=f"")
            result1 = run_selenium1(f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[0]}", f"{undesired}", 1, resumeContent)
            progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Looking for jobs where you can use your experience in {newSkills}etc...</h6>",unsafe_allow_html=True)
            my_bar.progress(50, text=f"")
            result2 = run_selenium1(f"{newJobtitles[1]}-{ExperienceLevel}", f"{newSkills[1]}", f"{undesired}", 1, resumeContent)
            progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>You have some background in {softSkills}. We're looking for more jobs that match that...</h6>",unsafe_allow_html=True)
            my_bar.progress(75, text=f"")
            result3 = run_selenium1(f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[2]}", f"{undesired}", 1, resumeContent)
            st.session_state["FinalResults"] = result1 + result2 + result3
            switch_page("results")
