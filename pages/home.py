import streamlit as st

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

with c2:
    st.write("Hi")