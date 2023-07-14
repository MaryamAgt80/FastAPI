from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from dbfolder import schema
from dbfolder.dbtable import get_db

router = APIRouter(prefix='/user', tags=['user'])
from dbfolder.schema import usermodel

@router.post('/create')
def createuser(request: usermodel, DB=Depends(get_db)):
    return schema.create_user(request, DB)
