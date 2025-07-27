import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col_empty, col2 = st.columns([1.5,0.5,1.5])

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Gwaliwa Peter Mashaka")
    content = """
    Gwaliwa is software engineer and data scientist. 
    Graduated from University of Aberdeen. She currently works at UNICEF.
    Have BSc in Computer Engineering and IT
    """
    #st.write(content)
    st.info(content)

content2= """ Below are some apps i build on python feel free to contact me
    """
st.write(content2)

df = pd.read_csv("data.csv", sep=(";"))
col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(df["title"][index])
        st.write(row["description"])
        st.image("images/"+ row['image'])
        st.write(f"source: {row['url']}")

with col4:
    for index, row in df[10:].iterrows():
        st.header(df["title"][index])
        st.write(row["description"])
        st.image("images/"+ row['image'])
        st.write(f"source: {row['url']}")