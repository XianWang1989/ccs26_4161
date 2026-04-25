
if tile not in openSet or tile.cost < existing_node_cost:  # Ensure to find existing node cost
    openSet.add(tile)
    heapq.heappush(openHeap, (tile.cost, tile))
