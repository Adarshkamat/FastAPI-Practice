from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client
from utils import get_loggedin_user

db=create_client("https://puubbqnwcmjsmvgpnqsc.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB1dWJicW53Y21qc212Z3BucXNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYyNzU2MDQsImV4cCI6MjA3MTg1MTYwNH0.BIzjRbWSDsH3qzVPm6QhVzWrzshclrWhu0Or0D5aXHU")


templates = Jinja2Templates(directory = "templates")
router = APIRouter()


@router.get("/")
def home():
     return RedirectResponse("/signup")
@router.get("/signup")
def signup(request : Request):
     return templates.TemplateResponse("signup.html",{"request":request})

@router.post("/api/signup")
def signup(request : Request , email = Form(...),password= Form(...)):
    result=db.auth.sign_up({
        "email":email,
        "password":password}
    )
    if result.user:
        return "user created successfully"

@router.get("/login")
def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@router.post("/api/login")
def login(request:Request,email=Form(...),password=Form(...)):
    res=db.auth.sign_in_with_password(
        {
            "email":email,
            "password":password
        }
    )
    if res.user :
            response=RedirectResponse("/dashboard",status_code=302)
            response.set_cookie("user_session",res.session.access_token,max_age=3600,httponly=True)
            return response 
    
@router.get("/dashboard")
def dashboard(request:Request):
     user=get_loggedin_user(request)
     if user:
      return templates.TemplateResponse("dashboard.html",{"request":request})
     return RedirectResponse("/login")