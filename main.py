from fastapi import FastAPI, status, Response
from enum import Enum
from roterfolder import blog_get, blog_post, userfile
from dbfolder.dbtable import engine
from dbfolder import schema

app = FastAPI()
schema.Base.metadata.create_all(engine)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(userfile.router)


@app.get('/', tags=['mainblog', 'blog'])
def hello():
    return ('hello word')


@app.get('/index', tags=['mainblog', 'blog'], description='page of first for show to user', summary='unkhon argomans')
def hello1():
    return ('hello word')


@app.get('/index2')
def hello2():
    return ('hello word')
