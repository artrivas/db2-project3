from fastapi.responses import JSONResponse
from idx.invert_index import InvertIndex
from main import handlers

async def get_knn_invidx(data: dict) -> dict:
    try:
        query = data.get('query')
        language = data.get('language')
        k = int(data.get('k')) if data.get('k') != '' else 5

        indivx = handlers['indivx']
        indivx.setLanguage(language)
        result, execution_time = indivx.knn_query(query, k)

        return {'content': result, 'execution_time': f"{execution_time} ms", 'status_code':200}
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)

