from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import sqlite3

app=FastAPI()
def get_db():
    conn = sqlite3.connect("databaseSQL")
    return conn 

@app.post("/user")
def add_user(name,username,password,course_id:int):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("insert into users (name,username,password,course_id) values (?,?,?,?)",(name,username,password,course_id))
        user_id =  cursor.lastrowid
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"The user is added successfully",
            "user_id": f"{user_id} : User id of {name}"
        })
    except Exception :
        print("There's been an error in adding the user")

@app.get("/getusers")
def get_users():
    try:
        conn=get_db()
        cursor=conn.cursor()
        cursor.execute("select * from users")
        users=cursor.fetchall()
        result=[]
        for user in users :
            result.append(list(user))
        return result
    except Exception :
        print("There's been an error displayind the message ")

@app.get("/getusers/{user_id}")
def get_user(user_id):
    try :
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("select * from users where id = ?",(user_id,))
        user = cursor.fetchone()
        return list(user)
    except Exception :
        print("There's been an error ")

@app.put('/updateuser/password/{user_id}')
def new_pass(user_id,password):
    try:
        conn = get_db()
        cursor=conn.cursor()
        cursor.execute("update users set password = ? where id = ?",(password,user_id))
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"users password updated Succesfully",
            "new_password":password
            
        })
    except Exception :
        print("There's been an error")

@app.put('/updateuser/username/{user_id}')
def new_pass(user_id,username):
    try:
        conn = get_db()
        cursor=conn.cursor()
        cursor.execute("update users set username = ? where id = ?",(username,user_id))
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"users password updated Succesfully",
            "new_username":username
            
        })
    except Exception :
        print("There's been an error")

@app.put('/updateuser/course/{user_id}')
def new_pass(user_id,course):
    try:
        conn = get_db()
        cursor=conn.cursor()
        cursor.execute("update users set course_id = ? where id = ?",(course,user_id))
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"users password updated Succesfully",
            "new_course":course
            
        })
    except Exception :
        print("There's been an error")

@app.delete("/deleteuser/{user}")
def del_user(user):
    try :
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("delete from users where id = ?",(user,))
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"User Deleted ",
        
        })
    except Exception :
        print("Theres been an error ")


# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------


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
