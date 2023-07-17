from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional ,List
from dbfolder import schema
from dbfolder.dbtable import get_db

router = APIRouter(prefix='/articales', tags=['articales'])


class article_display(BaseModel):
    name : str
    user_id : int
    class Config:
        orm_mode=True
class article_display2(BaseModel):
    name : str
    content: str
    class Config:
        orm_mode=True
class articalemodel(BaseModel):
    name: Optional[str]
    content: Optional[str]
    active: bool
    user_id :int

#create user
@router.post('/create',response_model=article_display2)
def createarticle(request: articalemodel, DB=Depends(get_db)):
    return schema.create_articale(request, DB)

@router.get('/articales_user/{id}')
def createarticle(id:int, DB=Depends(get_db)):
    return schema.showarticle_of_user(id, DB)

#read_users
@router.get('/showarticale',response_model=List[article_display])
def read_all_art(DB=Depends(get_db)):
    return schema.read_arts(DB)

#read only user
@router.get('/show/{id}' ,response_model=article_display)
def read_articale(id : int ,DB=Depends(get_db)):
    return schema.get_art(DB,id)
@router.get('/articales/delete/{id}')
def delete_ART(id : int ,DB=Depends(get_db)):
    return schema.del_art(DB,id)


@router.post('users/update/{id}',response_model=article_display)
def update_users(id:int,request:articalemodel,DB=Depends(get_db)):
    return schema.user_update(id,DB,request)
