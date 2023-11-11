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
    session.execute(insert(Event).values(name='TEST1', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', 
interes_sphere='IT', description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='TEST2', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', 
interes_sphere='IT', description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='TEST3', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', 
interes_sphere='IT', description='DESCRIPTION', datee='12'))
    session.execute(insert(Event).values(name='TEST4', time='10.30-11.30', type='Програмирование', activity_field='Оффлайн', 
interes_sphere='IT', description='DESCRIPTION', datee='12'))
    session.commit()

@router.get('/events/')
async def current_event_get(session: Session = Depends(get_db)):
    event = session.execute(select(Event).where(Event.datee==str(int(datetime.datetime.now().day)))).scalars()
    return {"data": datetime.datetime.now().day, "event": [i for i in event]}

@router.post('/excursion/add/')
async def initdb(session: Session = Depends(get_db)):
    excursion = insert(Excursion).values(name='Excursion', short_description='Cool excursion', description='Really cool excursion', duration=90, person='Ivan', person_photo_path='/static/photos/1.jpg')
    session.execute(excursion)
    session.commit()

@router.get("/excursion/{excursion_id}", response_model=ExcursionDto | None)
async def get_excursions(excursion_id: int, session: Session = Depends(get_db)) -> ExcursionDto | None:
    query = select(Excursion).where(Excursion.id == excursion_id).limit(1)
    excursion = session.execute(query).scalar()
    return excursion
