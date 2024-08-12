import streamlit as st
st.header("My webapp")
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
