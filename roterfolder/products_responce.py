from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from typing import Optional, List

router = APIRouter(prefix='/products', tags=['product'])
products = ['clock', 'frigid', 'wash']


# response
@router.get('/')
def all_products():
    pr = ''.join(products)
    return Response(content=pr, media_type='text/plain')


# html
@router.get('/html')
def all_products():
    pr = ''.join(products)
    return HTMLResponse(content=f'<div style="background_color:red;">{pr}<div>', media_type='text/html')


# plain response
@router.get('pr/{id}')
def get_product(id: int):
    if id > len(products):
        return PlainTextResponse(content='not found', media_type='text/plain')
    else:
        return HTMLResponse(content=f'<div style="background_color:red;">delam shekste<div>', media_type='text/html')


@router.get('/two/{id}', responses={
    404: {'content': {'text/plain': {'example': 'product not found'}},
          'description': 'not found your product'},
    200: {'content': {'text/html': {'example': 'product founded'}},
          'description': 'find your product'
          }
})
def get_product(id: int):
    if id > len(products):
        text = 'not found'
        return PlainTextResponse(status_code=404, content=text, media_type='text/plain')
    else:
        return HTMLResponse(content=f'<div style="background_color:red;">delam shekste<div>', media_type='text/html')


# header
#
# def all_productss(coustom_header:str=Header(None)):
#     data = products
#     #response = Response(content=data, media_type='text/plain')
#     #response.headers['username'] = coustom_header
#     return {'data':products,'header':coustom_header}

# @router.get('/myheader')
# def get_hed(custom_header: str = Header(None)):
#     response = Response(content='success', media_type='text/plain')
#     return response
@router.get('/myheader2')
def get_hedband(custom_header2: str = Header(None)):
    response = Response(content='success', media_type='text/plain')
    response.headers['session'] = custom_header2
    response.set_cookie(key='sithation', value='connected')
    return response


@router.get('cook')
def get_showcook(sithation: str = Cookie(None)):
    response = Response(content=sithation, media_type='text/plain')

    return response


@router.post('create')
def create_product(name: str = Form):
    products.append(name)
    return {'products': products}
