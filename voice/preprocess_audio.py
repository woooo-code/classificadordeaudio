import librosa
from AudioProcessor import log_mel_spectrogram


audio, sr = librosa.load('./output/audio/0.wav', sr=22000, duration=2)
processed = log_mel_spectrogram((audio, sr), librosa_like=True)