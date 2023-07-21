from fastapi import FastAPI, status, Response
from fastapi.requests import Request
from roterfolder import blog_get, blog_post, userfile, articales, products_responce
from dbfolder.dbtable import engine
from dbfolder import schema
from dbfolder.exception import EMAILINVALID, USEREXIST, FIELDSISNULL
from fastapi.responses import JSONResponse
from auth import auth2
app = FastAPI()
schema.Base.metadata.create_all(engine)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(userfile.router)
app.include_router(articales.router)

app.include_router(products_responce.router)
app.include_router(auth2.router)


@app.get('/', tags=['mainblog', 'blog'])
def hello():
    return ('hello word')


@app.get('/index', tags=['mainblog', 'blog'], description='page of first for show to user', summary='unkhon argomans')
def hello1():
    return ('hello word')


@app.get('/index2')
def hello2():
    return ('hello word')


@app.exception_handler(EMAILINVALID)
def email_not_valid(request: Request, exc: EMAILINVALID):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.exception_handler(FIELDSISNULL)
def fields_not_found(request: Request, exc=FIELDSISNULL):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)
