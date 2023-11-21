import librosa
import numpy as np
import pandas as pd
import os

def extract_features(file_path, max_length=1000):
    audio, sr = librosa.load(file_path, mono=True)
    # 1. Coeficientes MFCC
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)
    mfcc_features = np.concatenate((mfccs.mean(axis=1), mfccs.std(axis=1)))

    # 2. Delta MFCC
    delta_mfccs = librosa.feature.delta(mfccs)
    delta_mfcc_features = np.concatenate((delta_mfccs.mean(axis=1), delta_mfccs.std(axis=1)))

    # 3. Delta Delta MFCC
    delta2_mfccs = librosa.feature.delta(mfccs, order=2)
    delta2_mfcc_features = np.concatenate((delta2_mfccs.mean(axis=1), delta2_mfccs.std(axis=1)))

    # Representan la información espectral de la señal de audio.
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr)

    # 4. Contraste espectral
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)

    # 5. Tonnetz
    tonnetz = librosa.feature.tonnetz(y=audio, sr=sr)

    # 6. Tempograma
    tempo, tempogram = librosa.beat.beat_track(y=audio, sr=sr)

    # Asegurar que todas las características tengan la misma longitud
    all_features = np.concatenate((
        mfcc_features,
        delta_mfcc_features,
        delta2_mfcc_features,
        chroma.mean(axis=1),
        contrast.mean(axis=1),
        tonnetz.mean(axis=1),
        tempogram
    ))

    # Rellenar con ceros si es necesario
    if len(all_features) < max_length:
        all_features = np.pad(all_features, (0, max_length - len(all_features)))
    else:
        # Recortar si es necesario
        all_features = all_features[:max_length]
    return all_features


def listar_archivos_carpeta(ruta_carpeta):
    archivos = [arch for arch in os.listdir(ruta_carpeta) if arch.endswith(('.mp3'))]
    return archivos


def main():
    ruta_carpeta = "music/songs"
    archivos_carpeta = listar_archivos_carpeta(ruta_carpeta)

    # Almacena las características y las etiquetas (nombre de archivo) en listas
    caracteristicas = []
    etiquetas = []

    for archivo in archivos_carpeta:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        features = extract_features(ruta_archivo)
        caracteristicas.append(features)
        etiquetas.append(archivo)
    etiquetas = np.array(etiquetas)
    df = pd.DataFrame(data=caracteristicas)
    df['etiqueta'] = etiquetas
    df.to_csv('music/song_features.csv', index=False)


if __name__ == '__main__':
    main()