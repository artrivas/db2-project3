from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from queue import PriorityQueue
import pandas as pd
import  faiss

data = pd.read_csv('music/song_features.csv')
X = data.iloc[:, :-1].values.astype('float32')  # Asegúrate de que los datos sean de tipo float32
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Inicializa el índice de FAISS
dimension = X.shape[1]  # Dimensión de las características
nlist = 10
# Agrega los vectores al índice
quantizer = faiss.IndexFlatL2(dimension)
index = faiss.IndexIVFFlat(quantizer, dimension, nlist, faiss.METRIC_L2)

# Entrenamiento del índice
index.train(X)
index.add(X)


def knn_faiss(query_object, k):
    query_object = query_object.astype('float32')
    distances, indices = index.search(np.expand_dims(query_object, axis=0), k)
    return [(distances[0][i], data.iloc[indices[0][i]]['etiqueta']) for i in range(k)]

query_example = X[364]  # Puedes cambiar esto con el objeto de consulta que desees
k_result = knn_faiss(query_example, 5)
print("Resultados de búsqueda KNN con FAISS:")
for dist, label in k_result:
    print(f"Distancia: {dist}, Etiqueta: {label}")