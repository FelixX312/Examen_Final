from typing import Optional
from fastapi import FastAPI, Depends, Form, HTTPException, Path, Query, Header, Response, Cookie
from pymongo import MongoClient
from pydantic import BaseModel, Field 
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId
import json



app = FastAPI()

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    try:
        db = client["fastapieff"]
        yield db
    except Exception as e:
        print(str(e))
        raise
    finally:
        client.close()



class PostBase(BaseModel):
    nombre: str = Field(..., min_length=1,max_length=255)
    apellido: str = Field(..., min_length=1,max_length=255)
    aprobado: bool 
    nota: float 

class PostCreate(PostBase):
    pass



@app.get("/")
def index():
    return {"message": "Welcome to the API, Examen Final"}



@app.get('/post')
def get_all_id(db=Depends(get_db)):
    posts = []
    try:
        docs = db['ef'].find()
        for post in docs:
            posts.append({
                'id': str(post['_id']),
                'nombre': post['nombre'],
                'apellido': post['apellido'],
                'aprobado': post['aprobado'],
                'nota': post['nota'],
                'fecha': post.get('fecha',datetime.now()).isoformat()
            })
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
    return {'Total': len(posts),'Estudiantes': posts}



@app.get('/post/id')
def buscar_id(
    id: Optional[str] = Query(None, min_length=1,max_length=255, descriptions='Filtrar Titulo'),
    db = Depends(get_db)
):
    filtro = {}
    
    if id:
        try:
            filtro['_id'] = ObjectId(id)
        except InvalidId:
            raise HTTPException(status_code=400, detail="ID invalido")

    docs = db['ef'].find(filtro)
    posts = []
    for post in docs:
        posts.append({
            'id': str(post['_id']),
            'nombre': post['nombre'],
            'apellido': post['apellido'],
            'aprobado': post['aprobado'],
            'nota': post['nota'],
            'fecha': post.get('fecha',datetime.now()).isoformat()
        })
    return {'Total': len(posts),'Estudiantes': posts}



@app.post("/post/create-json-data")
def create_one_post_json_data(post: PostCreate, db = Depends(get_db)):
    print(post)
    new_post = {
        "nombre": post.nombre,
        "apellido":post.apellido,
        "aprobado":post.aprobado,
        "nota":post.nota,
        "fecha": datetime.now() 
    }
    print(new_post)
    result = db['ef'].insert_one(new_post)
    print(result.inserted_id)
    created_post = db ['ef'].find_one({'_id': result.inserted_id})
    print(created_post)

    return {
        'id': str(created_post['_id']),
        'nombre': created_post['nombre'],
        'apellido': created_post['apellido'],
        'aprobado': created_post['aprobado'],
        'nota': created_post['nota'],
        'fecha': created_post['fecha'].isoformat()
    }



@app.put("/post/edit/{id}")
def edit_one_post(id: str, post: PostCreate, db = Depends(get_db)):
    existing_post = db['ef'].find_one({'_id': ObjectId(id)})
    if not existing_post:
        return{'Error': 'No existing id'}
    
    updated_data = {
        "nombre": post.nombre,
        "apellido":post.apellido,
        "aprobado":post.aprobado,
        "nota":post.nota,
        "fecha": datetime.now() 
    }

    filtro = {'_id': ObjectId(id)}
    _set = {'$set': updated_data}
    db['ef'].update_one(filtro,_set)

    updated_post = db['ef'].find_one({'_id': ObjectId(id)})
    return{
        'id': str(updated_post['_id']),
        'nombre': updated_post['nombre'],
        'apellido': updated_post['apellido'],
        'aprobado': updated_post['aprobado'],
        'nota': updated_post['nota'],
        'fecha': updated_post['fecha'].isoformat()
    }


@app.delete("/post/delete/{id}")
def delete_one_post(id: str, db = Depends(get_db)):
    post = db['ef'].find_one({'_id': ObjectId(id)})
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    
    db['ef'].delete_one({'_id': ObjectId(id)})
    return{'message': 'Post deleted sucessfully'}