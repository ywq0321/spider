import pickle
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

n_peaks = 100


with open("spider.json", "r") as f:
   trace = json.load(f)

trace.append(trace[0])
factor = len(trace)
x, y = zip(*trace)
y = -np.array(y) + 338
plt.scatter(x, y, marker='.')
# plt.show()

points = []

for i in range(len(x)):
    points.append(x[i] + 1j*y[i])
yf = fft(points)
xf = fftfreq(len(points), 1 / len(points))
# plt.plot(xf, yf)
# plt.show()

# plt.clf()
print(len(points))
peaks = list(reversed(sorted(zip(xf, yf), key=lambda a: np.abs(a[1]))))[:n_peaks]
print(peaks)

# with open("peaks.pkl", "wb") as f:
#    pickle.dump(peaks, f)
t = np.linspace(0, 2*np.pi, 1000)
xt = []
yt = []
for i in t:
    x = 0
    y = 0
    for j in peaks:
        x += j[1].real * np.cos(j[0] * i) - j[1].imag * np.sin(j[0] * i)
        y += j[1].real * np.sin(j[0] * i) + j[1].imag * np.cos(j[0] * i)
    xt.append(x)
    yt.append(y)
print(factor)
plt.scatter(np.array(xt)/factor, np.array(yt)/factor, marker='.')
plt.show()

