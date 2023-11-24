from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from urllib.parse import quote, unquote
import os
import unicodedata

PATH_TO_MUSIC = 'music/songs'  # actualiza con la ruta global

async def get_mp3_by_name(song_name: str): # -> Optional[StreamingResponse]:
    try:
        # Decodificar el nombre del archivo de la URL
        song_name_decoded = unquote(song_name)

        # Normalizar los caracteres Unicode en el nombre del archivo
        song_name_normalized = unicodedata.normalize('NFKD', song_name_decoded)

        # Encontrar el archivo MP3 correspondiente al nombre de la canción
        song_file = None
        for f in os.listdir(PATH_TO_MUSIC):
            f_normalized = unicodedata.normalize('NFKD', f)
            if f_normalized.lower().startswith(song_name_normalized.lower()) and f_normalized.endswith('.mp3'):
                song_file = f
                break

        if not song_file:
            raise HTTPException(status_code=404, detail="Song not found")

        # Construir la ruta completa del archivo
        song_path = os.path.join(PATH_TO_MUSIC, song_file)

        # Retornar el archivo MP3 como una respuesta de transmisión
        return StreamingResponse(open(song_path, "rb"), media_type="audio/mpeg", headers={"Content-Disposition": f'attachment; filename="{quote(song_file)}"'})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))