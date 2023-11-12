from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Event, Excursion
from schemas import ExcursionDto
import datetime
from pydantic import BaseModel

router = APIRouter(tags=["Excursions"])


class Excursion_Model(BaseModel):
    name: str
    short_description: str
    description: str
    duration: int
    person: str
    person_photo_path: str


@router.post('/excursion/add/')
async def initdb(excursion: Excursion_Model, session: Session = Depends(get_db)):
    excursion_obj = insert(Excursion).values(name=excursion["name"], short_description=excursion["short_desription"], description=excursion["description"], duration=excursion["duration"], person=excursion["person"], person_photo_path=excursion["person_photo_path"])
    session.execute(excursion_obj)
    session.commit()


@router.get("/excursion/{excursion_id}", response_model=ExcursionDto | None)
async def get_excursions(excursion_id: int, session: Session = Depends(get_db)) -> ExcursionDto | None:
    query = select(Excursion).where(Excursion.id == excursion_id).limit(1)
    excursion = session.execute(query).scalar()
    return excursion
