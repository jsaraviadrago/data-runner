import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn

url_data = "https://raw.githubusercontent.com/jsaraviadrago/data-runner/main/Activities_07082024_VF.csv"

data_runs = pd.read_csv(url_data)

st.header("My webapp")
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

st.line_chart(data_runs,
              x = 'Date',
              y= 'Distance')

