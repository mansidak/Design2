import os
import random
import gc
import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re
import threading
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import PyPDF2
from docx import Document
import openai
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import psutil
from streamlit.components.v1 import html

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

    st.set_page_config(page_title="19th Street", page_icon='⓵⓽',
                       initial_sidebar_state='collapsed')
    # print(threading.enumerate())
    # st.write(threading.enumerate())


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
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
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

    footer = """<style>
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

    progress_text = "See your search progress here."
    progress_text_2 = "Hola"

    hide_menu_style = """
            <style>
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
                st.write(f"https://search.linkup.com/search/results/{jobTitle}-jobs?all={skill1}&none={undesired}&location={locationpreference}&pageNum={pageNumber}")
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
            except:
                driver.close()
                driver.quit()
        return links


    @st.cache(show_spinner=False)
    def get_links(i, skill1, resumeContent):
        Final_Array = []
        Final_Links = []
        Final_Titles = []
        Final_Company = []
        Final_Description = []
        Final_Location = []
        shortened_summary = []
        Final_Skills = []
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(i)
            # time.sleep(2)
            elements = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[1]/a")
            for a in elements:
                if str(a.get_attribute('href')).startswith("https://out.linkup.com/") and a.get_attribute(
                        'href') not in Final_Links:
                    Final_Links.append(a.get_attribute('href'))
            title = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[2]/div[1]/h2").text
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

            for links, titles, companies, summaries, descriptions, locations, skills in zip(Final_Links,
                                                                                            Final_Titles,
                                                                                            Final_Company,
                                                                                            shortened_summary,
                                                                                            Final_Description,
                                                                                            Final_Location,
                                                                                            Final_Skills):
                Final_Array.append((links, titles, companies, summaries, descriptions, locations, skills))

            driver.close()
            driver.quit()
        except:
            driver.close()
            driver.quit()
        return Final_Array


    @st.cache(show_spinner=False)
    def openAIGetRelevantJobTitles(resumeContent):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"The following is the data from the resume of a job seeker. \n\n{resumeContent}\n\nTheir full name is: \n",
            temperature=0.7,
            max_tokens=146,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        Name = response["choices"][0]["text"]
        return Name

    @st.cache(show_spinner=False)
    def openAIGetRelevantJobTitlesDuplicate(resumeContent):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"The following is the data from the resume of a job seeker. I want you to do four things:\n\n\n{resumeContent}\n\n\n1. In addition to what they've already done, what other jobs titles would they like to pursue? List 3 and separate them by commas.\n2. If you were to choose only top six strongest technical skills of this person, what would those six be? Only list skills this person has given description about.\n3. Their Full Name \n4.Their top 3 soft skills\n5. Now list every single technical skills they've used in the past. Separate them by commas. \n",
            temperature=0.7,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        Titles = response["choices"][0]["text"]
        print(Titles)
        Jobtitles = Titles.split('1.')[1].split('2.')[0].split(',')
        Skills = Titles.split('2.')[1].split('3.')[0].split(',')
        Name = Titles.split('3.')[1].split('4.')[0]
        softSkills = Titles.split('4.')[1].split('5.')[0]
        OldSkills = Titles.split('5.')[1]

        newJobtitles = [item.replace(" ", "-") for item in Jobtitles]
        newSkills = [re.sub(r'\s+', '-', item) for item in Skills]

        return Name, newJobtitles, newSkills, softSkills, OldSkills


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


    # @st.cache(show_spinner=False)
    def extract_text_from_pdf(pdf_file):
        pdfReader = PyPDF2.PdfReader(pdf_file)
        txtFile = open('sample.txt', 'w')
        num_pages = len(pdfReader.pages)
        for page_num in range(num_pages):
            pageObj = pdfReader.pages[page_num]
            txtFile.write(pageObj.extract_text())
            resumeContent = pageObj.extract_text()
        return resumeContent


    if ResumePDF is not None:
        SubTitle.empty()
        Credits.empty()
        holder.empty()
        resumeContent = extract_text_from_pdf(ResumePDF)
        Name = openAIGetRelevantJobTitles(resumeContent)

        if 'Name' not in st.session_state:
            st.session_state['Name'] = Name
        if 'resumeContent' not in st.session_state:
            st.session_state["resumeContent"] = resumeContent
        NameHolder.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{Name}</h2>",
                            unsafe_allow_html=True)
        if 'newSkills' not in st.session_state:
            NameDuplicate, newJobtitles, newSkillsall, softSkills, OldSkillsBullet = openAIGetRelevantJobTitlesDuplicate(resumeContent)
            st.session_state['newJobtitles'] = newJobtitles
            st.session_state['newSkillsall'] = newSkillsall
            newSkills = random.sample(newSkillsall, 3)
            st.session_state['newSkills'] = newSkills
            st.session_state['softSkills'] = softSkills
            st.session_state['OldSkillsBullet'] = OldSkillsBullet
        newSkillsall = st.session_state['newSkillsall']
        newSkills = random.sample(newSkillsall,3)
        newJobtitles = st.session_state['newJobtitles']
        OldSkillsBullet = st.session_state['OldSkillsBullet']
        softSkills = st.session_state['softSkills']
        st.write(newSkillsall)
        st.write(newSkills)
        st.write(newJobtitles)
        holder2 = st.empty()
        ExperienceLevel = holder2.selectbox(
            'Select Experience Level*',
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
            'Location Preferences, if any (This might limit your search results. We )', ("",
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
                                          " Evansville, Indiana","Alabama",
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
                                             "Wyoming",), key="locationPreference")

        st.markdown("""
        <style>
            .st-au {
            border-radius:30px; 
            }
        </style>""", unsafe_allow_html=True)

        col1a, col2a, col3a = st.columns([1, 1, 1])
        with col1a:
            st.write("")
        with col2a:
            Search = st.button("Take me to 19th Street", key="SearchButton")
        with col3a:
            st.write("")

        if ExperienceLevel is not None and Search:


            st.markdown("""
            <style>
             div[data-baseweb="select"] {
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

            # SearchHolder.empty()
            NameHolder.markdown(f"<h2 style='text-align: center; font-family: Sans-Serif;'>Welcome,{Name}</h2>",unsafe_allow_html=True)
            DisplaySkills = ', '.join([item.replace('-', ' ') for item in newSkillsall])
            progressText.markdown(
                f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Looking for jobs where you can use your experience in {DisplaySkills}etc...</h6>",
                unsafe_allow_html=True)
            my_bar.progress(25, text=f"")

            links1 = run_selenium1(f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[0].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            links2 = run_selenium1(f"{newJobtitles[1]}-{ExperienceLevel}", f"{newSkills[1].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            links3 = run_selenium1(f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[2].replace(' ', '_')}", f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            st.write(links1)
            st.write(links2)
            st.write(links3)
            # with ThreadPoolExecutor(max_workers=3) as executor:
            #     future1 = executor.submit(run_selenium1, f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[0]}",
            #                               f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            #     future2 = executor.submit(run_selenium1, f"{newJobtitles[1]}-{ExperienceLevel}", f"{newSkills[1]}",
            #                               f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            #     future3 = executor.submit(run_selenium1, f"{newJobtitles[0]}-{ExperienceLevel}", f"{newSkills[2]}",
            #                               f"{undesired}", 1, resumeContent, locationpreference.replace(' ', '_'))
            # executor.shutdown(wait=True)
            #
            # # Get the results
            # links1 = future1.result()
            # links2 = future2.result()
            # links3 = future3.result()
            # executor.shutdown(wait=True)

            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(get_links, link, newSkills[0], resumeContent) for link in links1]
                result1 = [future.result() for future in futures]
                result11 = sum(result1, [])
            progressText.markdown(
                f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>You have some background in {softSkills}. We're looking for more jobs that match that...</h6>",
                unsafe_allow_html=True)
            my_bar.progress(50, text=f"")
            executor.shutdown(wait=True)

            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(get_links, link, newSkills[1], resumeContent) for link in links2]
                result2 = [future.result() for future in futures]
                result22 = sum(result2, [])
            progressText.markdown(
                f"<h6 style='text-align: center; font-family: Sans-Serif;font-weight: lighter;'>Hold tight! Doing one last search....</h6>",
                unsafe_allow_html=True)
            my_bar.progress(95, text=f"")
            executor.shutdown(wait=True)

            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(get_links, link, newSkills[2], resumeContent) for link in links3]
                result3 = [future.result() for future in futures]
                result33 = sum(result3, [])
            executor.shutdown(wait=True)

            print(threading.enumerate())
            st.write(threading.enumerate())

            st.session_state["FinalResults"] = result11 + result22 + result33
            executor.shutdown()
            switch_page("results")