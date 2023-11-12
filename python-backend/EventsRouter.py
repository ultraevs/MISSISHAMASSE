from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Event, Excursion
from schemas import ExcursionDto
import datetime


router = APIRouter(tags=["Events"])

@router.get('/initdb')
async def initdb(session: Session = Depends(get_db)):
    session.execute(insert(Event).values(name='Бокс1', time='10.30-11.30', type='Бокс', activity_field='Оффлайн', 
interes_sphere='Спорт', description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='Тенис2', time='11.30-12.30', type='Теннис', activity_field='Оффлайн', 
interes_sphere="Спорт", description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='Плавание3', time='12.30-13.30', type="Плавание", activity_field='Оффлайн', 
interes_sphere='Спорт', description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='Прога4', time='13.30-14.30', type='Програмирование', activity_field='Онлайн', 
interes_sphere='IT', description='DESCRIPTION', datee='12'))
    session.commit()


@router.get('/events/')
async def current_event_get(session: Session = Depends(get_db)):
    event = session.execute(select(Event)).scalars()
    return {"data": datetime.datetime.now().day, "event": [i for i in event]}

