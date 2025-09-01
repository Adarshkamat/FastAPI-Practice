from supabase import create_client
from fastapi import Request

from supabase import create_client

db=create_client("https://puubbqnwcmjsmvgpnqsc.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB1dWJicW53Y21qc212Z3BucXNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYyNzU2MDQsImV4cCI6MjA3MTg1MTYwNH0.BIzjRbWSDsH3qzVPm6QhVzWrzshclrWhu0Or0D5aXHU")



def get_loggedin_user(request: Request):
    token = request.cookies.get('user_session')
    result = db.auth.get_user(token)
    if result:
        return result.user
    return None