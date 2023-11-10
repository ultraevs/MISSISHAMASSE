from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Event
import datetime
router = APIRouter(tags=["Events"])


@router.get('/events/')
async def current_event_get(session: Session = Depends(get_db)):
    event = session.execute(select(Event).where(Event.datee==str(int(datetime.datetime.now().day + 1)))).scalars()
    return {"event": [i for i in event]}


@router.get('/initdb')
async def initdb(session: Session = Depends(get_db)):
    session.execute(insert(Event).values(name='TEST1', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', interes_sphere='IT', description='DESCRIPTION', datee='11'))
    session.execute(insert(Event).values(name='TEST2', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', interes_sphere='IT', description='DESCRIPTION', datee='11'))
    session.execute(insert(Event).values(name='TEST3', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', interes_sphere='IT', description='DESCRIPTION', datee='11'))
    session.execute(insert(Event).values(name='TEST4', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', interes_sphere='IT', description='DESCRIPTION', datee='11'))
    session.commit()