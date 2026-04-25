
import random
import math

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    output = (
        sigmoid((sigmoid(i1*network[x][0] + i2*network[x][1]) * network[x][6]) +
        (sigmoid(i1*network[x][2] + i2*network[x][3]) * network[x][7]) +
        (sigmoid(i1*network[x][4] + i2*network[x][5]) * network[x][8]))
    )
    network[x].append(output)

def seed():
    for b in range(h):
        for y in range(w):
            network[b][y] = random.random()

def calall():
    for c in range(h):
        netcal(c)
        print(network[c][9])  # This should print the output

def cost():
    for d in range(h):
        network[d].append(1 - network[d][9])  # Adding cost based on output
        print(network[d][10])  # This should print the cost

def sort():
    global network  # Use global to modify the global array
    network = sorted(network, key=lambda x: x[10])  # Sort the network based on the cost

# Set inputs
i1 = 0
i2 = 1

# Run the sequence
seed()
calall()
print("break")
cost()
sort()
print(network)
