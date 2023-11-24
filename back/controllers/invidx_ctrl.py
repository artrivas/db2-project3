from fastapi.responses import JSONResponse
from typing import Optional
from handlers_dict import handlers
from fastapi import Form

async def get_knn_invidx(query: str = Form(...), k: str = Form(...), language: str = Form(...)) -> Optional[dict]:
    try:
        query: str = query
        k = int(k) if k != '' else 5
        language: str = language

        indivx = handlers['invidx']
        results, scores, execution_time = indivx.knn_query(query, k, language)
        if results.shape[0] == 0: 
            res = {}
        else:
            df = results.copy()  
            df['scores'] = scores
            res = df.to_dict(orient='index')
            
        return {
            'content': res, 
            'execution_time': f"{execution_time} ms", 
            'status_code': 200
        }
    except Exception as e:
        return {
            'content': {}, 
            'status_code': 200
        }
