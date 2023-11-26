from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from urllib.parse import quote # , unquote
import pandas as pd 
# import unicodedata
import os

PATH_TO_MUSIC = 'music/songs'  # actualiza con la ruta global

async def get_mp3_by_id(id: str):
    try:
        # Construir la ruta completa del archivo
        song_path = os.path.join(PATH_TO_MUSIC, id)

        # Retornar el archivo MP3 como una respuesta de transmisión
        return StreamingResponse(open(song_path, "rb"), media_type="audio/mpeg", headers={"Content-Disposition": f'attachment; filename="{quote(id)}"'})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Song not found")