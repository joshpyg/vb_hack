import streamlit as st
import pandas as pd
import numpy as np

number1 = st.number_input(
    "Enter the first number", value=None, placeholder = "Type a number..."
)
number2 = st.number_input(
    "Enter the first number", value=None, placeholder = "Type a number..."
)
operation = st.selectbox(
    "choose an oeration",
    ["Add", "Subtract", "Multiply", "Divide"]
)
if number1 is not None and number2 is not None:

    if operation == "Add":
        answer = number1 + number2

    elif operation == "Subtract":
        answer = number1 - number2

    elif operation == "Multiply":
        answer = number1 * number2

    elif operation == "Divide":
        answer = number1 / number2

    st.write("Answer:", answer)