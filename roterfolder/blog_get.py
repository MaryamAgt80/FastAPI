from fastapi import APIRouter,Body,Query,Path,Response,status
from pydantic import BaseModel

from enum import Enum

router=APIRouter(prefix='/blog',tags=['blog'])
@router.get('/blog/{id}')
def get_id(id: int,idcom:int=Query(None,gt=12),sub:str=Body()):
    return {'message': f'product{id}'}


@router.get('/default/{id}/{idcomment}')
def deffunc(id: int, idcomment: int, username: str = Body(Ellipsis), valid: bool = True):
    return {'id': id, 'idcomment': idcomment, "username": username, 'valid': valid}
class usertype(str,Enum):
    mes1='user1'
    mes2='user2'
    mes3='user3'
    mes4='user4'

@router.get('/defaultt/{id}/{idcomment}',status_code=status.HTTP_200_OK)
def hrefquest(id: int, idcomment: int, username: usertype, valid:bool,response:Response):
    if id>5:
        response.status_code=status.HTTP_404_NOT_FOUND;
        return 'error'
    return {'id': id, 'idcomment': idcomment, "username": username, 'valid': valid}
