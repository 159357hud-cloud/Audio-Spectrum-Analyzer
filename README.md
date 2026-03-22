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


$$
X_k = \sum_{n=0}^{N-1} x_n e^{-\frac{i2\pi}{N}kn}
$$


这里是公式的后续说明。
