
import heapq

def aStar(self, current, end):
    openSet = {}  # Dictionary for open nodes
    openHeap = [] # List for min-heap
    closedSet = set() # Set for already explored nodes
    curNode = Node(0, current, self.manHatDist(current, end))
    openSet[curNode.pos] = curNode
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode.pos) # Remove from open set
        closedSet.add(curNode)    # Add to closed set

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tile.parent = curNode
                tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

                # Only add/update the tile if it's not in openSet or has lower cost
                if tile.pos not in openSet or openSet[tile.pos].cost > tile.cost:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
