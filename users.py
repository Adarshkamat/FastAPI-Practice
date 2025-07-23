from fastapi import Body, FastAPI
import json

# /user/add
# /password/update?username=existing_username
# /user/delete?username=existing_username
# /user/all -> shd return all users
# /user?username=existing_username -> specific username & passwoird

# app = FastAPI()
 
# def load_json_db():
#     #open file and return data
#     with open("database.json", 'r') as f:
#         return json.load(f)
   
 
# def save_json_db(user_details):
#     with open('database.json', 'w') as f:
#         json.dump(user_details, f)
 
# @app.post('/save')
# def users(details: dict = Body(...)):
#     all_users = load_json_db()
#     all_users.append({ details.get('username') : details.get('password')})
#     save_json_db(all_users)
#     # print(all_users)
#     all_users = load_json_db()
#     return all_users

from fastapi import Body, FastAPI, HTTPException
import json
import os

app = FastAPI()

DB_FILE = "database.json"

# Ensure JSON file exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump([], f)

def load_json_db():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_json_db(user_details):
    with open(DB_FILE, 'w') as f:
        json.dump(user_details, f, indent=4)


# Original /save (same as /user/add)
@app.post('/user/add')
def add_user(details: dict = Body(...)):
    all_users = load_json_db()
    username = details.get('username')
    password = details.get('password')

    # Check if user already exists
    for user in all_users:
        if username in user:
            raise HTTPException(status_code=400, detail="Username already exists")

    all_users.append({username: password})
    save_json_db(all_users)
    return {"message": "User added successfully", "data": all_users}


# /password/update?username=existing_username
@app.put('/password/update')
def update_password(username: str, new_password: str = Body(...)):
    all_users = load_json_db()
    user_found = False

    for user in all_users:
        if username in user:
            user[username] = new_password
            user_found = True
            break

    if not user_found:
        raise HTTPException(status_code=404, detail="Username not found")

    save_json_db(all_users)
    return {"message": f"Password updated for {username}"}


# /user/delete?username=existing_username
@app.delete('/user/delete')
def delete_user(username: str):
    all_users = load_json_db()
    initial_len = len(all_users)

    # Remove user dict from list
    all_users = [user for user in all_users if username not in user]

    if len(all_users) == initial_len:
        raise HTTPException(status_code=404, detail="Username not found")

    save_json_db(all_users)
    return {"message": f"User {username} deleted successfully"}


# /user/all -> returns all users
@app.get('/user/all')
def get_all_users():
    return load_json_db()


# /user?username=existing_username
@app.get('/user')
def get_user(username: str):
    all_users = load_json_db()
    for user in all_users:
        if username in user:
            return {username: user[username]}
    raise HTTPException(status_code=404, detail="Username not found")
