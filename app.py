# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:10:10 2021

@author: Tapiwa Chamboko  
"""

import streamlit as st 

header = st.container()
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with header:
    st.title("WELLNESS PHARMACY FOR TAPIWA CHAMBOKO CLOULD COMPUTING RESEARCH ")
    st.text("WELLNESS PHARMACY CLOULD COMPUTING FORM")

name = st.text_input("Enter your name, """)


job = st.text_input("Role at your current position?")


age = st.slider("Enter your age", min_value=10, max_value = 100 )
selected_element = st.selectbox("Select Department", ("Marketing Department","IT Department"))

if name != "":
    st.markdown(
    f""" 
    * Name : {name}
    * Job : {job}
    * Age : {age}
    """           
    )

col1, col2 = st.columns(2)
#with st.form(key = "form1"):
with col1:
     name2 = st.text_input("financial environment contexts")
     job2 = st.text_input("positive impacts of cloud systems")
     age2 = st.text_input("negative impacts of cloud systems")
     age3 = st.text_input("type of cloud computing used")
     numtime = st.slider("Time taken for setup (Months)", min_value=1, max_value = 100 )

     
with col2:
    name1 = st.text_input("security features of cloud computing")
    job1 = st.text_input("quality metrics of cloud computing")
    age1 = st.number_input("Enter operational time (hours)", min_value=0, max_value=100, step=1)
    age4 = st.text_input("Apps installed on the cloud")
    numtime2 = st.slider("Work-flow time redused by cloud computing ? (Hours)", min_value=1, max_value = 24 )

result = st.button("Click here to Submit")
if result:
    st.markdown(
        """
        ## Thank you for taking your valuable time to go through this questionnaire!
        """
        )










     
      
                                             
    