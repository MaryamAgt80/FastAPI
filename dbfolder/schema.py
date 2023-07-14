from sqlalchemy import Column, Integer, String
from dbfolder.dbtable import Base, get_db
from dbfolder.hashpass import changepasshash
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from dbfolder.hashpass import changepasshash


class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String)


class usermodel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]


def create_user(request: usermodel, DB: Session):
    print(request.name)
    User = user(name=request.name,
                email=request.email,
                password=request.password)
    DB.add(User)
    DB.commit()
    DB.refresh(User)
    return User
