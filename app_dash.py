import streamlit as st
from streamlit_embedcode import github_gist

st.title("Embedding Jupyter Notebook in Streamlit")

# Embed a Jupyter Notebook using a GitHub Gist URL
gist_url = "https://github.com/JoseRicoCct/Streamlit_Dash_Test.git"
github_gist(gist_url)