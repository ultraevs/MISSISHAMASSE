from fastapi import FastAPI, Request, status, Depends, APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(tags=["MAIN"])


@router.get('/')
async def get_main():
    with open('static/index.html', 'r') as html:
        data = html.read()
        return HTMLResponse(content=data)