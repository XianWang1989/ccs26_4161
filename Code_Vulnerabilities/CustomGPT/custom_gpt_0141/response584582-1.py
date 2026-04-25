
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    # Calculate the output and append to the current network array
    output = sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                     (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                     (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8]))
    network[x].append(output)

def seed():
    for b in range(10):
        for y in range(9):
            network[b][y] = random.random()

def calall():
    for c in range(9):
        netcal(c)
        print(network[c][9])

def cost():
    for d in range(9):
        network[d].append(1 - network[d][9])
        print(network[d][10])

def sort_network():
    # Sort the network in place by the last item (cost)
    network.sort(key=lambda x: x[10])

# Initialize inputs
i1 = 0
i2 = 1

# Run the functions
seed()
calall()
print("Break")
cost()
sort_network()  # Sort the network array
print(network)
