from fastapi.responses import JSONResponse
from fastapi import Form
from typing import Optional
from handlers.handlers_dict import handlers

PATH_TO_MUSIC = 'music/songs' # update with global path

async def get_knn_sequential(track_id: str = Form(...), k: str = Form(...)) -> Optional[dict]:
    sequential = handlers['sequential']
    try:
        neighbors = sequential.knn_query(track_id, int(k))
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(status_code=404, content="Song not found")
    

async def get_range_sequential(track_id: str = Form(...), r: str = Form(...)) -> Optional[dict]:
    sequential = handlers['sequential']
    try:
        neighbors = sequential.range_query(track_id, float(r))
        return {
            'content': neighbors,
            'status_code': 200
        }
    except Exception as e:
        return JSONResponse(status_code=404, content="Song not found")
    