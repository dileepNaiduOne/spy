import streamlit as st


from code.get_data import Get_Data

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

with c2:
    username = st.text_input(label="Reddit Username", placeholder="Type in the Reddit Username : ")
    texting_space = st.empty()
    with st.spinner("Extracting Data...."):
        reddits = Get_Data().get_reddits(username)
        if len(reddits) != 0:
            texting_space.write(reddits)

    

    