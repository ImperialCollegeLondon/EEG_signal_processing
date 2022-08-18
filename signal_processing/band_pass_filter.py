import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import time

data = pd.read_csv('data.csv') # to read data you can use your method 
data = data['EEG']

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_lowpass(cutoffs, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoffs, fs, order=5):
    b, a = butter_lowpass(cutoffs, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y


fps=fs = 10     # sample rate, Hz !!
cutoffs = 30
cutoff=2
filtered_sine_high_pass = butter_highpass_filter(data cutoff, fps)
filtered_sine  =  butter_lowpass_filter(filtered_sine_high_pass, cutoffs, fps)
 
plt.plot(data)
plt.plot(filtered_sine)
plt.show()
