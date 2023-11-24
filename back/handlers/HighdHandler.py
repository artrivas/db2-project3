from utils.calculate_exec_time import calculate_exec_time
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple
import pandas as pd
import numpy as np
import faiss

class HighdHandler:
    @calculate_exec_time
    def __init__(self, index_file='music/song_features.csv') -> None:
        self.data = pd.read_csv(index_file)
        data_values = self.data.iloc[:, :-1].values.astype(np.float32)  # Convertir a numpy.float32
        scaler = StandardScaler()
        self.collection_data = scaler.fit_transform(data_values)
        dimension = data_values.shape[1] 
        nlist = 10
        quantizer = faiss.IndexFlatL2(dimension)
        self.index = faiss.IndexIVFFlat(quantizer, dimension, nlist, faiss.METRIC_L2)
        # Entrenamiento del índice
        self.index.train(self.collection_data)
        self.index.add(self.collection_data)

    @calculate_exec_time
    def knn_query(self, filename: str, k: int) -> List[List[Tuple[str, float]]]:
        num = self.data.loc[self.data['etiqueta'] == filename].index[0]
        query = self.collection_data[num]
        distances, indices = self.index.search(np.expand_dims(query, axis=0), k)
        return [(float(distances[0][i]), self.data.iloc[indices[0][i]]['etiqueta']) for i in range(k)]