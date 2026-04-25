
import heapq

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    closedSet = {}    # Dict to track best cost for closed nodes
    startNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet[curNode.pos] = curNode.cost

        for tile in self.getAdjacentNodes(curNode.pos):
            newCost = curNode.cost + self.manHatDist(tile.pos, end)

            if tile.pos in closedSet and closedSet[tile.pos] <= newCost:
                continue

            if tile not in openSet or newCost < tile.cost:
                tile.parent = curNode
                tile.cost = newCost
                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
