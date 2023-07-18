import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt


def vad(audio_file):
  """Performs voice activity detection on an audio file.

  Args:
    audio_file: The path to the audio file.

  Returns:
    A boolean array indicating whether each frame of audio contains speech.
  """

  # Load the audio file.
  audio, sr = librosa.load(audio_file)

  # Frame the audio signal.
  frames = librosa.util.frame(audio, frame_length=512, hop_length=152)

  # Calculate the energy of each frame.
  energy = np.sum(frames**2, axis=1)

  # Threshold the energy to detect speech frames.
  threshold = np.mean(energy) * 0.9
  vad = energy > threshold

  return vad

def noise_reduction(audio_file, vad):
  """Removes noise from an audio file using VAD.

  Args:
    audio_file: The path to the audio file.
    vad: A boolean array indicating whether each frame of audio contains speech.

  Returns:
    A noise-reduced audio file.
  """

  # Load the audio file.
  audio, sr = librosa.load(audio_file)
    # Resize the vad array to match the audio length.
  vad_resized = np.resize(vad, len(audio))
  
  # Apply the mask to the audio signal.
  noise_reduced_audio = audio * vad_resized

  return noise_reduced_audio, sr, audio


def plot(signal, denoised_signal):
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




noise_file = "../../audios/noise.wav"
music_file = "../../audios/voice.wav"
noised_voice = "signal.wav"


if __name__ == "__main__":
  vad = vad(noised_voice)
  noise_reduced_audio, sr, signal = noise_reduction(noised_voice, vad)
  plot(signal, noise_reduced_audio)
  # Save the noise-reduced audio file.
  sf.write('denoised.wav', noise_reduced_audio, sr)
