from sqlalchemy import text
from setting.connection import MysqlConnectionHandler
from repositories.repository import MysqlConnectionHandler
from sqlalchemy.orm import session
from model import User

connection = MysqlConnectionHandler()

class UserRepository():
    @staticmethod
    def get_email(email):
        with connection as conn:
            query=text(f"SELECT * FROM users WHERE email = '{email}'")
            result = conn.execute(query).fetchone()
            return result._mapping
                  
    @staticmethod
    def get_people_all():
        with connection as conn:
            query=text(f"SELECT * FROM users")
            result = conn.execute(query).fetchone()
            return result._mapping

    @staticmethod
    def delete_people(id):
        with connection as conn:
            query=text(f"DELETE FROM users WHERE id = '{id}'")
            result = conn.execute(query)

            conn.commit()
            return result.mappings

    @staticmethod
    def get_id(id):
        with connection as conn:
            query=text(f"SELECT * FROM users WHERE id = '{id}'")
            result = conn.execute(query).fetchone()

            return result._mapping
    
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