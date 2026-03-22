# 🎵 Real-time-Audio-Spectrum-Analyzer
> A lightweight Python tool for real-time audio frequency visualization using **FFT**.

![Demo](https://github.com/159357hud-cloud/Audio-Spectrum-Analyzer/blob/main/demo.gif?raw=true) 

## 🌟 Key Features
- **Real-time Processing**: Captures live audio using PyAudio.
- **DSP Implementation**: Leverages `numpy.fft` for efficient Fast Fourier Transform.
- **High Performance**: Optimized for Python 3.12+ on Windows.

## 🛠️ Installation
```bash
pip install -r requirements.txt
python main.py
🔬 Physics & Math
The project transforms time-domain signals $x_n$ into the frequency domain:

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=X_k%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7BN-1%7D%20x_n%20e%5E%7B-%5Cfrac%7Bi2%5Cpi%7D%7BN%7Dkn%7D">
</p>
