
import math
import random

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    network[x].append(sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                               (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                               (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))

def seed():
    b = 0
    while b < 10:
        y = 0
        while y < 9:
            network[b][y] = random.random()
            y += 1
        b += 1

def calall():
    c = 0
    while c < 9:
        netcal(c)
        print(network[c][9])
        c += 1

def cost():
    d = 0
    while d < 9:
        network[d].append(1 - network[d][9])
        print(network[d][10])
        d += 1

def sort_network():
    # Sort the network in place by the last element in each inner list (index 10)
    network.sort(key=lambda x: x[10])

# Main execution
i1 = 0
i2 = 1

seed()
calall()
print("break")
cost()
sort_network()  # Sort the network after calculating costs
print(network)
