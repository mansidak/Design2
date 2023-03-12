import os
import streamlit
import streamlit as st
import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from streamlit_option_menu import option_menu
import threading
from concurrent.futures import ThreadPoolExecutor
import PyPDF2
import openai
from PIL import Image
import extra_streamlit_components as stx
from streamlit_extras.switch_page_button import switch_page
import psutil
import pyrebase

st.set_page_config(page_title="19th Street | Dashboard", page_icon="⓵⓽", initial_sidebar_state="collapsed", layout="wide")

@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()


firebaseconfig = {
            "apiKey": "AIzaSyDCHY-GB5WCd0V6o4psrasOYZL_F7xcODM",
            "authDomain": "nineteenth-street.firebaseapp.com",
            "projectId": "nineteenth-street",
            "storageBucket": "nineteenth-street.appspot.com",
            "messagingSenderId": "964724806859",
            "appId": "1:964724806859:web:010841fc337f30b50cb74e",
            "measurementId": "G-N3TMC7M1WT",
            "databaseURL": "https://nineteenth-street-default-rtdb.firebaseio.com"
        }


if __name__ == "__main__":
    cookies = cookie_manager.get_all()
    # st.write(cookies)
    def main(user: object):

        coldash1, coldash2, coldash3 = st.columns([1, 2, 1])
        with coldash1:
            st.write("")
        with coldash2:
            selected2 = option_menu(None, ["Home", "Search", "Build", 'Dashboard'],
                                    icons=['house', 'search', "file-earmark-font", 'stack'],
                                    menu_icon="cast", default_index=1, orientation="horizontal",
                                    styles={
                                        "container": {"padding": "0!important", "background-color": "#0f0f0f"},
                                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px",
                                                     "--hover-color": "#0f0f0f", "color": "white",
                                                     "background-color": "#0f0f0f"},
                                        "nav-link-selected": {"font-weight": "bold", "background-color": "#0f0f0f",
                                                              "color": "#F63366"},
                                    })

            if selected2 == "Home":
                switch_page("streamlit_app")
            elif selected2 == "Dashboard":
                switch_page("dashboard")
            elif selected2 == "Build":
                switch_page("PreResumeBuilder")

        with coldash3:
            st.write("")

        st.markdown("""
                        <style>
                        
                        .css-1uhah0b.e8zbici2{
                        z-index:1;
                        }
                        
                        header[data-testid="stHeader"] {
                        position: relative;
                        }
                        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(8) {
                            margin-top:-90px;
                            margin-left:-90px;
                            min-width:100%;
                            position:fixed;
                            z-index:2;
                            }

                          .dark{
                                background-color: #eeeeee;
                                color:black;
                                border-color: black;
                                }

                           .dark:hover{
                                background-color: #eeeeee;
                                color: #F63366;
                                border-color: #F63366;
                                }

                            .button.dark {
                              background-color: #4CAF50; /* Green */
                              border: none;
                              color: white;
                              padding: 15px 32px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                            }
                        </style>
                        """, unsafe_allow_html=True)
        st.markdown("""

                <style>
                .stAlert{
                height:0px;
                visibility:hidden
                }
                </style>""", unsafe_allow_html=True)


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

        colmain1, colmain2, colmain3 = st.columns([0.5, 1, 0.5])
        with colmain1:
            st.write("")
        with colmain2:
            # st.write(f"You're logged in as {st.session_state['user']['email']}")
            set_code(code=user['refreshToken'])

            footer = """
                                        <style>
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
            st.markdown(footer, unsafe_allow_html=True)
            hide_streamlit_style = """
                                          <style>
                                          div[class='css-4z1n4l ehezqtx5']{
                                            background: rgba(0, 0, 0, 0.3);
                                            color: #fff;
                                            backdrop-filter: blur(10px);
                                            border-radius: 10px;
                                            height: 40px;
                                            max-width: 175px;
                                            position: fixed;
                                            top: 80%;
                                            left: 50%;
                                            transform: translate(-50%, -50%);
                                            z-index:99999;
                                            width: 50%;
                                          }

                                          css-klqnuk ehezqtx4{

                                          }
                                          .css-1nsk2xq edgvbvh3{
                                          visibility:hidden;
                                          height:0px;
                                          }

                                          .css-14x9thb ehezqtx3
                                          {
                                          visibility:hidden;
                                          height:0px;
                                          }
                                          .css-1nsk2xq{
                                          visibility:hidden;
                                          height:0px;
                                          }

                                          .css-14x9thb
                                          {
                                          visibility:hidden;
                                          height:0px;
                                          }
                                          .st-be{
                                          border-radius: 50px;
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
                    .css-leojxt::before{
                    content: "Filters"
                    }
                    div[data-testid="stSidebarNav"] {
                        visibility: hidden;
                        height: 0%;
                        position: fixed;
                        }

                      div[data-testid="collapsedControl"] {
                        visibility: hidden;
                        height: 0%;
                        position: fixed;
                        }
                <style>
                """, unsafe_allow_html=True)

            progress_text = "See your search progress here."
            progress_text_2 = "Hola"

            hide_menu_style = """
            
            
                                    <style>
                                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(11){
            margin-top:-120px;
            }
                                    #MainMenu {visibility: hidden;}
                                    .css-c0yjmw e1fqkh3o9 {visibility: hidden;}
                                    .css-1lamwuk e1fqkh3o8 {display: none;}
                                    .css-1helkxk e1fqkh3o9{display: none;}

                                    div[data-testid="stSidebarNav"] {
                                        visibility: hidden;
                                        height: 0%;
                                        position: fixed;
                                        }

                                        div[class="stAlert"] {
                                        visibility: hidden;
                                        height: 0%;
                                        position: fixed;
                                        }
                                         div[role="alert"] {
                                        visibility: hidden;
                                        height: 0%;
                                        position: fixed;
                                        }

                                    </style>
                                    """
            st.markdown(hide_menu_style, unsafe_allow_html=True)

            @st.cache(show_spinner=False)
            def run_selenium1(jobTitle, skill1, undesired, pageNumber, resumeContent, locationpreference):
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

                with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
                    try:
                        driver.get(
                            f"https://search.linkup.com/search/results/{jobTitle}-jobs?all={skill1}&none={undesired}&location={locationpreference}&pageNum={pageNumber}")
                        jobs_block = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]")
                        time.sleep(1)
                        links = []
                        jobs_list1 = jobs_block[0].find_elements(By.CLASS_NAME, "job-listing")[:9]
                    except:
                        print("didn't exist")
                    for job in jobs_list1:
                        all_links = job.find_elements(By.TAG_NAME, "a")
                        for a in all_links:
                            if str(a.get_attribute('href')).startswith(
                                    "https://search.linkup.com/details/") and a.get_attribute('href') not in links:
                                links.append(a.get_attribute('href'))
                                print(links)
                            else:
                                pass


                def get_links(i, skill1, resumeContent):
                    Final_Links = []
                    Final_Titles = []
                    Final_Company = []
                    Final_Description = []
                    Final_Location = []
                    shortened_summary = []
                    Final_Skills = []
                    compatibilityScore = []

                    try:
                        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                        driver.get(i)
                        # time.sleep(2)
                        elements = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[1]/a")
                        for a in elements:
                            if str(a.get_attribute('href')).startswith("https://out.linkup.com/") and a.get_attribute(
                                    'href') not in Final_Links:
                                Final_Links.append(a.get_attribute('href'))
                        title = driver.find_element(By.XPATH,
                                                    "/html/body/main/div[2]/div/div[2]/div/div[2]/div[1]/h2").text
                        Final_Titles.append(title)
                        location = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[1]/div/div/p[2]").text
                        Final_Location.append(location)
                        Final_Skills.append(skill1)
                        company = driver.find_element(By.XPATH,
                                                      "/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div/h6[1]").text
                        Final_Company.append(company)

                        description = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[3]").text
                        Final_Description.append(description)
                        words = description.split()
                        description_length = len(words)
                        if description_length > 950:
                            sliced_description = ''.join(words[:950])
                            response3 = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system",
                                     "content": "You are an AI Assistant that summarizes job postings in less than a paragraph. Just talk about what they're looking for."},
                                    {"role": "user",
                                     "content": f"The following is a job posting I want you to summarize \n\n{description}\n\n"}])

                            shortened_summary.append(response3["choices"][0]["message"]["content"])
                            print(response3["usage"]["total_tokens"])
                        else:
                            response3 = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system",
                                     "content": "You are an AI Assistant that summarizes job postings in less than a paragraph. Just talk about what they're looking for."},
                                    {"role": "user",
                                     "content": f"The following is a job posting I want you to summarize \n\n{description}\n\n"}])
                            shortened_summary.append(response3["choices"][0]["message"]["content"])
                            print(response3["usage"]["total_tokens"])

                        compatibilityScoreAPI = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system",
                                     "content": """
                                     You're an AI Bot calculates compatibility score of a job seeker for a given job. Your output should always be of the following format: 
                                     
                                     "Score: (out of 5, example 2.5,3,3.5,4,4.5,5) ;
                                     Skills that match: (list 2-3 skills that overlap with resume);"
                                     
                                     Most importantly, you don't add any extra fluff or explanation to your response. Your response is always in the given format.
                                     """},
                                    {"role": "user",
                                     "content": f"Here's the Job summary \n\n{response3['choices'][0]['message']['content']}\n\n Here's the resume: {resumeContent}"}])


                        compatibilityScore.append(compatibilityScoreAPI["choices"][0]["message"]["content"])
                        print(compatibilityScoreAPI["usage"]["total_tokens"])
                        for links, titles, companies, summaries, descriptions, locations, skills, compatibilityScores in zip(Final_Links,
                                                                                                        Final_Titles,
                                                                                                        Final_Company,
                                                                                                        shortened_summary,
                                                                                                        Final_Description,
                                                                                                        Final_Location,
                                                                                                        Final_Skills,
                                                                                                        compatibilityScore):
                            Final_Array.append((links, titles, companies, summaries, descriptions, locations, skills, compatibilityScores))

                        driver.close()
                        driver.quit()
                    except:
                        driver.close()
                        driver.quit()
                    return Final_Array

                with ThreadPoolExecutor() as executor:
                    futures = [executor.submit(get_links, link, skill1, resumeContent) for link in links]
                    result1 = [future.result() for future in futures]
                    result11 = sum(result1, [])
                executor.shutdown(wait=True)

                return result11

            @st.cache(show_spinner=False)
            def openAIGetName(resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You are an AI Assistant that grabs the name of a person from resume data and outputs their full name. Your response shouldn't have any extra fluff."},
                        {"role": "user",
                         "content": f"The following is the data from the resume of a job seeker. \n\n{resumeContent}\n\nTheir full name is:"}])

                Name = response["choices"][0]["message"]["content"]
                st.session_state['Name']=Name

                return Name

            def openAIGetRelevantJobTitlesDuplicate(resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You're an AI bot that scans the resume of a job seeker and suggest 7 generic but different job titles that they should pursue. You don't add extra fluff in your response and your response should always have the format of 'title 1, title 2, title 3, title 4, title 5, title 6'."},
                        {"role": "user",
                         "content": f"The resume is as follows: \n\n{resumeContent}\n\n"}])

                JobTitles = response["choices"][0]["message"]["content"]
                return JobTitles

            def openAIGetRelevantHardSkills(resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You're an AI bot that takes in the resume description of a job seeker and outputs the technical skills that appear most frequently in the resume of the person. You don't add extra fluff in your response and your response should always have the format of 'skill1, skill2, skill3, skill4, skill5, skill6'."},
                        {"role": "user",
                         "content": f"The resume is as follows: \n\n{resumeContent}\n\n"}])

                HardSkills = response["choices"][0]["message"]["content"]
                # st.write(HardSkills)
                return HardSkills

            def openAIGetRelevantSoftSkills(resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You're an AI bot that takes in the resume description of a job seeker and outputs the soft skills (like communication, team work etc.) that the person posses. You don't add extra fluff in your response and your response should always have the format of 'skill1, skill2, skill3, skill4, skill5, skill6'."},
                        {"role": "user",
                         "content": f"The resume is as follows: \n\n{resumeContent}\n\n"}])

                SoftSkills = response["choices"][0]["message"]["content"]
                # st.write(SoftSkills)
                return SoftSkills

            def openAIGetAllSkills(resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You're an AI bot that takes in the resume description of a job seeker and outputs all the technical skills the person possesses. You don't add extra fluff in your response and your response should always have the format of 'skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9, skill10'."},
                        {"role": "user",
                         "content": f"The resume is as follows: \n\n{resumeContent}\n\n"}])

                AllSkills = response["choices"][0]["message"]["content"]
                # st.write(AllSkills)
                return AllSkills

            def openAIMatchSkillsWithJobs(Skills, JobTitles, resumeContent):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You're an AI bot that can match job titles with relevant skills in that industry. For example if you get Skills = 'skill1, skill2, skill3, skill4' and Job Titles = 'job title 1, job title 2, job title 3, job title 4'. You will match the skills that are related to each jobs and list the out put as ' job title 1 : skill 3, job title 2: skill 4, job title 3: skill 2, job title 4: skill1'. If there are no skills matching for that job title, assign a random skill from the data. Your response should not have any extra fluff and you shouldn't add any skills of your own.Also you cannot match one job to more than one skill."},
                        {"role": "user",
                         "content": f"""
                                 Skills = {Skills}.
                                 Job Titles = {JobTitles}.
                                """}])

                Matched = response["choices"][0]["message"]["content"]
                # st.write(Matched)
                return Matched

            col1, col2, col3 = st.columns([2, 1, 2])

            with col1:
                st.write("")

            with col2:
                image = Image.open('PenManLogo.png')
                st.image(image)

            with col3:
                st.write("")

            NameHolder = st.empty()
            progressText = st.empty()
            my_bar = st.empty()

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


            def extract_text_from_pdf(pdf_file):

                pdfReader = PyPDF2.PdfReader(pdf_file)
                print(len(pdfReader.pages))
                pageObj = pdfReader.pages[0]
                resumeContent = pageObj.extract_text()
                pdf_file.close()
                firebase = pyrebase.initialize_app(firebaseconfig)
                AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
                localId = AccountInfo["localId"]
                db = firebase.database()
                FirebaseResumeContent = db.child("users").child(localId).child("Resume").set(resumeContent)
                return resumeContent

            def MatchMethod(Matches):
                job_skills = {}
                lines = Matches.split("\n")
                for line in lines:
                    job_desc = line.split(":")
                    job = job_desc[0]
                    first_skill = job_desc[1].split(",")[0].strip()
                    job_skills[job] = first_skill

                job_titles = []
                skills = []

                for job, skill in job_skills.items():
                    job_titles.append(job)
                    skills.append(skill)

                return job_titles, skills

            if ResumePDF is not None:
                SubTitle.empty()
                Credits.empty()
                holder.empty()
                resumeContent = extract_text_from_pdf(ResumePDF)
                Name = openAIGetName(resumeContent)
                firebase = pyrebase.initialize_app(firebaseconfig)
                AccountInfo = auth.get_account_info(user['idToken'])["users"][0]
                localId = AccountInfo["localId"]
                db = firebase.database()
                db.child("users").child(localId).child("Name").set(Name)

                if 'Name' not in st.session_state:
                    st.session_state['Name'] = Name
                if 'resumeContent' not in st.session_state:
                    st.session_state["resumeContent"] = resumeContent
                NameHolder.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{Name}</h2>",
                                    unsafe_allow_html=True)
                if 'newSkills' not in st.session_state:
                    colspinner1, colspinner2, colspinner3 = st.columns([1,0.8,1])
                    with colspinner2:
                        with st.spinner("Parsing resume..."):
                            try:
                                newJobtitles = openAIGetRelevantJobTitlesDuplicate(resumeContent)
                                newSkills = openAIGetRelevantHardSkills(resumeContent)
                                softSkills = openAIGetRelevantSoftSkills(resumeContent)
                                OldSkillsBullet = openAIGetAllSkills(resumeContent)
                                Matches = openAIMatchSkillsWithJobs(newSkills, newJobtitles, resumeContent)

                                st.session_state['newJobtitles'] = newJobtitles
                                st.session_state['newSkills'] = newSkills
                                st.session_state['softSkills'] = softSkills
                                st.session_state['OldSkillsBullet'] = OldSkillsBullet
                                st.session_state['Matches'] = Matches
                            except:
                                streamlit.experimental_rerun
                newSkills = st.session_state['newSkills']
                newJobtitles = st.session_state['newJobtitles']
                OldSkillsBullet = st.session_state['OldSkillsBullet']
                softSkills = st.session_state['softSkills']
                Matches = st.session_state['Matches']
                # st.write(newJobtitles)
                FreshJobTitles, FreshSkills = MatchMethod(Matches)
                # st.write(FreshJobTitles, FreshSkills)
                with st.form("my_form"):
                    holder2 = st.empty()
                    ExperienceLevel = holder2.selectbox(
                        'Select Experience Level (Required)',
                        (None, 'Intern', 'Entry-Level', 'Associate'),
                        key="ExperienceLevel"
                    )

                    holder3 = st.empty()
                    undesired3 = holder3.selectbox(
                        "Is there something you don't wanna do again?",
                        ((" ," + OldSkillsBullet).split(',')),
                        key="Undesired"
                    )
                    undesired = undesired3.replace(" ", "")
                    holder4 = st.empty()
                    locationpreference = holder4.selectbox(
                        'Location Preferences, if any. (This might limit your search results.)', ("",
                                                                                                  " New York, New York",
                                                                                                  " Los Angeles, California",
                                                                                                  " Chicago, Illinois",
                                                                                                  " Houston, Texas",
                                                                                                  " Phoenix, Arizona",
                                                                                                  " Philadelphia, Pennsylvania",
                                                                                                  " San Antonio, Texas",
                                                                                                  " San Diego, California",
                                                                                                  " Dallas, Texas ",
                                                                                                  " San Jose, California ",
                                                                                                  " Austin, Texas ",
                                                                                                  " Jacksonville, Florida ",
                                                                                                  " Fort Worth, Texas ",
                                                                                                  " Columbus, Ohio ",
                                                                                                  " San Francisco, California ",
                                                                                                  " Charlotte, North Carolina ",
                                                                                                  " Indianapolis, Indiana ",
                                                                                                  " Seattle, Washington ",
                                                                                                  " Denver, Colorado ",
                                                                                                  " Washington, DC ",
                                                                                                  " Boston, Massachusetts ",
                                                                                                  " El Paso, Texas ",
                                                                                                  " Detroit, Michigan ",
                                                                                                  " Nashville, Tennessee ",
                                                                                                  " Portland, Oregon ",
                                                                                                  " Memphis, Tennessee ",
                                                                                                  " Oklahoma City, Oklahoma ",
                                                                                                  " Las Vegas, Nevada ",
                                                                                                  " Louisville, Kentucky ",
                                                                                                  " Baltimore, Maryland ",
                                                                                                  " Milwaukee, Wisconsin ",
                                                                                                  " Albuquerque, New Mexico ",
                                                                                                  " Tucson, Arizona ",
                                                                                                  " Fresno, California ",
                                                                                                  " Sacramento, California ",
                                                                                                  " Long Beach, California ",
                                                                                                  " Kansas City, Missouri ",
                                                                                                  " Mesa, Arizona ",
                                                                                                  " Virginia Beach, Virginia ",
                                                                                                  " Atlanta, Georgia ",
                                                                                                  " Colorado Springs, Colorado ",
                                                                                                  " Omaha, Nebraska ",
                                                                                                  " Raleigh, North Carolina ",
                                                                                                  " Miami, Florida ",
                                                                                                  " Oakland, California ",
                                                                                                  " Minneapolis, Minnesota ",
                                                                                                  " Tulsa, Oklahoma ",
                                                                                                  " Cleveland, Ohio ",
                                                                                                  " Wichita, Kansas ",
                                                                                                  " New Orleans, Louisiana ",
                                                                                                  " Arlington, Texas ",
                                                                                                  " Bakersfield, California ",
                                                                                                  " Tampa, Florida ",
                                                                                                  " Honolulu, Hawaii ",
                                                                                                  " Aurora, Colorado ",
                                                                                                  " Anaheim, California ",
                                                                                                  " Santa Ana, California ",
                                                                                                  " St.  Louis, Missouri ",
                                                                                                  " Riverside, California ",
                                                                                                  " Corpus Christi, Texas ",
                                                                                                  " Lexington, Kentucky ",
                                                                                                  " Pittsburgh, Pennsylvania ",
                                                                                                  " Anchorage, Alaska ",
                                                                                                  " Stockton, California ",
                                                                                                  " Cincinnati, Ohio ",
                                                                                                  " Saint Paul, Minnesota ",
                                                                                                  " Toledo, Ohio ",
                                                                                                  " Newark, New Jersey ",
                                                                                                  " Greensboro, North Carolina ",
                                                                                                  " Plano, Texas ",
                                                                                                  " Henderson, Nevada ",
                                                                                                  " Lincoln, Nebraska ",
                                                                                                  " Buffalo, New York ",
                                                                                                  " Fort Wayne, Indiana ",
                                                                                                  " Jersey City, New Jersey ",
                                                                                                  " Chula Vista, California ",
                                                                                                  " Orlando, Florida ",
                                                                                                  " St. Petersburg, Florida ",
                                                                                                  " Norfolk, Virginia ",
                                                                                                  " Chandler, Arizona ",
                                                                                                  " Laredo, Texas ",
                                                                                                  " Madison, Wisconsin ",
                                                                                                  " Durham, North Carolina ",
                                                                                                  " Lubbock, Texas ",
                                                                                                  " Garland, Texas ",
                                                                                                  " Glendale, Arizona ",
                                                                                                  " Winston-Salem, North Carolina ",
                                                                                                  " Reno, Nevada ",
                                                                                                  " Hialeah, Florida ",
                                                                                                  " Baton Rouge, Louisiana ",
                                                                                                  " Irving, Texas ",
                                                                                                  " Scottsdale, Arizona ",
                                                                                                  " North Las Vegas, Nevada ",
                                                                                                  " Fremont, California ",
                                                                                                  " Chesapeake, Virginia ",
                                                                                                  " Gilbert, Arizona ",
                                                                                                  " Akron, Ohio ",
                                                                                                  " Rochester, New York ",
                                                                                                  " Bois, Idaho ",
                                                                                                  " Modesto, California ",
                                                                                                  " Montgomery, Alabama ",
                                                                                                  " Spokane, Washington ",
                                                                                                  " Des Moines, Iowa ",
                                                                                                  " Richmond, Virginia ",
                                                                                                  " Yonkers, New York ",
                                                                                                  " Tacoma, Washington ",
                                                                                                  " Glendale, California ",
                                                                                                  " Irvine, California ",
                                                                                                  " Shreveport, Louisiana ",
                                                                                                  " Grand Rapids, Michigan ",
                                                                                                  " Birmingham, Alabama ",
                                                                                                  " Knoxville, Tennessee ",
                                                                                                  " Amarillo, Texas ",
                                                                                                  " Huntington Beach, California ",
                                                                                                  " Columbus, Georgia ",
                                                                                                  " Salt Lake City, Utah ",
                                                                                                  " Augusta, Georgia ",
                                                                                                  " Mobile, Alabama ",
                                                                                                  " Little Rock, Arkansas ",
                                                                                                  " Moreno Valley, California ",
                                                                                                  " Boise, Idaho ",
                                                                                                  " Alexandria, Virginia ",
                                                                                                  " Providence, Rhode Island ",
                                                                                                  " Grand Prairie, Texas ",
                                                                                                  " Newport News, Virginia ",
                                                                                                  " Clarksville, Tennessee ",
                                                                                                  " Wichita Falls, Texas ",
                                                                                                  " Springfield, Missouri ",
                                                                                                  " Huntington, West Virginia ",
                                                                                                  " Oceanside, California ",
                                                                                                  " Garden Grove, California ",
                                                                                                  " Santa Rosa, California ",
                                                                                                  " Santa Clarita, California ",
                                                                                                  " Fort Lauderdale, Florida ",
                                                                                                  " Rancho Cucamonga, California ",
                                                                                                  " Port St.  Lucie, Florida ",
                                                                                                  " Ontario, California ",
                                                                                                  " Tempe, Arizona ",
                                                                                                  " Vancouver, Washington ",
                                                                                                  " Cape Coral, Florida ",
                                                                                                  " Sioux Falls, South Dakota ",
                                                                                                  " Peoria, Arizona ",
                                                                                                  " Eugene, Oregon ",
                                                                                                  " Lancaster, California ",
                                                                                                  " Hayward, California ",
                                                                                                  " Salinas, California ",
                                                                                                  " Palmdale, California ",
                                                                                                  " Pomona, California ",
                                                                                                  " Pasadena, Texas ",
                                                                                                  " Joliet, Illinois ",
                                                                                                  " Paterson, New Jersey ",
                                                                                                  " Kansas City, Kansas ",
                                                                                                  " Torrance, California ",
                                                                                                  " Syracuse, New York ",
                                                                                                  " Bridgeport, Connecticut ",
                                                                                                  " Hayward, Wisconsin ",
                                                                                                  " Fort Collins, Colorado ",
                                                                                                  " Escondido, California ",
                                                                                                  " Lakewood, Colorado ",
                                                                                                  " Naperville, Illinois ",
                                                                                                  " Dayton, Ohio ",
                                                                                                  " Hollywood, Florida ",
                                                                                                  " Sunnyvale, California ",
                                                                                                  " Alexandria, Louisiana ",
                                                                                                  " Mesquite, Texas ",
                                                                                                  " Savannah, Georgia ",
                                                                                                  " Cary, North Carolina ",
                                                                                                  " Fullerton, California ",
                                                                                                  " Warren, Michigan ",
                                                                                                  " Clarksville, Indiana ",
                                                                                                  " McAllen, Texas ",
                                                                                                  " New Haven, Connecticut ",
                                                                                                  " Sterling Heights, Michigan ",
                                                                                                  " West Valley City, Utah ",
                                                                                                  " Columbia, South Carolina ",
                                                                                                  " Killeen, Texas ",
                                                                                                  " Topeka, Kansas ",
                                                                                                  " Thousand Oaks, California ",
                                                                                                  " Cedar Rapids, Iowa ",
                                                                                                  " Olathe, Kansas ",
                                                                                                  " Elizabeth, New Jersey ",
                                                                                                  " Waco, Texas ",
                                                                                                  " Hartford, Connecticut ",
                                                                                                  " Visalia, California ",
                                                                                                  " Gainesville, Florida ",
                                                                                                  " Simi Valley, California ",
                                                                                                  " Stamford, Connecticut ",
                                                                                                  " Bellevue, Washington ",
                                                                                                  " Concord, California ",
                                                                                                  " Miramar, Florida ",
                                                                                                  " Coral Springs, Florida ",
                                                                                                  " Lafayette, Louisiana ",
                                                                                                  " Charleston, South Carolina ",
                                                                                                  " Carrollton, Texas ",
                                                                                                  " Roseville, California ",
                                                                                                  " Thornton, Colorado ",
                                                                                                  " Beaumont, Texas ",
                                                                                                  " Allentown, Pennsylvania ",
                                                                                                  " Surprise, Arizona ",
                                                                                                  " Evansville, Indiana",
                                                                                                  "Alabama",
                                                                                                  "Alaska",
                                                                                                  "Arizona",
                                                                                                  "Arkansas",
                                                                                                  "California",
                                                                                                  "Colorado",
                                                                                                  "Connecticut",
                                                                                                  "Delaware",
                                                                                                  "District of Columbia",
                                                                                                  "Florida",
                                                                                                  "Georgia",
                                                                                                  "Hawaii",
                                                                                                  "Idaho",
                                                                                                  "Illinois",
                                                                                                  "Indiana",
                                                                                                  "Iowa",
                                                                                                  "Kansas",
                                                                                                  "Kentucky",
                                                                                                  "Louisiana",
                                                                                                  "Maine",
                                                                                                  "Montana",
                                                                                                  "Nebraska",
                                                                                                  "Nevada",
                                                                                                  "New Hampshire",
                                                                                                  "New Jersey",
                                                                                                  "New Mexico",
                                                                                                  "New York",
                                                                                                  "North Carolina",
                                                                                                  "North Dakota",
                                                                                                  "Ohio",
                                                                                                  "Oklahoma",
                                                                                                  "Oregon",
                                                                                                  "Maryland",
                                                                                                  "Massachusetts",
                                                                                                  "Michigan",
                                                                                                  "Minnesota",
                                                                                                  "Mississippi",
                                                                                                  "Missouri",
                                                                                                  "Pennsylvania",
                                                                                                  "Rhode Island",
                                                                                                  "South Carolina",
                                                                                                  "South Dakota",
                                                                                                  "Tennessee",
                                                                                                  "Texas",
                                                                                                  "Utah",
                                                                                                  "Vermont",
                                                                                                  "Virginia",
                                                                                                  "Washington",
                                                                                                  "West Virginia",
                                                                                                  "Wisconsin",
                                                                                                  "Wyoming",),
                        key="locationPreference")

                    st.markdown("""
                                    <style>
                                        .st-au {
                                        border-radius:30px; 
                                        }
                                     div[data-testid="stForm"] {border: 0px}
    
                                    </style>""", unsafe_allow_html=True)

                    col1a, col2a, col3a = st.columns([1.1, 1, 1])
                    with col1a:
                        st.write("")
                    with col2a:
                        st.subheader("")
                        Search = st.form_submit_button("Take me to 19th Street")
                    with col3a:
                        st.write("")

                    if Search:
                        if ExperienceLevel is not None and Search:

                            st.markdown("""
                                            <style>
                                             div[data-testid="stForm"]  {
                                                visibility: hidden;
                                                height: 0%;
                                                opacity:0;
                                                }
                                                
                                                
                                             div[data-baseweb="select"] {
                                                visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
                                                
                                                button[kind ="secondaryFormSubmit]{
                                                visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
                                                .row-widget.stTextInput.css-pb6fr7.edfmue0 {
                                                visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
                                                
                                                .css-17z41qg.e16nr0p34{
                                                 visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
        
                                                .css-17z41qg.e16nr0p34{
                                                 visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
        
                                                .css-17z41qg.e16nr0p34{
                                                 visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
                                                .css-1db87p3.edgvbvh10{
                                                 visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
                                                div[class="row-widget stSelectbox"] {
                                                visibility: hidden;
                                                height: 0%;
                                                position: fixed;
                                                }
        
        
                                            </style>
                                                """, unsafe_allow_html=True)

                            NameHolder.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{Name}</h2>",
                                                unsafe_allow_html=True)

                            # progressText.markdown(
                            #     f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Looking for jobs where you can use your experience in {st.session_state['newSkills']} etc...</h6>",
                            #     unsafe_allow_html=True)
                            # links1 = run_selenium1(f"{FreshJobTitles[0].replace(' ', '-')}-{ExperienceLevel}", f"{FreshSkills[0].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
                            # my_bar.progress(25, text=f"")
                            #
                            # links2 = run_selenium1(f"{FreshJobTitles[1].replace(' ', '-')}-{ExperienceLevel}", f"{FreshSkills[1].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
                            # my_bar.progress(50, text=f"")
                            # progressText.markdown(
                            #     f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Hang tight! We're scanning for opportunities that match your unique set of {st.session_state['softSkills']}</h6>",
                            #     unsafe_allow_html=True)
                            #
                            # links3 = run_selenium1(f"{FreshJobTitles[2].replace(' ', '-')}-{ExperienceLevel}", f"{FreshSkills[2].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
                            # my_bar.progress(75, text=f"")
                            # progressText.markdown(
                            #     f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'> Hold tight, big dawg 🐶</h6>",
                            #     unsafe_allow_html=True)
                            #
                            #
                            # links4 = run_selenium1(f"{FreshJobTitles[3].replace(' ', '-')}-{ExperienceLevel}", f"{FreshSkills[3].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
                            # my_bar.progress(90, text=f"")
                            # progressText.markdown(
                            #     f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'> Doing one last search...</h6>",
                            #     unsafe_allow_html=True)
                            #
                            #
                            # links5 = run_selenium1(f"{FreshJobTitles[4].replace(' ', '-')}-{ExperienceLevel}", f"{FreshSkills[4].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))                    #
                            # my_bar.progress(100, text=f"")



                            def progress_shit():
                                st.markdown("""
                                <style>
                                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld5 > div.block-container.css-k1ih3n.egzxvld4 > div:nth-child(1) > div > div:nth-child(11) > div.css-keje6w.e1tzin5v2 > div:nth-child(1) > div > div:nth-child(11) > div > div.st-b8 > div > div > div{
                                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                                animation: gradient 5s ease infinite;
                                }
                                
                                @keyframes gradient {
                                0% {
                                background-position: 0% 50%;
                                }
                                50% {
                                background-position: 100% 50%;
                                }
                                100% {
                                background-position: 0% 50%;
                                }
                                }
                                </style>
                                """, unsafe_allow_html=True)

                                progressText.markdown( f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Looking for jobs where you can use your experience in {st.session_state['newSkills']} etc...</h6>", unsafe_allow_html=True)
                                my_bar.progress(25, text=f"")
                                time.sleep(10)

                                progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Hang tight! We're scanning for opportunities that match your unique set of {st.session_state['softSkills']}</h6>", unsafe_allow_html=True)
                                my_bar.progress(40, text=f"")
                                time.sleep(8)

                                progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Hold tight, big dawg...🐶</h6>",unsafe_allow_html=True)
                                my_bar.progress(60, text=f"")
                                time.sleep(10)

                                progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Generating Compatibility Scores 💯</h6>",unsafe_allow_html=True)
                                my_bar.progress(80, text=f"")
                                time.sleep(6)

                                progressText.markdown(f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Doing one last search...</h6>",unsafe_allow_html=True)
                                my_bar.progress(90, text=f"")
                            try:
                                with ThreadPoolExecutor(max_workers=6) as executor:
                                    future1 = executor.submit(run_selenium1, f"{FreshJobTitles[0].replace(' ', '-')}-{ExperienceLevel}",f"{FreshSkills[0].replace(' ', '_')}", f"{undesired},Deloitte", 1,
                                                              resumeContent, locationpreference.replace(' ', '_'))
                                    future2 = executor.submit(run_selenium1,
                                                              f"{FreshJobTitles[1].replace(' ', '-')}-{ExperienceLevel}",
                                                              f"{FreshSkills[1].replace(' ', '_')}", f"{undesired},Deloitte", 1,
                                                              resumeContent, locationpreference.replace(' ', '_'))
                                    future3 = executor.submit(run_selenium1,
                                                              f"{FreshJobTitles[2].replace(' ', '-')}-{ExperienceLevel}",
                                                              f"{FreshSkills[2].replace(' ', '_')}", f"{undesired},Deloitte", 1,
                                                              resumeContent, locationpreference.replace(' ', '_'))
                                    future4 = executor.submit(run_selenium1,
                                                              f"{FreshJobTitles[3].replace(' ', '-')}-{ExperienceLevel}",
                                                              f"{FreshSkills[3].replace(' ', '_')}", f"{undesired},Deloitte", 1,
                                                              resumeContent, locationpreference.replace(' ', '_'))
                                    future5 = executor.submit(run_selenium1,
                                                              f"{FreshJobTitles[4].replace(' ', '-')}-{ExperienceLevel}",
                                                              f"{FreshSkills[4].replace(' ', '_')}", f"{undesired},Deloitte", 1,
                                                              resumeContent, locationpreference.replace(' ', '_'))

                                    future6 = executor.submit(progress_shit())
                            except:
                                st.experimental_rerun()

                            executor.shutdown(wait=True)
                            links1 = future1.result()
                            links2 = future2.result()
                            links3 = future3.result()
                            links4 = future4.result()
                            links5 = future5.result()


                            executor.shutdown(wait=True)

                            print(threading.enumerate())

                            st.session_state["FinalResults"] = links1 + links2 + links3 + links4 + links5
                            Archives = links1 + links2 + links3 + links4 + links5

                            # for job in Archives:
                            #     firebase = pyrebase.initialize_app(firebaseconfig)
                            #     db = firebase.database()
                            #     link = job[0]
                            #     title = job[1]
                            #     companyName = job[2]
                            #     location = job[5]
                            #     data = {
                            #         "Link": str(link),
                            #         "Title": str(title),
                            #         "Company Name": str(companyName),
                            #         "Location": str(location),
                            #     }
                            #
                            #     db.child("users").child(str(localId)).child("Archive").push(data)
                            # st.subheader(datetime.datetime.now())


                            switch_page("results")
        with colmain3:
            st.write("")





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

                    div[data-testid="stSidebarNav"] {
                    height: 0%;
                    position: fixed;
                    }



                    .css-13e20ss{
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }

                    div[class="stException"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }

                  </style>
                  """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

def set_code(code: str):
    st.experimental_set_query_params(code=code)


col1form, col2form, col3form = st.columns([0.25, 1, 0.25])
with col1form:
    st.write("")
with col2form:
    def login_form(auth):
        email = st.text_input(
            label="email", placeholder="fullname@gmail.com")
        password = st.text_input(
            label="password", placeholder="password", type="password")

        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['user'] = user
                st.experimental_rerun()
            except requests.HTTPError as exception:
                st.write(exception)
        if st.button("Forgot Password", key="forgotpassword"):
            auth.send_password_reset_email("email")


    def Signup_form(auth):
        email = st.text_input(
            label="email", placeholder="fullname@gmail.com")
        password = st.text_input(
            label="password", placeholder="password", type="password")

        if st.button("login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['user'] = user
                st.experimental_rerun()
            except requests.HTTPError as exception:
                st.write(exception)
        if st.button("Forgot Password", key="forgotpassword"):
            auth.send_password_reset_email("email")

with col3form:
    st.write("")


def logout():
    del st.session_state['user']
    st.experimental_set_query_params(code="/logout")


def get_user_token(auth, refreshToken: object):
    user = auth.get_account_info(refreshToken['idToken'])

    user = {
        "email": user['users'][0]['email'],
        "refreshToken": refreshToken['refreshToken'],
        "idToken": refreshToken['idToken']
    }

    st.session_state['user'] = user

    return user


def refresh_session_token(auth, code: str):
    try:
        return auth.refresh(code)
    except:
        return "fail to refresh"


firebase = pyrebase.initialize_app(firebaseconfig)

auth = firebase.auth()

# authentification
if "user" not in st.session_state:
    st.session_state['user'] = None

if st.session_state['user'] is None:
    try:
        # code = st.experimental_get_query_params()['code'][0]
        code = cookie_manager.get(cookie="userCookie")
        refreshToken = refresh_session_token(auth=auth, code=code)

        if refreshToken == 'fail to refresh':
            raise (ValueError)

        user = get_user_token(auth, refreshToken=refreshToken)

        main(user=user)
    except:
        st.title("Login")
        login_form(auth)

else:
    main(user=st.session_state['user'])