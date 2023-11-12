from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form

async def get_knn_sequential(file: UploadFile = File(...), k: str = Form(...)) -> dict:
    pass

async def get_range_sequential(file: UploadFile = File(...), r: str = Form(...)) -> dict:
    pass