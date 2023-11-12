import os
import pickle
import librosa
import numpy as np
from typing import List, Tuple

class FeatureExtractor:
    def __init__(self, music_path: str) -> None:
        """
        Initialize the FeatureExtractor instance.

        Args:
            music_path (str): The path to the directory containing music files.
        """
        self.music_path: str = music_path

    def extract_features(self, audio_file_path: str) -> np.ndarray:
        """
        Extract audio features from a given audio file.

        Args:
            audio_file_path (str): The path to the audio file.

        Returns:
            np.ndarray: Extracted audio features.
        """
        # Add logic to extract audio features using librosa
        y, sr = librosa.load(audio_file_path)
        features = librosa.feature.mfcc(y=y, sr=sr)
        return features

    def process_music_directory(self) -> None:
        """
        Process the music directory, extract features, and save them to a pickle file.
        """
        output: List[Tuple[str, np.ndarray]] = []

        for root, dirs, files in os.walk(self.music_path):
            for file in files:
                if file.endswith(".mp3"):
                    audio_file_path = os.path.join(root, file)
                    audio_features = self.extract_features(audio_file_path)
                    output.append((file, audio_features))

        # Save the features to a pickle file
        with open("embeds/collection.pkl", mode="wb") as outfile:
            pickle.dump(output, outfile)

def main() -> None:
    music_feature_extractor = FeatureExtractor(music_path="../music")
    music_feature_extractor.process_music_directory()

if __name__ == '__main__':
    main()
