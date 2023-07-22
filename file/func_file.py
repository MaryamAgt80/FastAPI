from fastapi import APIRouter, File, UploadFile
from typing import Annotated
import shutil
from fastapi.responses import FileResponse
router = APIRouter(prefix='/file', tags=['files'])


# upload file
@router.post('/upload')
def uploaderfile(file: UploadFile = File(...)):
    path = f'files/{file.filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        'file_size': file.size,
        'file_name': file.filename,
        'type': file.content_type

    }


# download file


# show file
@router.get('show/{name}',response_class=FileResponse)
def show_images(name: str):
    path = f'files/{name}'
    return path
