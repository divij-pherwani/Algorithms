import sys
import numpy as np

def DP(D, i, j, m, attack, weapon, gold):
    var = i - 1
    temp = D[var][j]
    for x in range(m):
        if (attack[i][x] == j) or (weapon[i][x] == j):
            temp = max(temp, D[var][attack[i][x]] + gold[i][x])
    return temp


def huntForGold(n, m, k, h, attack, weapon, gold, city):
    ret = [0 for x in range(h)]
    D = np.zeros(shape=(n,k))
    for i in range(n):
        for j in range(k):
            D[i][j] = DP(D, i,j,m,attack, weapon, gold)

    count = 0
    for l in city:
        ret[count] = int(max(D[l]))
        count = count+1
    return ret


# Use the following code when submitting
# your solution to the Szkopul webserver.

# Reads the input
astr = sys.stdin.readline().split()
n = int(astr[0])
m = int(astr[1])
k = int(astr[2])
h = int(astr[3])
attack = [[0 for x in range(m)] for y in range(n)]
weapon = [[0 for x in range(m)] for y in range(n)]
gold = [[0 for x in range(m)] for y in range(n)]
city = [0 for y in range(h)]
sys.stdin.readline()
# Read attack
for i in range(0, n):
    astr = sys.stdin.readline().split()
    attack[i] = [int(s) for s in astr[0:m]]
sys.stdin.readline()
# Read weapon
for i in range(0, n):
    astr = sys.stdin.readline().split()
    weapon[i] = [int(s) for s in astr[0:m]]
sys.stdin.readline()
# Read gold
for i in range(0, n):
    astr = sys.stdin.readline().split()
    gold[i] = [int(s) for s in astr[0:m]]
sys.stdin.readline()
# Read city
for i in range(0, h):
    astr = sys.stdin.readline().split()
    city[i] = int(astr[0])
# Calls your funcion
ret = huntForGold(n, m, k, h, attack, weapon, gold, city)
# Writes the output
for i in range(0, h):
    print(ret[i])