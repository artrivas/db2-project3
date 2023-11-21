from utils.calculate_exec_time import calculate_exec_time
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from queue import PriorityQueue
from typing import List, Tuple
import numpy as np
import pandas as pd

class SequentialHandler:
    @calculate_exec_time
    def __init__(self, index_file='music/song_features.csv') -> None:
        self.data = pd.read_csv(index_file)
        data_values = self.data.iloc[:, :-1].values.astype('float32')
        scaler = StandardScaler()
        self.collection_data = scaler.fit_transform(data_values)
        

    @calculate_exec_time
    def range_query(self, music: List[List[float]], radius: float) -> List[List[Tuple[str, float]]]:
        within_radius = []
        for i in range(len(self.collection_data)):
            # Calcular la distancia euclidiana
            distance = euclidean_distances(music, self.collection_data[i].reshape(1, -1))[0, 0]
            # Verificar si la distancia está dentro del radio
            if distance <= radius:
                label = self.data.iloc[i]['etiqueta']
                within_radius.append((distance, label))
        return within_radius


    @calculate_exec_time
    def knn_query(self, music: List[List[float]], k: int) -> List[List[Tuple[str, float]]]:
        similarities = cosine_similarity(music, self.collection_data).flatten()
        # Cola de prioridad
        priority_queue = PriorityQueue()
        for i, sim in enumerate(similarities):
            priority_queue.put((-sim, self.data.iloc[i]['etiqueta']))
        neighbors = []
        for _ in range(k):
            sim, neighbor = priority_queue.get()
            neighbors.append((neighbor, -sim))
        return neighbors
