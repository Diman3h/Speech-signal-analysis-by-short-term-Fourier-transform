import numpy as np
import wave
import matplotlib.pyplot as plt
wlen=512
inc=128
f = wave.open(r"lantian.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data = wave_data*1.0/(max(abs(wave_data)))
print(wave_data[:10])
signal_length=len(wave_data) # Общая длина сигнала
    if signal_length<=wlen: # Если длина сигнала меньше длины кадра, количество кадров определяется как 1
        nf=1
    else: # В противном случае рассчитать общую длину кадра
        nf=int(np.ceil((1.0*signal_length-wlen+inc)/inc))
print(nf)
pad_length=int((nf-1)*inc+wlen) # Все кадры складываются в общую сплющенную длину
zeros=np.zeros((pad_length-signal_length,)) # Недостаточная длина заполняется 0, аналогично операции расширенного массива в FFT
pad_signal=np.concatenate((wave_data,zeros)) # Заполненный сигнал записывается как pad_signal
indices=np.tile(np.arange(0,wlen),(nf,1))+np.tile(np.arange(0,nf*inc,inc),(wlen,1)).
print(indices[:2])
indices=np.array(indices,dtype=np.int32) # Преобразовать индексы в матрицу
frames=pad_signal[indices] # Получить сигнал кадра
windown=np.hanning(wlen)
a=frames[50:51]
b=a[0]*windown
fft_signal = np.fft.fft(b)
fft_signal=abs(fft_signal)
time=np.arange(0,wlen)*framerate/nframes
plt.figure(figsize=(10,4))
plt.plot(time,fft_signal,c="g")
plt.grid()
plt.show()
