import numpy as np
from scipy.signal import butter, lfilter
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

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

# Define the filter parameters
order = 4               # Filter order
cutoff_freq = 6000      # Cutoff frequency in Hz
sampling_freq = 44100   # Sampling frequency of the audio signal
# TODO: sr * 2 vs sr or constant 44100 (figure out which is better)

# Design the Butterworth low-pass filter
nyquist_freq = 0.5 * sampling_freq
normalized_cutoff_freq = cutoff_freq / nyquist_freq
b, a = butter(order, normalized_cutoff_freq, btype='low', analog=False, output='ba')

# Apply the low-pass filter to the signal
denoised_signal = lfilter(b, a, signal)

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
