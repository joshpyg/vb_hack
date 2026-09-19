import streamlit as st
import pandas as pd
import numpy as np

number = st.number_input(
    "Inert a number", value=None, placeholder="Type a number"
)
st.write("The current number is ", number)