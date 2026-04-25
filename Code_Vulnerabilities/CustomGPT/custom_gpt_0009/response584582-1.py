
def sort():
    global network  # Use global to modify the outer `network` variable
    network = sorted(network, key=lambda x: x[10])
