import streamlit as st
import pandas as pd
import numpy as np

number = st.number_input(
    "Type a number", value=None, placeholder="Type a number"
)
st.write("The current number is ", number)

number2 = st.number_input(
    "Type a second number", value=None, placeholder="Type a number"
)
st.write("The current number is ", number)

if st.button("add"):
    st.write(number + number2)

if st.button("subtract"):
    st.write(number - number2)