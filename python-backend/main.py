from fastapi import FastAPI, Request, status, Depends
import json
from MainRouter import router as main_router
from EventsRouter import router as events_router
app = FastAPI(title="SMOLATOUR")
app.include_router(main_router)
app.include_router(events_router)

