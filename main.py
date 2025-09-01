from fastapi import FastAPI
from fastapi.responses import HTMLResponse , RedirectResponse ,JSONResponse
from src.routes.auth import router 
from src.routes.dashboard import router as r_dash
from src.routes.plans import router as r_plan
app = FastAPI()
app.include_router(router)
app.include_router(r_dash)
app.include_router(r_plan)