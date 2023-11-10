from fastapi import FastAPI, Request, status, Depends
import json
from fastapi.staticfiles import StaticFiles
from MainRouter import router as main_router
from EventsRouter import router as events_router
app = FastAPI(title="SMOLATOUR")
app.mount("/static", StaticFiles(directory="static/"), name="static")
app.mount("/static/assets", StaticFiles(directory="static/assets"), name="/static/assets")
app.include_router(main_router)
app.include_router(events_router)

