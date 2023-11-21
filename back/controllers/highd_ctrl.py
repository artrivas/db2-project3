from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form
from utils.extract_features import extract_features
from typing import Optional
from handlers_dict import handlers

PATH_TO_MUSIC = 'music/songs' # update with global path

async def get_knn_highd(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]:
    try:
        path = 'music/uploads/' + file.filename
        with open(path, 'wb') as f:
            f.write(file.file.read())
        all_features = extract_features(path)
        highd = handlers['highd']
        neighbors = highd.knn_query(all_features, int(k))
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)