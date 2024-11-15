import streamlit as st 
import numpy as np 
import pandas as pd
# import streamlit as st
import streamlit_pydantic as sp
from pydantic import BaseModel
import re
class ExampleModel(BaseModel):
    product_name: str
    Quantity: int
    # Submit: bool

def function(corpus , s):
    l=[]
    for word in corpus:
        if s in word:
            l.append(word)
    return l

@st.cache
def email(s):
    pass
# data = {}

corpus = ["paracetamol" , 'dolo', "cough syrup", "cotton buds", "bandages", "syringes"]

try :
    st.title("PILLSWIFT ADARSH")
    tab1 , tab2 ,tab3 = st.tabs(["Intro" , "Buy","Choose"])

    with tab1 :
        # st.image(["medicines.jpg"],width =300,caption =["medicines"])
        pass

    with tab2 :
        # data = sp.pydantic_form(key="my_sample_form", model=ExampleModel)
        search = st.text_input("Search here . . .")
        if search :
            l = function(corpus,search)
            if l:
                st.write("You must be looking for :" , l)
    with tab3:
        options = st.multiselect("Choose products :",corpus)
        st.write(options)
        
except Exception as e :
    print(e)
    raise e