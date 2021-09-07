import sys


def trackerApp(n, d, event):
    ret = [""] * n
    position = dict()
    pairs = 0

    for k, i in enumerate(event):
        if i[0] == 1:
            # Adding element
            position[i[1]] = "Value"
            # Adding number of pairs formed using the element
            pairs = pairs + int((i[1] + d) in position) + int((i[1] - d) in position)

        elif i[0] == -1:
            # Removing element
            del position[i[1]]
            # Removing number of pairs formed using the element
            pairs = pairs - int((i[1] + d) in position) - int((i[1] - d) in position)

        # Final events
        if pairs >= 1:
            ret[k] = "red"
        else:
            ret[k] = "yellow"

    del position
    del pairs
    return ret


# Reads the input
astr = sys.stdin.readline().split()
n = int(astr[0])
d = int(astr[1])
event = [[0 for _ in range(2)] for _ in range(n)]
# Read event
for i in range(0, n):
    astr = sys.stdin.readline().split()
    event[i] = [int(s) for s in astr[0:2]]

# Calls your function
ret = trackerApp(n, d, event)

# Writes the output
for i in range(0, n):
    print(ret[i])