import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# --- 基础配置 ---
CHUNK = 1024 * 2             # 每次处理的采样点数
FORMAT = pyaudio.paInt16     # 音频格式
CHANNELS = 1                 # 单声道
RATE = 44100                 # 采样率 (Hz)

# 初始化音频流
p = pyaudio.PyAudio()
try:
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, 
                    input=True, frames_per_buffer=CHUNK)
except Exception as e:
    print(f"找不到麦克风或权限被拒绝: {e}")
    exit()

# 设置实时绘图窗口
plt.ion() 
fig, ax = plt.subplots(figsize=(10, 5))
x = np.linspace(0, RATE // 2, CHUNK // 2) 
line, = ax.plot(x, np.zeros(CHUNK // 2), color='#00FFCC', lw=1.2)

ax.set_title("Real-time Audio Spectrum (FFT Analysis)", fontsize=12)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")
ax.set_ylim(0, 1) # 振幅范围
ax.grid(True, linestyle='--', alpha=0.5)

print(">>> 程序已启动，尝试对着麦克风发出声音...")

try:
    while plt.fignum_exists(fig.number):
        # 1. 读取音频数据
        data = stream.read(CHUNK, exception_on_overflow=False)
        data_int = np.frombuffer(data, dtype=np.int16)
        
        # 2. FFT 变换（把时间信号转为频率信号）
        fft_complex = np.fft.fft(data_int)
        fft_abs = np.abs(fft_complex[0:CHUNK//2]) 
        
        # 3. 数据归一化（让波动好看一点）
        y_data = fft_abs / (CHUNK * 500) 
        
        # 4. 更新图表
        line.set_ydata(y_data)
        fig.canvas.draw()
        fig.canvas.flush_events()

except KeyboardInterrupt:
    print("\n程序手动停止")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()