from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form
from typing import Optional
from handlers_dict import handlers

PATH_TO_MUSIC = 'music/songs'

async def get_knn_highd(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]:
    try:
        path = 'music/uploads/' + file.filename
        with open(path, 'wb') as f:
            f.write(file.file.read())
        highd = handlers['highd']
        print(path)
        neighbors = highd.knn_query(file.filename, int(k))
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)
