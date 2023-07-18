import numpy as np
import librosa
import matplotlib.pyplot as plt
import pywt
import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile

noise_file = "../../audios/noise.wav"
# music_file = "../audios/duke.wav"
music_file = "../../audios/voice.wav"

# Load the audio signal
noise, sr = librosa.load(noise_file)
music, sr = librosa.load(music_file)
# Ensure the noise and music arrays have the same length
min_length = min(len(noise), len(music))
noise = noise[:min_length]
music = music[:min_length]

# Combine the noise and music signals
signal = noise + music


# wavelet_name = "db3"
wavelet_name = "sym14"
# wavelet_name = "db31"
level = 1

# Set the threshold value
threshold_value = 0.5

# Perform wavelet denoising
coeffs = pywt.wavedec(signal, wavelet_name, level=level)
thresholded_coeffs = []
for detail_coeff in coeffs[1:]:
    thresholded_coeff = pywt.threshold(detail_coeff, threshold_value, mode='soft')
    thresholded_coeffs.append(thresholded_coeff)
denoised_signal = pywt.waverec([coeffs[0]] + thresholded_coeffs, wavelet_name)

sf.write('signal.wav', signal, sr)
sf.write('denoised.wav', denoised_signal, sr)

# sd.play(signal, sr)
# sd.play(drbio1.1

# # Plot the original signal and denoised signal
plt.figure(figsize=(14, 12))
plt.subplot(2, 1, 1)
plt.plot(signal, color='blue', label='Noisy Signal')
plt.title('Noisy Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(denoised_signal, color='red', label='Denoised Signal')
plt.title('Denoised Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig("signal-processing")

# plt.tight_layout()
# plt.savefig(denoised_signal, dpi=300)
# plt.savefig(signal, dpi=300)