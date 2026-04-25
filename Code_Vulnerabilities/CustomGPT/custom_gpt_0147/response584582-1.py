
import random
import math

# Dimensions
w, h = 9, 10
network = [[0 for x in range(w+2)] for y in range(h)]  # +2 for output and cost

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    output = (
        sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
        (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
        (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))
    network[x][w] = output  # Store output in the last index of network row

def seed():
    for b in range(h):
        for y in range(w):
            network[b][y] = random.random()  # Random weights

def calall():
    for c in range(h):
        netcal(c)
        print("Output for network {}: {}".format(c, network[c][w]))

def cost():
    for d in range(h):
        network[d][w+1] = 1 - network[d][w]  # Calculate cost
        print("Cost for network {}: {}".format(d, network[d][w+1]))

def sort():
    network.sort(key=lambda x: x[w+1])  # Sort based on cost (last index)

# Parameters
i1, i2 = 0, 1

# Execution
seed()
calall()
print("Calculating costs...")
cost()
print("Sorting networks by cost...")
sort()
print("Sorted networks:")
for row in network:
    print(row)
