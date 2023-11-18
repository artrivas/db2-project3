from utils.calculate_exec_time import calculate_exec_time
from idx.invert_index import InvertIndex
from typing import List, Tuple
import pandas as pd
import numpy as np

class IndInvHandler:
    @calculate_exec_time
    def __init__(self, indexfile: str = 'spimi.txt') -> None:
        self.index = InvertIndex(index_file=indexfile)
        

    @calculate_exec_time
    def set_language(self, language: str = 'en') -> None:
        self.index.set_language(language)
        self.index.construction()    
        

    @calculate_exec_time
    def knn_query(self, query: str, k: int) -> Tuple[pd.DataFrame, float]:
        result, execution_time = self.index.retrieve_k_nearest(query, k)
    





        """
        index = InvertIndex(index_file="spimi.txt")
        matching_indices, scores, execution_time = index.retrieve_k_nearest(query, k)
        df = index.loadData()
        rows = df.iloc[matching_indices].iloc[:, 2:-2].values.tolist()
        content = list(map(lambda row: ' '.join(map(str, row)), rows))
        df = df.iloc[matching_indices].iloc[:, [1, -2]]
        df['content'] = content
        df['scores'] = scores
        df['id'] = df['id'].astype(int)
        result = df.values.tolist()
        """
