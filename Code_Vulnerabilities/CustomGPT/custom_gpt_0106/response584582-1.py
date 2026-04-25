
import random
import math

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(index):
    network[index].append(sigmoid(
        (sigmoid(i1 * network[index][0] + i2 * network[index][1]) * network[index][6]) +
        (sigmoid(i1 * network[index][2] + i2 * network[index][3]) * network[index][7]) +
        (sigmoid(i1 * network[index][4] + i2 * network[index][5]) * network[index][8])
    ))

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
    network.sort(key=lambda x: x[10])

i1 = 0
i2 = 1

seed()
calall()
print("Break")
cost()
sort_network()
print(network)
