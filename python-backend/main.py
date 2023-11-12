from fastapi import FastAPI, Request, status, Depends
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from MainRouter import router as main_router
from EventsRouter import router as events_router
from ExcursionRouter import router as excursion_router
from RoadRouter import router as road_router
app = FastAPI(title="SMOLATOUR")
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static/"), name="static")
app.mount("/static/assets", StaticFiles(directory="static/assets"), name="/static/assets")
app.include_router(main_router)
app.include_router(events_router)
app.include_router(road_router)
app.include_router(excursion_router)

