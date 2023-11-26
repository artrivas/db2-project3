from controllers.music_ctrl import get_mp3_by_id
from fastapi import APIRouter

routes_music = APIRouter()

@routes_music.get('/{track_id}')
async def get_mp3(track_id: str): 
    return await get_mp3_by_id(track_id)