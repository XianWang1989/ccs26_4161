
import math
import random

w, h = 9, 10
network = [[0 for _ in range(w)] for _ in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    result = (sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                      (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                      (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))
    network[x].append(result)

def seed():
    for b in range(10):
        for y in range(9):
            network[b][y] = random.random()

def calall():
    for c in range(9):
        netcal(c)
        print(network[c][9])  # Print the output of the network

def cost():
    for d in range(9):
        network[d].append(1 - network[d][9])  # Append cost calculation
        print(network[d][10])  # Print the cost

def sort_network():
    global network  # Indicate that we are modifying the global network variable
    network = sorted(network, key=lambda x: x[10])  # Sort by the last element

# Entry point
i1 = 0
i2 = 1

seed()
calall()
print("break")
cost()
sort_network()  # Change to the corrected sorting function
print(network)  # Print the sorted network
