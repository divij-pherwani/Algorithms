import sys
import numpy as np
from itertools import combinations


def fwa(n, roads):
    delta = np.ones(shape=(n, n)) * np.inf
    pairs = list(combinations(range(n), 2))
    for i in range(n):
        delta[i][i] = 0
    for j in roads:
        delta[j[0]][j[1]] = 1
        delta[j[1]][j[0]] = 1
    for k in range(n):
        for j in pairs:
            delta[j[0]][j[1]] = min(delta[j[0]][j[1]], delta[j[0]][k] + delta[k][j[1]])
            delta[j[1]][j[0]] = min(delta[j[1]][j[0]], delta[j[1]][k] + delta[k][j[0]])
    return delta


def dash(n, s, delta):
    d_dash = [np.inf for _ in range(n)]
    for i in range(n):
        for j in s:
            d_dash[i] = min(d_dash[i], delta[j][i], delta[i][j])
    return d_dash


def buildCastle(n, m, s, roads, scenarios):
    ret = [-1 for _ in range(0, s)]
    delta = fwa(n, roads)
    count = 0
    vertex = list(range(n))
    for sn in scenarios:
        unmarked = [ele for ele in vertex if ele not in sn]
        d_dash = dash(n, sn, delta)
        maxDist = [np.inf for _ in range(n)]
        d = [0 for _ in range(n)]
        for j in unmarked:
            for kn in range(n):
                d[kn] = min(d_dash[kn], delta[j][kn])
            maxDist[j] = max(d)
        maxDist = np.array(maxDist)
        ret[count] = max(list(np.where(maxDist == min(maxDist))[0]))
        count = count + 1
    return ret


# Reads the input
astr = sys.stdin.readline().split()
n = int(astr[0])
m = int(astr[1])
s = int(astr[2])
sys.stdin.readline()
# Read roads
roads = [(-1, -1) for _ in range(m)]
for i in range(m):
    astr = sys.stdin.readline().split()
    roads[i] = (int(astr[0]), int(astr[1]))
sys.stdin.readline()
# Read scenarios
scenarios = [(-1, []) for _ in range(s)]
for i in range(s):
    astr = sys.stdin.readline().split()
    k = int(astr[0])
    scenarios[i] = [int(v) for v in astr[1:k + 1]]

# Calls your funcion
ret = buildCastle(n, m, s, roads, scenarios)

# Writes the output
for i in range(0, s):
    print(ret[i])
