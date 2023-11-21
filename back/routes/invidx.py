from controllers.invidx_ctrl import get_knn_invidx
from fastapi import APIRouter
from typing import Optional

routes_invidx = APIRouter()

@routes_invidx.post('/knn')
async def get_knn(data: dict) -> Optional[dict]:
    return await get_knn_invidx(data)