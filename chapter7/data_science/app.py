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
from agent import (
    # create_agent,
    DataAgent,
    # query_agent,
    query_agent_with_stream
)


def main():
    st.title("👨‍💻 Chat with your CSV")
    st.write("Please upload your CSV file below.")
    data_file = st.file_uploader("Upload a CSV")
    query = st.text_area("Insert your query")

    if st.button("Submit Query", type="primary"):
        # assert data_file is not None
        if data_file is None:
            st.warning("⚠️  Please upload a CSV file before submitting.")
            return
        # agent = create_agent(data_file.getvalue().decode())
        stringio = StringIO(data_file.getvalue().decode("utf-8"))
        agent = DataAgent(stringio)
        # response = query_agent(agent=agent, query=query)
        # st.write(response['output'])
        st.write(agent.df)
        events = query_agent_with_stream(agent=agent, query=query)
        for event in events:
            message = event.get('messages', [])[-1].content
            st.markdown(message)
        st.subheader("Output")
        st.write(event['output'])


if __name__ == "__main__":

    main()
