import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import sys
import urllib

# init pos
x = 409
y = 338

freq = 1  # record every freq points
n_peaks = 100  # no. of epicycles

spider = cv2.imread('spider.jpg')
# print(spider.shape)
for i in range(len(spider)):
    for j in range(len(spider[i])):
        if np.all(spider[i][j] < np.array([240, 240, 240])):
            spider[i][j] = np.array([100, 150, 200])
spider = cv2.GaussianBlur(spider, (5, 5), sigmaX=0.5, sigmaY=0.5)
spider = cv2.Canny(spider, 80, 200)
plt.imshow(spider)
plt.show()
assert spider[y][x] == 255
sys.setrecursionlimit(10000)


def dfs(x, y, graph, start, visited, trace):
    global fig
    pltx, plty = zip(*trace)
    fig.remove()
    fig = plt.plot(pltx, -np.array(plty), color='b')[0]
    plt.pause(0.000001)
    if (x, y) == (411, 337) and len(visited) > 5:
        return trace
    for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
        if not (i == 0 and j == 0):
            x += i
            y += j
            if spider[y][x] == 255 and not ([x, y] in visited):
                visited.append([x, y])
                trace.append([x, y])
                if x == 410 and y == 338:
                    pass
                cur_trace = dfs(x, y, graph, start, visited, trace.copy())
                if cur_trace is not None:
                    return cur_trace

            x -= i
            y -= j
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == 2 or j == 2 or x == -2 or j == -2:
                x += i
                y += j
                if spider[y][x] == 255 and not ([x, y] in visited):
                    visited.append([x, y])
                    trace.append([x, y])
                    cur_trace = dfs(x, y, graph, start, visited, trace.copy())
                    if cur_trace is not None:
                        return cur_trace
                x -= i
                y -= j
    global cur
    cur = (x, y)

plt.ion()
fig = plt.plot([], [])[0]
plt.ylim(-360, 0)
plt.xlim(0, 540)

visited = []
trace = dfs(x, y, spider, (x, y), visited, [[x, y]])
global cur
print(cur)
print(len(trace))
x, y = zip(*trace)
plt.plot(x, -np.array(y), marker='.')
plt.show()