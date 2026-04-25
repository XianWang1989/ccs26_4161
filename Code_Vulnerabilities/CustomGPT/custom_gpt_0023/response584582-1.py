
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    output = (sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                      (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                      (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))
    network[x].append(output)

def seed():
    for b in range(h):
        for y in range(w):
            network[b][y] = random.random()

def calall():
    for c in range(h):
        netcal(c)
        print(f"Output for network {c}: {network[c][9]}")

def cost():
    for d in range(h):
        error = 1 - network[d][9]
        network[d].append(error)
        print(f"Cost for network {d}: {network[d][10]}")

def sort_network():
    network.sort(key=lambda x: x[10])  # Sort in-place

# Main execution flow
i1 = 0
i2 = 1

seed()
calall()
print("Calculating costs...")
cost()
sort_network()
print("Sorted Network:\n", network)
