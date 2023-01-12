from operator import index
import streamlit as st
import pandas as pd
import os 

st.title("Dataset Uploading")
st.image("EDA.png", width= 500)
"""
st.write("you dont have data now...we got you. Download any of data for apporiate model and upload to test.")

with open('Data select\classification data.csv', 'rb') as f: 
                st.download_button('Regression sample data', f, file_name="regression.csv")
with open('Data select\data.csv', 'rb') as f: 
                st.download_button('Classifcation sample data', f, file_name="Classification.csv")
"""

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
file = st.file_uploader("Upload Your Dataset (CSV)")
try:
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)
        submit = st.button("Submit")
        if submit:
            if file is not None:
                st.session_state["my_input"]= df
                st.success("Sucessfully uploaded")
                st.write("Proceed to EDA")
            else:
                st.error("please select file to upload")
except:
    st.write("Only support CSV Files")
                

        
