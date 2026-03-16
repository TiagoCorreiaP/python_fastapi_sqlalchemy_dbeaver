from fastapi import FastAPI, HTTPException
from repositories.repository import UserRepository
from model import UserCreate

app = FastAPI()

@app.get('/search_by_email')
def search_by_email(email):
    email = UserRepository.get_email(email)
    return email


@app.get('/')
def read_all():
    return UserRepository.get_people_all()

@app.delete('/delete_users')
def deletar_by_id(id):
    return UserRepository.delete_people(id)

@app.get('/search_by_id')
def search_by_id(id):
    return UserRepository.get_id(id)

@app.post('/create')
def create_user_route(user_data: UserCreate):
    return UserRepository.create_user(user_data)