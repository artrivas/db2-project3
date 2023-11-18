from utils.calculate_exec_time import calculate_exec_time
from utils.MaxHeap import MaxHeap
from typing import List, Tuple
import numpy as np

class SequentialHandler:
    @calculate_exec_time
    def __init__(self, collection_data: List[Tuple[str, np.ndarray]]) -> None:
        self.collection_data = collection_data
        pass


    @calculate_exec_time
    def range_query(self, music_name: str, radius: float) -> List[List[Tuple[str, float]]]:
        pass


    @calculate_exec_time
    def knn_query(self, music_name: str, k: int) -> List[List[Tuple[str, float]]]:
        pass
