from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from database import engine
Base = declarative_base()


class Sightseeing(Base):
    __tablename__ = "sightseeings"

    id = Column(Integer, primary_key=True, autoincrement=True)  # noqa: A003
    name = Column(String(200))
    coord_x = Column(Float(50))
    coord_y = Column(Float(50))
    description = Column(String(1000))


class Road(Base):
    __tablename__ = "roads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(1000))
    main_photo = Column(String(100))
    profile_photo = Column(String(100))


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    time = Column(String(50))
    date = Column(String(50))
    type = Column(String(50))
    activity_field = Column(String(50))
    visit_type = Column(String(50))
    interes_sphere = Column(String(50))
    description = Column(String(1000))


Base.metadata.create_all(bind=engine)