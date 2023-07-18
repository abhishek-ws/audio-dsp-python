### Audio Signal Processing and filtering

This repository contains practical implementaion of various techniques used for filtering an audio signal and reducing noise to the minimal.

Following are the techniques covered in this repository so far :-

---

#### Low pass filtering

- Low-pass filtering removes high-frequency noise by attenuating frequencies above a certain cutoff. The scipy library offers various low-pass filter design functions, such as Butterworth, Chebyshev, and FIR filters.

- Practical implementation is [here](https://github.com/abhishek-ws/audio-dsp-python/tree/main/noise-filter/low-pass-filtering)

---

#### Wavelet denoising

- Wavelet denoising is based on the wavelet transform, which decomposes the signal into different frequency components using a set of wavelet basis functions.
- It provides a time-frequency representation of the signal and noise, allowing for more localized analysis and denoising.
- Practical implementation is [here](https://github.com/abhishek-ws/audio-dsp-python/tree/main/noise-filter/wavelet-denoising)

#### Median Filtering

- Median filtering replaces each sample with the median value in its neighborhood, which can effectively suppress impulsive noise. The scipy library includes functions for median filtering.

- Practical implementation is [here](https://github.com/abhishek-ws/audio-dsp-python/tree/main/noise-filter/median-filtering)

---

#### Voice activity detection

- An algorithm to detect periods of speech activity and silence in the audio signal. By activating the noise reduction techniques only during speech segments, you can reduce the risk of distorting the desired speech signal.

- Practical implementation is [here](https://github.com/abhishek-ws/audio-dsp-python/tree/main/noise-filter/voice-activity-detection)

---

- The repository is a POC to showcase how to process a audio file.
- I have done some fine tuning with the scripts in order to make sure the filtering algorithm is optimised
- I will be doing some more iterations on the scripts and add more methods as per requirements

#### References

- [Librosa docs](https://librosa.org/doc/latest/index.html)
- [Audio Signal Processing for Machine Learning](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0)
- [Signal Processing: Filtering Out The Noise](https://www.catchpoint.com/blog/signal-vs-noise)
- [Noise Reduction using Filters
  ](https://medium.com/@abhijnanprakash/noise-reduction-using-filters-5c8fa8bce42)

#### Upcoming additions :-

- **Spectral Subtraction**: This method estimates the noise spectrum from a noisy signal and subtracts it from the magnitude spectrum to enhance the desired signal. The magnitude spectrum can be obtained using the FFT. The librosa library in Python provides functions for spectral subtraction.

- **Wiener Filtering**: Wiener filtering is a statistical approach that estimates the clean signal from the noisy signal using the power spectral densities of both the noise and the clean signal. The scipy library in Python provides functions for Wiener filtering.
