from streamlit_option_menu import option_menu
import streamlit as st
import requests
import PyPDF2
import openai
from PIL import Image
from st_btn_select import st_btn_select
import datetime
import extra_streamlit_components as stx
from streamlit_extras.switch_page_button import switch_page
import psutil
from streamlit.components.v1 import html
import pyrebase




import datetime
st.write("# Cookie Manager")

@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()

st.subheader("All Cookies:")
cookies = cookie_manager.get_all()
st.write(cookies)

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Get Cookie:")
    cookie = st.text_input("Cookie", key="0")
    clicked = st.button("Get")
    if clicked:
        value = cookie_manager.get(cookie=cookie)
        st.write(value)
with c2:
    st.subheader("Set Cookie:")
    cookie = st.text_input("Cookie", key="1")
    val = st.text_input("Value")
    if st.button("Add"):
        cookie_manager.set(cookie, val, expires_at=datetime.datetime(year=2022, month=2, day=2))
with c3:
    st.subheader("Delete Cookie:")
    cookie = st.text_input("Cookie", key="2")
    if st.button("Delete"):
        cookie_manager.delete(cookie)