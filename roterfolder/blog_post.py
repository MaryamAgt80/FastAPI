from fastapi import APIRouter,Body,Path,Query,Response,status
from pydantic import BaseModel
from typing import Optional,List

router=APIRouter(prefix='/postblog',tags=['create'])

class blog(BaseModel):
    id:int
    title:str
    body:str
    auther:str


@router.post('/new')
def create_blog(myblog:blog,commentid:int=Query(None,title='comment id',description='enter your comment',alias='ایدی کامنت',deprecated=True), username: str = Body(Ellipsis),):
    return {'message':'post',
            'blog':myblog,'comment':commentid}
