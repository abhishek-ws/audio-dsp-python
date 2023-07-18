import numpy as np
from scipy.signal import medfilt
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

window_size = 1        # Size of the median filter window

# music_file = "../audios/duke.wav"
noise_file = "../../audios/noise.wav"
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

denoised_signal = medfilt(signal, kernel_size=window_size)

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


# Save the filtered signal as a WAV file
sf.write('signal.wav', signal, sr)
sf.write('denoised.wav', denoised_signal, sr)
