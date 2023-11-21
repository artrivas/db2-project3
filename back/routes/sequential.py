from controllers.sequential_ctrl import get_knn_sequential, get_range_sequential
from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional

routes_sequential = APIRouter()

@routes_sequential.post('/knn')
async def get_knn(file: UploadFile = File(...), k: str = Form(...)) -> Optional[dict]: 
    return await get_knn_sequential(file, k)

@routes_sequential.post('/range')
async def get_range(file: UploadFile = File(...), r: str = Form(...)) -> Optional[dict]:
    return await get_range_sequential(file, r)