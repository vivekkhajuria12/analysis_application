# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:21:36 2023

@author: vivek khajuria
"""

import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Data Analysis")
#st.subhead("data analysis using python and streamlit")

upload=st.file_uploader("Upload you data set in csv format")

if upload is not None:
    data=pd.read_csv(upload)


if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("head"):
            st.write(data.head())
        if st.button("tail"):
            st.write(data.tail())
    
    
if upload is not None:
    if st.checkbox("datatype of each column"):
        st.text("datatypes")
        st.write(data.dtypes)
    
    
if upload is not None:
    if st.checkbox("shape of your data"):
        st.text("shape is")
        st.write(data.shape)
        
        
        
if upload is not None:
    if st.checkbox("is there is any null value"):
        st.text("Null value  is")
        st.write(data.isnull().sum())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        