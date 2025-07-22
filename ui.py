import streamlit as st
import requests
st.title("Calculator App (using FastAPI + Streamlit)")

# Input Fields
first = st.text_input("Enter First Number:")

second = st.text_input("Enter Second Number:")
first_num = int(first)
second_num = int(second)
operation = st.text_input("Enter Operation (add, subtract, multiply, divide):")
url=f"http://127.0.0.1:8000/{operation}?first={first_num}&second={second_num}"
response=requests.get(url)
data=response.json()
st.write(data)