import streamlit as st
import time

with open( "style1.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

time.sleep(2)
st.switch_page("pages/home.py")