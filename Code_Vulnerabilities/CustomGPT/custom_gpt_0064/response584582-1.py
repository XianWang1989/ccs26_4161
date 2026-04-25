
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    # Example values for i1 and i2
    net_output = sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6])
                         + (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7])
                         + (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8]))
    network[x].append(net_output)

def seed():
    for b in range(10):
        for y in range(9):
            network[b][y] = random.random()

def calall():
    for c in range(9):
        netcal(c)

def cost():
    for d in range(9):
        network[d].append(1 - network[d][9])  # Adjust index if needed

def sort_network():
    network.sort(key=lambda x: x[10])  # Sort in place

# Main execution
i1 = 0
i2 = 1

seed()
calall()
cost()
sort_network()  # Sort after calculations
print(network)
