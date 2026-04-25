
if tile not in openSet or tile.cost < openSet[tile]:
    openSet[tile] = tile.cost
    heapq.heappush(openHeap, (tile.cost, tile))
