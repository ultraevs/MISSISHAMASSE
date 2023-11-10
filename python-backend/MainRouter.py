from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(tags=["MAIN"])


@router.get('/')
async def get_main():
    with open('static/index.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)


@router.get('/menu')
async def get_main_menu():
    with open('static/main_menu.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)


@router.get('/tours')
async def get_main_tours():
    with open('static/main_tours.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)


@router.get('/roads')
async def get_main_roads():
    with open('static/main_roads.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)


@router.get('/events')
async def get_main_events():
    with open('static/main_events.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)