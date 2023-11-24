from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form
from typing import Optional
from handlers_dict import handlers
import numpy as np   

PATH_TO_MUSIC = 'music/songs' # update with global path

async def get_knn_sequential(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]:
    try:
        path = 'music/uploads/' + file.filename
        with open(path, 'wb') as f:
            f.write(file.file.read())
        sequential = handlers['sequential']
        neighbors = sequential.knn_query(file.filename, int(k))
        print(path)
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)


async def get_range_sequential(file: UploadFile = File(...), r: str = Form(...)) -> Optional[dict]:
    try:
        path = 'music/uploads/' + file.filename
        with open(path, 'wb') as f:
            f.write(file.file.read())
        sequential = handlers['sequential']
        neighbors = sequential.range_query(file.filename, float(r))
        print(path)
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)