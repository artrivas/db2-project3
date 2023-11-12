from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form

async def get_knn_rtree(file: UploadFile = File(...), k: str = Form(...)) -> dict:
    pass
