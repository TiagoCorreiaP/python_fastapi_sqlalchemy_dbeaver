from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, EmailStr

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    idade: Mapped[int]
    profissao: Mapped[str]

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    idade: int
    profissao: str

class Config:
    from_attributes = True
