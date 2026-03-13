from fastapi import FastAPI
from repositories.repository import UserRepository

app = FastAPI()

@app.get('/')
def buscar_por_email(email):
    email = UserRepository.get_email(email)
    return email



