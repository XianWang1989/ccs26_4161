
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    output = sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                     (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                     (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8]))
    network[x].append(output)

def seed():
    for b in range(h):
        for y in range(w):
            network[b][y] = random.random()

def calall():
    for c in range(h):
        netcal(c)
        print(network[c][9])

def cost():
    for d in range(h):
        network[d].append(1 - network[d][9])
        print(network[d][10])

def sort_network():
    global network  # Make sure to update the global variable
    network = sorted(network, key=lambda x: x[10])  # Assign sorted list back to network

# Initialization
i1 = 0
i2 = 1

# Create and calculate networks
seed()
calall()
print("break")
cost()
sort_network()  # Call the sorting function
print(network)
