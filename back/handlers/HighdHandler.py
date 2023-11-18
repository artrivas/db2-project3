from utils.calculate_exec_time import calculate_exec_time
from faiss import IndexLSH
from typing import List, Tuple
import numpy as np

class HighdHandler:
    @calculate_exec_time
    def __init__(self, num_bits: int, D: int, collection_data: List[Tuple[str, np.ndarray]]) -> None:
        self.collection_data = collection_data
        self.index = IndexLSH(D, num_bits)
        pass


    @calculate_exec_time
    def knn_query(self, music_name: str, k: int) -> List[List[Tuple[str, float]]]:
        pass
