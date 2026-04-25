
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    # Calculate the output of the network
    output = (sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                      (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                      (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))
    network[x].append(output)  # Append the output to the network

def seed():
    for b in range(10):  # Seed random weights
        for y in range(9):
            network[b][y] = random.random()

def calall():
    for c in range(9):
        netcal(c)
        print(network[c][9])  # Output of the network

def cost():
    for d in range(9):
        network[d].append(1 - network[d][9])  # Calculate and append cost
        print(network[d][10])  # Cost

def sort():
    global network  # Make sure to modify the global network variable
    network = sorted(network, key=lambda x: x[10])  # Sort and assign back to network

# Initialize input values
i1 = 0
i2 = 1

seed()
calall()
print("break")
cost()
sort()
print(network)  # The sorted network
