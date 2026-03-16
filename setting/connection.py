from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class MysqlConnectionHandler:
    def __init__(self):
        self.__session = None
        self.__url = "mysql+pymysql://root:tiagocorreia@localhost:3307/teste"
        self.__engine = self.create_engine()
        
    def create_engine(self):
        self.__engine = create_engine(self.__url)
        return self.__engine
        
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        return self.__session
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
