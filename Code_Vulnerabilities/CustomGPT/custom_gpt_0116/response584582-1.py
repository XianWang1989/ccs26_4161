
import random
import math

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
    for c in range(w):
        netcal(c)

def cost():
    for d in range(w):
        network[d].append(1 - network[d][9])

def sort_network():
    # Use sorted() to sort the network by the last item in each array and assign back to network
    global network
    network = sorted(network, key=lambda x: x[10])

# Initialize
i1 = 0
i2 = 1

# Run the functions
seed()
calall()
print("Outputs before cost calculation:")
for row in network:
    print(row)

cost()
sort_network()

print("Sorted network:")
for row in network:
    print(row)
