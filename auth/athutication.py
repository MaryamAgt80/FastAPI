# from fastapi.security import OAuth2PasswordBearer
# from datetime import timedelta, datetime
# from typing import Optional
# from jose import jwt
#
# auth_schema = OAuth2PasswordBearer(tokenUrl='token')
# secret_key = 'afede8100f8028754264274992c35265aa420d3d028f00076d2cd4c64dc5d896'
# algoritm_coding = 'HS256'
# ACCESS_TOKEN_TIME = 30
#
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     # if expires_delta:
#     #     expire = datetime.utcnow() + expires_delta
#     # else:
#     #     expire = datetime.utcnow() + timedelta(minutes=15)
#     # to_encode.update({'exp': expire})
#     encoded = jwt.encode(to_encode, secret_key, algorithm=algoritm_coding)
#     return encoded
