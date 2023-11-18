import pickle
import numpy as np

# Supongamos que tienes una lista de tuplas como esta
mi_lista = [('dato1', np.array([1, 2, 3])),
            ('dato2', np.array([4, 5, 6])),
            ('dato3', np.array([7, 8, 9]))]

# Guardar la lista en un archivo
with open('embeds/archivo.pkl', 'wb') as archivo:
    pickle.dump(mi_lista, archivo)

# Cargar la lista desde el archivo
with open('embeds/archivo.pkl', 'rb') as archivo:
    lista_cargada = pickle.load(archivo)

# Imprimir la lista cargada
print(lista_cargada)
