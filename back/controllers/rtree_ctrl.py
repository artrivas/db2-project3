from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form
from typing import Optional
from handlers_dict import handlers

PATH_TO_MUSIC = 'music/songs' # update with global path

async def get_knn_rtree(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]:
    try:
        path = 'music/uploads/' + file.filename
        with open(path, 'wb') as f:
            f.write(file.file.read())
        rtree = handlers['rtree']
        neighbors = rtree.knn_query(file.filename, int(k))
        print(path)
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)
