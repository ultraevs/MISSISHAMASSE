from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from database import engine
Base = declarative_base()


class Sightseeing(Base):
    __tablename__ = "sightseeing"

    id = Column(Integer, primary_key=True, autoincrement=True)  # noqa: A003
    name = Column(String(200))
    firstname = Column(String(50))
    description = Column(String(200))


class Excursion(Base):
    __tablename__ = 'excursions' 
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    short_description = Column(String(200))
    description = Column(String(1000))
    duration = Column(Integer)
    person = Column(String(100))
    person_photo_path = Column(String(100))


class Road(Base):
    __tablename__ = "roads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    firstname = Column(String(100))
    description = Column(String(1000))
    main_photo = Column(String(100))
    profile_photo = Column(String(100))


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    time = Column(String(50))
    datee = Column(String(50))
    type = Column(String(50))
    activity_field = Column(String(50))
    visit_type = Column(String(50))
    interes_sphere = Column(String(50))
    description = Column(String(1000))

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)