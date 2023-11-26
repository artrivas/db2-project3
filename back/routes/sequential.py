from controllers.sequential_ctrl import get_knn_sequential, get_range_sequential
from fastapi import APIRouter, Form
from typing import Optional

routes_sequential = APIRouter()

@routes_sequential.post('/knn')
async def get_knn(track_id: str = Form(...), k: str = Form(...)) -> Optional[dict]: 
    return await get_knn_sequential(track_id, k)

@routes_sequential.post('/range')
async def get_range(track_id: str = Form(...), r: str = Form(...)) -> Optional[dict]:
    return await get_range_sequential(track_id, r)