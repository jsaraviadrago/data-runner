import streamlit as st
import pandas as pd
import numpy as np

url = ""

data_runs = pd.read_csv("")


st.header("My webapp")
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

