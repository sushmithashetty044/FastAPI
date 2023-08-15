from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity


note = APIRouter()
templates = Jinja2Templates(directory = "templates")
@note.get("/",response_class=HTMLResponse)
def read_items(request : Request):
    docs = conn.fastAPI.fastAPI.find({})
    newDoc = []
    for doc in docs:
        newDoc.append({
            "id":doc["_id"],
            "title":doc["title"],
             "desc" : doc["desc"],
             "important":doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request" : request, "newDoc" : newDoc})


@note.post("/")
async def create_items(request : Request):
    form = await request.form()
    formDict = dict(form) 
    formDict["important"] = True if  formDict["important"] == "on" else False
    note = conn.fastAPI.fastAPI.insert_one(formDict)
    return {"Suscces":True}

