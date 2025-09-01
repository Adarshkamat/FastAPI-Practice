from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client

db=create_client("https://puubbqnwcmjsmvgpnqsc.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB1dWJicW53Y21qc212Z3BucXNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYyNzU2MDQsImV4cCI6MjA3MTg1MTYwNH0.BIzjRbWSDsH3qzVPm6QhVzWrzshclrWhu0Or0D5aXHU")


templates = Jinja2Templates(directory = "templates")
router = APIRouter()
