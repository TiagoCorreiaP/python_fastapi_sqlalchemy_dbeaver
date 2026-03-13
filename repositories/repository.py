from sqlalchemy import text
from setting.connection import MysqlConnectionHandler

connection = MysqlConnectionHandler()

class UserRepository():

    @staticmethod
    def get_email(email):
        with connection as conn:
            query=text(f"SELECT * FROM users WHERE email = '{email}'")
            result = conn.execute(query).fetchone()
            
            return result._mapping