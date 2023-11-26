from controllers.highd_ctrl import get_knn_highd
from fastapi import APIRouter, Form
from typing import Optional

routes_highd = APIRouter()

@routes_highd.post('/knn')
async def get_knn(track_id: str = Form(...), k: str = Form(...)) -> Optional[dict]:
    return await get_knn_highd(track_id, k)