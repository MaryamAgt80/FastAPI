# from fastapi import APIRouter, Depends, status
# from fastapi.exceptions import HTTPException
# from pydantic import BaseModel
# from typing import Optional, List
# from dbfolder import schema
# from dbfolder.dbtable import get_db
# from dbfolder.schema import user
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm
# from auth import athutication
#
# router = APIRouter(tags=['authentication'])
#
#
# @router.post('/token')
# def get_token(request: OAuth2PasswordRequestForm = Depends(), DB: Session = Depends(get_db)):
#     User = DB.query(user).filter(user.name == request.username).first()
#     print(User.name)
#     if User:
#         access_token = athutication.create_access_token(data={'sub': User.name})
#         return {
#             'access_token': access_token,
#             'type_token': 'bearer',
#             'userID': user.id,
#             'username': user.name,
#         }
#
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username is not valid')
