from utils.calculate_exec_time import calculate_exec_time
from rtree import index
from typing import List, Tuple
import numpy as np

class RTreeHandler:
    @calculate_exec_time
    def __init__(self, M: int, D: int, collection_data: List[Tuple[str, np.ndarray]]) -> None:
        self.collection_data = collection_data
        prop = index.Property()
        prop.dimension = D
        prop.buffering_capacity = M
        pass


    @calculate_exec_time
    def knn_query(self, music_name: str, k: int) -> List[List[Tuple[str, float]]]:
        pass
