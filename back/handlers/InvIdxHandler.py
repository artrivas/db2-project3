from utils.calculate_exec_time import calculate_exec_time
from idx.invert_index import InvertIndex
from typing import Tuple, List
import pandas as pd

class InvIdxHandler:
    @calculate_exec_time
    def __init__(self, indexfile: str = 'spimi_spanish.txt') -> None:
        self.index = InvertIndex(index_file=indexfile)

    @calculate_exec_time
    def knn_query(self, query: str, k: int, language: str) -> Tuple[pd.DataFrame, List[float], float]:
        return self.index.retrieve_k_nearest(query, k, language)