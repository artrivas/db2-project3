from controllers.rtree_ctrl import get_knn_rtree
from fastapi import APIRouter, UploadFile, File, Form

routes_rtree = APIRouter()

@routes_rtree.post('/knn')
async def get_knn(file: UploadFile = File(...), k: str = Form(...)) -> dict:
    return await get_knn_rtree(file, k)