from sqlalchemy import Column, Integer, String, update, ForeignKey
from dbfolder.dbtable import Base, get_db
from dbfolder.hashpass import changepasshash
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session, relationship, Mapped, mapped_column
from dbfolder.hashpass import changepasshash
from fastapi import status
from fastapi.exceptions import HTTPException
from dbfolder.exception import EMAILINVALID , USEREXIST ,FIELDSISNULL


class user(Base):
    __tablename__ = 'user_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String)
    child_articles: Mapped[List["Article"]] = relationship()


class Article(Base):
    __tablename__ = "articales"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name = Column(String(50))
    content = Column(String(50))
    active = bool
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))


################      user        ###########################
class usermodel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]


def create_user(request: usermodel, DB: Session):
    print(request.name)
    if '@' not in request.email:
        raise EMAILINVALID('eror not @ in email')
    if ((not request.name) or (not request.email) or (not request.password) ):
        raise FIELDSISNULL('fileds is null')
    User = user(name=request.name,
                email=request.email,
                password=changepasshash(request.password))
    DB.add(User)
    DB.commit()
    DB.refresh(User)
    return User


# read all users
def read_users(DB: Session):
    users = DB.query(user).all()
    return users


# read user
def get_user(DB: Session, id: int):
    User = DB.query(user).filter(user.id == id).first()

    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found user that id ={id}')
    return User


# delete user
def del_user(DB: Session, id: int):
    User = get_user(DB, id)
    DB.delete(User)
    DB.commit()
    return 'removed'


def user_update(id, DB: Session, request: usermodel):
    User = DB.query(user).filter(user.id == id)

    User.update({
        user.name: request.name,
        user.email: request.email,
        user.password: changepasshash(request.password)
    })
    DB.commit()
    return 'ok'


##############################    artclale       #########################################

class articalemodel(BaseModel):
    name: Optional[str]
    content: Optional[str]
    active: bool
    user_id: int


def create_articale(request: articalemodel, DB: Session):
    ArtilceAbject = Article(name=request.name,
                            content=request.content,
                            active=request.active,
                            user_id=request.user_id)
    DB.add(ArtilceAbject)
    DB.commit()
    DB.refresh(ArtilceAbject)
    return ArtilceAbject


def showarticle_of_user(id: int, DB: Session):
    UserAbject = DB.query(user).filter(user.id == id).first()
    list_article = UserAbject.child_articles
    return list_article


def read_arts(DB: Session):
    ARTS = DB.query(Article).all()
    return ARTS


def get_art(DB: Session, id: int):
    ArticalesAbjects = DB.query(Article).filter(Article.id == id).first()
    return ArticalesAbjects


def del_art(DB: Session, id: int):
    AbjectArticle = get_art(DB, id)
    DB.delete(AbjectArticle)
    DB.commit()
    return 'removed'
