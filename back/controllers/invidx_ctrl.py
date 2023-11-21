from fastapi.responses import JSONResponse
from typing import Optional
from handlers_dict import handlers

async def get_knn_invidx(data: dict) -> Optional[dict]:
    try:
        query: str = data.get('query')
        language: str = data.get('language')
        k = int(data.get('k')) if data.get('k') != '' else 5

        indivx = handlers['invidx']
        results, scores, execution_time = indivx.knn_query(query, k, language)

        rows = results.iloc[:, 2:-2].values.tolist()
        content = list(map(lambda row: ' '.join(map(str, row)), rows))

        df = results.iloc[:, [1, -2]]
        df['content'] = content
        df['scores'] = scores
        df['track_id'] = df['track_id'].astype(int)
        res = df.values.tolist()
        
        return {
            'content': res, 
            'execution_time': f"{execution_time} ms", 
            'status_code':200
        }
    except Exception as e:
        return JSONResponse(content=str(e), status_code=500)

