from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from models import Sightseeing
router = APIRouter(tags=["Events"])


@router.get('/events/{event_id}')
async def current_event_get(event_id: int, session: Session = Depends(get_db)):
    event = session.execute(select(Sightseeing)).scalar()
    return {"event": event}