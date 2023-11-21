from controllers.music_ctrl import get_mp3_by_name
from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from typing import Optional

routes_music = APIRouter()

@routes_music.get('/{song_name}')
async def get_mp3(song_name: str): # -> Optional[StreamingResponse]:
    return await get_mp3_by_name(song_name)