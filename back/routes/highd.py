from controllers.highd_ctrl import get_knn_highd
from fastapi import APIRouter, UploadFile, File, Form

routes_highd = APIRouter()

@routes_highd.post('/knn')
async def get_knn(file: UploadFile = File(...), k: str = Form(...)) -> dict:
    return await get_knn_highd(file, k)