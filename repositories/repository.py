from sqlalchemy import text
from setting.connection import MysqlConnectionHandler
from repositories.repository import MysqlConnectionHandler
from sqlalchemy.orm import session
from model import User

connection = MysqlConnectionHandler()

class UserRepository():
    @staticmethod
    def get_email(user_email: str):
        with connection as conn:
            return conn.query(User).filter(User.email == user_email).first() 
                  
    @staticmethod
    def get_people_all():
        with connection as conn:
            query=text(f"SELECT * FROM users")
            result = conn.execute(query).fetchall()

            return [row._mapping for row in result]  

    @staticmethod
    def delete_people(user_id: int):
        with connection as conn:
            usuario = conn.query(User).filter(User.id == user_id).delete()
            conn.commit()

    @staticmethod
    def get_id(user_id: int):
        with connection as conn:
            return conn.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def create_user(user_data):
        with connection as conn:
            
            new_user = User(
                nome=user_data.nome,
                email=user_data.email,
                idade=user_data.idade,
                profissao=user_data.profissao
            )
            conn.add(new_user)
            conn.commit()
            conn.refresh(new_user)
            return new_user

