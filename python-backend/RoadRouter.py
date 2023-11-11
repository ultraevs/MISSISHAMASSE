from fastapi import FastAPI, Request, status, Depends, APIRouter, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db, engine
from models import Road
import datetime
import shutil
import os
import json

router = APIRouter(tags=["Roads"])


from typing import List


@router.post('/suggest_road/')
async def suggest_road(
    session: Session = Depends(get_db),
    files: List[UploadFile] = File(...),
    text_data: str = Form(...)
):
    try:
        text_data_dict = json.loads(text_data)
        # Путь к папке для сохранения файлов
        upload_folder = 'static/photos/'

        # Проверка существования папки
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        main_photo_path = ''
        profile_photo_path = ''

        for i, file in enumerate(files):
            # Путь к файлу на сервере
            file_path = os.path.join(upload_folder, file.filename)

            # Сохраняем файл
            with open(file_path, "wb") as file_object:
                shutil.copyfileobj(file.file, file_object)

            # Присваиваем пути к соответствующим переменным
            if i == 0:
                main_photo_path = os.path.join('photos', file.filename)
            elif i == 1:
                profile_photo_path = os.path.join('photos', file.filename)
        session.execute(
            insert(Road).values(
                name=text_data_dict.get("name", ""),
                description=text_data_dict.get("description", ""),
                main_photo=main_photo_path,
                profile_photo=profile_photo_path
            )
        )
        session.commit()
        return JSONResponse(content={"text_data": text_data_dict}, status_code=200)

    except Exception as e:
        # Handle errors
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get('/road/{road_name}')
async def get_road(road_name: str, session: Session = Depends(get_db)):
    road = session.execute(select(Road).filter_by(name=road_name)).scalar()

    if road:
        text_data = {
            "name": road.name,
            "description": road.description
        }

        # Response with text data as JSON
        json_response = JSONResponse(content={"text_data": text_data})

        # Response with photo files
        main_photo_path = 'static/' + road.main_photo
        profile_photo_path = 'static/' + road.profile_photo
        main_photo_response = FileResponse(main_photo_path, media_type="image/jpeg", headers={"Content-Disposition": f"attachment; filename={os.path.basename(main_photo_path)}"})
        profile_photo_response = FileResponse(profile_photo_path, media_type="image/jpeg", headers={"Content-Disposition": f"attachment; filename={os.path.basename(profile_photo_path)}"})

        # Combine responses
        responses = [json_response, main_photo_response, profile_photo_response]

        return responses

    return JSONResponse(content={"error": "Road not found"}, status_code=404)