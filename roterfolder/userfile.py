from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional, List
from dbfolder import schema
from dbfolder.dbtable import get_db

router = APIRouter(prefix='/user', tags=['user'])


class user_display(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True


class usermodel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]


# create user
@router.post('/create', response_model=user_display)
def createuser(request: usermodel, DB=Depends(get_db)):
    return schema.create_user(request, DB)


# read_users
@router.get('/users', response_model=List[user_display])
def read_all_user(DB=Depends(get_db)):
    return schema.read_users(DB)


# read only user
@router.get('/users/{id}', response_model=user_display)
def read_user(id: int, DB=Depends(get_db)):
    return schema.get_user(DB, id)


@router.get('/users/delete/{id}')
def delete_user(id: int, DB=Depends(get_db)):
    return schema.del_user(DB, id)


@router.post('users/update/{id}')
def update_users(id: int, request: usermodel, DB=Depends(get_db)):
    return schema.user_update(id, DB, request)
