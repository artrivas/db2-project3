from controllers.rtree_ctrl import get_knn_rtree
from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional

routes_rtree = APIRouter()

@routes_rtree.post('/knn')
async def get_knn(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]:
    return await get_knn_rtree(file, k)