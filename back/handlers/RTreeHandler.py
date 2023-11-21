from utils.calculate_exec_time import calculate_exec_time
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from typing import List, Tuple
from rtree import index
import pandas as pd
import numpy as np


class RTreeHandler:
    @calculate_exec_time
    def __init__(self, index_file='music/song_features.csv') -> None: 
        p = index.Property()
        p.dimension = 100
        p.buffering_capacity = 3
        data = pd.read_csv(index_file)
        new_data = self.reduce_dimensionality(data)
        self.collection = new_data
        self.core = index.Index(properties = p)
        for itr in range(len(self.collection)):
            self.core.insert(id=itr,coordinates=self.collection[itr][:-1])

    
    @calculate_exec_time
    def reduce_dimensionality(data: pd.DataFrame) -> List[List[float]]:
        new_data = []
        for i in range(len(data)):
            new_data.append(data.iloc[i][:-1])
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(new_data)
        pca = PCA(n_components=100)
        data_pca = pca.fit_transform(data_scaled)
        new_data_pca =[]
        for i in range(len(data_pca)):
            temp=list(data_pca[i])
            temp.append(data.iloc[i][len(data.iloc[0])-1])
            new_data_pca.append(temp)
        return new_data_pca


    @calculate_exec_time
    def knn_query(self, music: List[List[float]], k: int) -> List[List[Tuple[str, float]]]:
        # Suponiendo que query es el vector de dimensiones de la cancion
        ans = []
        result = self.core.nearest(coordinates=music, num_results=k)
        for itr in result:
            ans.append(self.collection[itr][len(self.collection[itr])-1])
        return ans
