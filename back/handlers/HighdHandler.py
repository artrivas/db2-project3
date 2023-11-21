from utils.calculate_exec_time import calculate_exec_time
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple
import pandas as pd
import numpy as np
class HighdHandler:
    pass
"""
from faiss

    @calculate_exec_time
    def __init__(self, index_file='../music/song_features.csv') -> None:
        self.data = pd.read_csv(index_file)
        data_values = self.data.iloc[:, :-1].values.astype('float32')
        scaler = StandardScaler()
        self.collection_data = scaler.fit_transform(data_values)
        dimension = data_values.shape[1] 
        nlist = 10
        quantizer = faiss.IndexFlatL2(dimension)
        self.index = faiss.IndexIVFFlat(quantizer, dimension, nlist, faiss.METRIC_L2)

    @calculate_exec_time
    def knn_query(self, music: List[List[float]], k: int) -> List[List[Tuple[str, float]]]:
        distances, indices = self.index.search(music, k)
        return [(distances[0][i], self.data.iloc[indices[0][i]]['etiqueta']) for i in range(k)]
"""