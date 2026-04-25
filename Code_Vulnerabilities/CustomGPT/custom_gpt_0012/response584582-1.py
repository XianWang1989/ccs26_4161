
def sort():
    global network  # Add this line to make sure you modify the global variable
    network = sorted(network, key=lambda x: x[10])  # Assign the sorted list back to network
