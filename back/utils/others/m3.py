from rtree import index
import pandas as pd
import librosa
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def reducir_dimensionalidad(data):
    new_data = []
    for i in range(len(data)):
        new_data.append(data.iloc[i][:-1])
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(new_data)
    pca = PCA(n_components=100)
    data_pca = pca.fit_transform(data_scaled)
    new_data_pca =[]
    for i in range(len(data_pca)):
        temp = list(data_pca[i])
        temp.append(data.iat[i, -1])  # Cambio aquí
        new_data_pca.append(temp)
    return new_data_pca

data = pd.read_csv('music/song_features.csv')
new_data = reducir_dimensionalidad(data)

class RtreeIndex:
    def __init__(self,c):
        p = index.Property()
        p.dimension = 100
        p.buffering_capacity = 3
        self.collection = c
        self.core = index.Index(properties=p)
        for itr in range(len(self.collection)):
            self.core.insert(id=itr,coordinates=self.collection[itr][:-1])
    def knn_rtree(self,query,k):
        #Suponiendo que query es el vector de dimensiones de la cancion
        ans = []
        result = self.core.nearest(coordinates=query[:-1],num_results=k)
        for itr in result:
            ans.append(self.collection[itr][len(self.collection[itr])-1])
        return ans

consultas = RtreeIndex(new_data)

resultado = consultas.knn_rtree(new_data[364],20)
print(resultado)