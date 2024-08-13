import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn

url_data = "https://raw.githubusercontent.com/jsaraviadrago/data-runner/main/Activities_07082024_VF.csv"

data_runs = pd.read_csv(url_data)

st.header("Mis carreras")

st.write("Este es mi dashboard sobre mis carreras y las métricas que me interesan cuando corro")
#x = st.slider("Select a value")
#st.write(x, "squared is", x * x)


st.header("Histórico de carreras y sus distancias")
st.line_chart(data_runs,
              x = 'Date',
              y= 'Distance')

st.header("Histórico de promedio de pulso")
st.line_chart(data_runs,
              x = 'Date',
              y= 'Avg HR')

st.header("Relación entre promedio de pulsaciones y distancia")
st.scatter_chart(data_runs,
                 x = "Avg HR",
                 y = "Distance")

