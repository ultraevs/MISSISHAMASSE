from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Event, Excursion
from schemas import ExcursionDto
import datetime


router = APIRouter(tags=["Excursions"])


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
