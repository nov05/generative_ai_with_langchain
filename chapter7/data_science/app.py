"""
Streamlit app for data analysis.

Run like this:
$ PYTHONPATH=. streamlit run app.py

Refer to Chapter 7 Notebook 5: 
https://drive.google.com/file/d/1yfJCkgC5NqJlFA5P84vd9KBADM6_Rhqs  
"""
# Code updated by Nov05 on 2025-06-23

import streamlit as st
from io import StringIO
# Local imports
from agent import create_agent, query_agent


st.title("👨‍💻 Chat with your CSV")
st.write("Please upload your CSV file below.")
data_file = st.file_uploader("Upload a CSV")
query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):
    assert data_file is not None
    # agent = create_agent(data_file.getvalue().decode())  # Nov05
    # Nov05: Use StringIO for text-based file
    stringio = StringIO(data_file.getvalue().decode("utf-8"))
    agent = create_agent(
        stringio,
    )
    response = query_agent(agent=agent, query=query)
    st.write(response)
