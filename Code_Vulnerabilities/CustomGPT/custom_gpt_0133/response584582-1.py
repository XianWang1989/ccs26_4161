
import random
import math

w, h = 9, 10
network = [[0 for x in range(w)] for y in range(h)]

def sigmoid(sigin):
    return 1 / (1 + math.exp(-sigin))

def netcal(x):
    network[x].append(sigmoid((sigmoid(i1 * network[x][0] + i2 * network[x][1]) * network[x][6]) +
                              (sigmoid(i1 * network[x][2] + i2 * network[x][3]) * network[x][7]) +
                              (sigmoid(i1 * network[x][4] + i2 * network[x][5]) * network[x][8])))

def seed():
    for b in range(h):  # Assuming you want to fill all h rows
        for y in range(w):  # Replacing the while loops with for loops for clarity
            network[b][y] = random.random()

def calall():
    for c in range(h):
        netcal(c)
        print(network[c][9])  # assuming index 9 will hold the network output

def cost():
    for d in range(h):
        network[d].append(1 - network[d][9])  # assuming index 9 holds the network output
        print(network[d][10])  # position after network output

def sort_network():
    # Sort the network in place
    network.sort(key=lambda x: x[10])  # Sorts the original list by the last value

i1 = 0
i2 = 1

seed()
calall()
print("Calculating costs...")
cost()
sort_network()  # Call the sort function to sort the list
print("Sorted network:", network)
