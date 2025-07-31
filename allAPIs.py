# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse
# import sqlite3

# app=FastAPI()
# def get_db():
#     conn = sqlite3.connect("databaseSQL")
#     return conn 

# @app.post("/user")
# def add_user(name,username,password,course_id:int):
#     try:
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("insert into users (name,username,password,course_id) values (?,?,?,?)",(name,username,password,course_id))
#         user_id =  cursor.lastrowid
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"The user is added successfully",
#             "user_id": f"{user_id} : User id of {name}"
#         })
#     except Exception :
#         print("There's been an error in adding the user")

# @app.get("/getusers")
# def get_users():
#     try:
#         conn=get_db()
#         cursor=conn.cursor()
#         cursor.execute("select * from users")
#         users=cursor.fetchall()
#         result=[]
#         for user in users :
#             result.append(list(user))
#         return result
#     except Exception :
#         print("There's been an error displayind the message ")

# @app.get("/getusers/{user_id}")
# def get_user(user_id):
#     try :
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("select * from users where id = ?",(user_id,))
#         user = cursor.fetchone()
#         return list(user)
#     except Exception :
#         print("There's been an error ")

# @app.put('/updateuser/password/{user_id}')
# def new_pass(user_id,password):
#     try:
#         conn = get_db()
#         cursor=conn.cursor()
#         cursor.execute("update users set password = ? where id = ?",(password,user_id))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"users password updated Succesfully",
#             "new_password":password
            
#         })
#     except Exception :
#         print("There's been an error")

# @app.put('/updateuser/username/{user_id}')
# def new_pass(user_id,username):
#     try:
#         conn = get_db()
#         cursor=conn.cursor()
#         cursor.execute("update users set username = ? where id = ?",(username,user_id))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"users password updated Succesfully",
#             "new_username":username
            
#         })
#     except Exception :
#         print("There's been an error")

# @app.put('/updateuser/course/{user_id}')
# def new_pass(user_id,course):
#     try:
#         conn = get_db()
#         cursor=conn.cursor()
#         cursor.execute("update users set course_id = ? where id = ?",(course,user_id))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"users password updated Succesfully",
#             "new_course":course
            
#         })
#     except Exception :
#         print("There's been an error")

# @app.delete("/deleteuser/{user}")
# def del_user(user):
#     try :
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("delete from users where id = ?",(user,))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"User Deleted ",
        
#         })
#     except Exception :
#         print("Theres been an error ")



# def get_db():
#     conn=sqlite3.connect("database")
#     return conn

# @app.post("/users")
# def create_user(name,username,password,course_id):
#     course_id=int(course_id)
#     try:
#         conn=get_db()
#         cursor=conn.cursor()
#         cursor.execute("INSERT INTO users(name,username,password,course_id) VALUES(?,?,?,?)",(name,username,password,course_id))
#         user_id=cursor.lastrowid
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"successfully created user",
#             "user_id":user_id
#         })
#     except Exception as e:
#         print("Something went wrong while execution")

# @app.get("/users")
# def all_users():
#     conn=get_db()
#     cursor=conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     users=cursor.fetchall()
#     cursor.close()
#     result=[]
#     for user in users:
#         result.append(list(user))
#     return result

# @app.put("/users/{user_id}")
# def update_user_password(user_id,password):
#     conn=get_db()
#     cursor=conn.cursor() 
#     cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
#     if not cursor.fetchone():
#         conn.close()
#         return JSONResponse(content={
#             "message":f"user with id-{user_id} was not found"
#         })    
#     if password:
#         cursor.execute("UPDATE users SET password=? WHERE id=?",(password,user_id))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":f"UPDATED successfully for user-{user_id}"
#         }) 
    
# @app.delete("/users/{user_id}")
# def delete_user(user_id):
#         conn=get_db()
#         cursor=conn.cursor()
#         cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
#         if cursor.rowcount==0:
#             raise HTTPException(status_code=404,detail="User not found to delete")
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":f"Successfully deleted the user-{user_id}"
#         })


# #----courses----
# @app.post("/courses")
# def create_course(name,duration):
#     try:
#         conn=get_db()
#         cursor=conn.cursor()
#         cursor.execute("INSERT INTO courses(name,duration) VALUES(?,?)",(name,duration))
#         course_id=cursor.lastrowid
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":"successfully created user",
#             "user_id":course_id
#         })
#     except Exception as e:
#         print("Something went wrong while execution")


# @app.get("/courses")
# def all_courses():
#     conn=get_db()
#     cursor=conn.cursor()
#     cursor.execute("SELECT * FROM courses")
#     courses=cursor.fetchall()
#     cursor.close()
#     result=[]
#     for course in courses:
#         result.append(list(course))
#     return result

# @app.put("/courses/{course_id}")
# def update_user_password(course_id,duration):
#     conn=get_db()
#     cursor=conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE id=?",(course_id,))
#     if not cursor.fetchone():
#         conn.close()
#         return JSONResponse(content={
#             "message":f"couse with id-{course_id} was not found"
#         })    
#     if duration:
#         cursor.execute("UPDATE courses SET duration=? WHERE id=?",(duration,course_id))
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":f"UPDATED successfully for course-{course_id}"
#         })

# @app.delete("/courses/{course_id}")
# def delete_user(course_id):
#         conn=get_db()
#         cursor=conn.cursor()
#         cursor.execute("DELETE FROM courses WHERE id=?",(course_id,))
#         if cursor.rowcount==0:
#             raise HTTPException(status_code=404,detail="course not found to delete")
#         conn.commit()
#         conn.close()
#         return JSONResponse(content={
#             "message":f"Successfully deleted the course-{course_id}"
#         })
