from controllers.invidx_ctrl import get_knn_invidx
from fastapi import APIRouter, Form
from typing import Optional

routes_invidx = APIRouter()

@routes_invidx.post('/knn')
async def get_knn(query: str = Form(...), k: str = Form(...), language: str = Form(...)) -> Optional[dict]:
    return await get_knn_invidx(query, k, language)