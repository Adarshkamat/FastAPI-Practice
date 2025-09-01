from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client
from utils import get_loggedin_user

db=create_client("https://puubbqnwcmjsmvgpnqsc.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB1dWJicW53Y21qc212Z3BucXNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYyNzU2MDQsImV4cCI6MjA3MTg1MTYwNH0.BIzjRbWSDsH3qzVPm6QhVzWrzshclrWhu0Or0D5aXHU")


templates = Jinja2Templates(directory = "templates")
router = APIRouter()

@router.get("/plans/new")
def form_plan(request:Request):
    user=get_loggedin_user(request)
    if user :
        return templates.TemplateResponse("new_plan.html",{"request":request})
    return RedirectResponse("/login")

@router.post("/plans/new")
def create_plan(request:Request,title=Form(...),days=Form(...),persons=Form(...),budget=Form(...),city=Form(...)):
    user=get_loggedin_user(request)
    if user:
        result=db.table("trawell").insert({"user":user.id,
                                          "title":title,
                                          "days":days,
                                          "person_count":persons,
                                          "budget":budget,
                                          "cities":city,
                                          "ai_plan":"nothing"}).execute()
    if result.data:
        return RedirectResponse(f"/plans/generate?plan_id={result.data[0]["id"]}",status_code=302)

@router.get("/plans/generate")
def show_plan(request:Request,plan_id):
    user = get_loggedin_user(request)
    if user:
        