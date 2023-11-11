from fastapi import FastAPI, Request, status, Depends, APIRouter, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Road
import datetime
import shutil
import os

router = APIRouter(tags=["Roads"])


@router.post('/suggest_road/')
async def suggest_road(session: Session = Depends(get_db), file: UploadFile = File(...), text_data: str = Form(...)):
    file_path = os.path.join('static/photos/', file.filename)
    with open(file_path, "wb") as file_object:
        print(file.file)
        shutil.copyfileobj(file.file, file_object)
    session.execute(insert(Road).values(name=text_data["name"], description=text_data["description", main_photo='', profile_photo='']))
    return JSONResponse(content={"filename": file.filename, "text_data": text_data}, status_code=200)
