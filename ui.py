import streamlit as st
import requests
 
#8501
st.title("User Management")
 
 
@st.dialog("Add User")
def new_user():
    course_id = -1
    name = st.text_input('Name', placeholder='Enter Name')
    username = st.text_input('Username', placeholder='Enter Username')
    password = st.text_input('Password', placeholder='Enter Password', type='password')
    course = st.selectbox("Select Course", ["1. Pet Grooming", "2. Cooking"])
    if course == '1. Pet Grooming':
        course_id = 1
    else:
        course_id = 2
    if st.button('Submit', use_container_width=True, type='primary'):
        #api call and save in db
        url = f"http://127.0.0.1:8000/user?name={name}&username={username}&password={password}&course_id={course_id}"
        res = requests.post(url)
        st.rerun()
 
def update_user_dialog(id):
    @st.dialog(f"Update Password for @{id}")
    def inner_dialog():
        new_password = st.text_input("New Password", placeholder="Enter new password", type="password")
        if st.button("Update Password", use_container_width=True, type="primary"):
              

            url = f'http://127.0.0.1:8000/updateuser/password/{id}?password={new_password}' 
            res = requests.put(url)
            st.rerun()
    inner_dialog()
response = requests.get("http://127.0.0.1:8000/getusers")
 
data = response.json()
 
new_user_btn = st.button("New User +", type='primary')
for user in data:
    with st.container(border=True):
        st.subheader(user[1])
        st.caption('@' + user[2])
        col1, col2 = st.columns(2)
        with col1:
                if st.button("Delete", key="del_"+user[2]):
                    requests.delete(f"http://127.0.0.1:8000/deleteuser/{user[0]}")
                    st.rerun()
        with col2:
                if st.button("Update", key="upd_"+user[2]):
                    update_user_dialog(user[0])
 
if new_user_btn:
    new_user()
# st.write(data)





































































# st.title("Calculator App (using FastAPI + Streamlit)")

# # Input Fields
# first = st.text_input("Enter First Number:")

# second = st.text_input("Enter Second Number:")
# first_num = int(first)
# second_num = int(second)
# operation = st.text_input("Enter Operation (add, subtract, multiply, divide):")
# url=f"http://127.0.0.1:8000/{operation}?first={first_num}&second={second_num}"
# response=requests.get(url)
# data=response.json()
# st.write(data)