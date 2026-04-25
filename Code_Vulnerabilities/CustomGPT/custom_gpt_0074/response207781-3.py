
openSet = {}  # use a dictionary to map node positions to Node
if tile.pos not in openSet or openSet[tile.pos].cost > tile.cost:
    openSet[tile.pos] = tile
