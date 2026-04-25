
import heapq

def aStar(self, current, end):
    openSet = {}  # Dictionary of explorable nodes
    openHeap = []  # All paths in a min-heap
    closedSet = set()
    curNode = Node(None, current, self.manHatDist(current, end))

    openSet[curNode.pos] = curNode
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
            if tile.pos not in openSet or tentative_cost < openSet[tile.pos].cost:
                tile.parent = curNode
                tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
