import matplotlib.pyplot as plt
import numpy as np
import pickle

# peaks = [(0.0, (993000+554507j)), (-1.0, (328328.42685825494-332873.78432952083j)), (1.0, (115352.33230568987+132419.79160192824j)), (7.0, (61992.3324740241-83294.38358148892j)), (-2.0, (-92577.93675485562-17025.432646439545j)), (-8.0, (8345.030908811921-87365.5193028198j)), (5.0, (-57769.27086454526-34795.782660884965j)), (-6.0, (53729.74651913325+12426.0471361366j)), (8.0, (-2008.642213884841-44933.687488420546j)), (3.0, (31894.438009314686-28600.72999608798j)), (-4.0, (3336.55794305561-39970.337156658854j)), (11.0, (19899.21859798889-29956.63364762169j))]
with open("peaks.pkl", "rb") as f:
   peaks = pickle.load(f)[:5]
length = 3695
dt = 0.001

epicycles = []  # mod, arg, frequency
for i in range(len(peaks)):
    if peaks[i][0] != 0:
        if peaks[i][1].real < 0 and peaks[i][1].imag < 0:
            epicycles.append([-np.abs(peaks[i][1])/length, np.arctan(peaks[i][1].imag/peaks[i][1].real), peaks[i][0]])
        else:
            epicycles.append([np.abs(peaks[i][1])/length, np.arctan(peaks[i][1].imag/peaks[i][1].real), peaks[i][0]])
print(epicycles)
points = [[], []]

fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
plt.ion()
t = 0
while t <= 1:
    for i in points:
        ax.plot(points[0], points[1], marker='.')
    x = 0
    y = 0
    for i in range(len(epicycles)):
        circlex = np.sin(np.linspace(0, 2*np.pi, 50)) * epicycles[i][0] + x
        circley = np.cos(np.linspace(0, 2*np.pi, 50)) * epicycles[i][0] + y
        ax.plot(circlex, circley, color=(0, 0, 0))
        x += epicycles[i][0] * np.cos(epicycles[i][1] + 2*np.pi*epicycles[i][2]*t)
        y += epicycles[i][0] * np.sin(epicycles[i][1] + 2*np.pi*epicycles[i][2]*t)
        # print(x, y)
    ax.set_xlim([-300, 300])
    ax.set_ylim([-300, 300])
    points[0].append(x)
    points[1].append(y)
    plt.pause(0.000000001)
    # if int(t*1000) % 10 == 0:
    #     print(1)
    #     plt.savefig(r'C:\Users\19yiw\PycharmProjects\otherWorks\figs' + chr(92) + str(int(t*100)) + '.png')
    t += dt
    ax.cla()
