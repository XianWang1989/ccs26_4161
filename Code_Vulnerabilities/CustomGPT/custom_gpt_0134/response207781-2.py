
import heapq

def aStar(self, current, end):
    openHeap = []
    openSet = {}  # Node -> cost
    closedSet = set()

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[startNode] = startNode.cost
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode)
        del openSet[curNode]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

            if tile not in openSet or tile.cost < openSet[tile]:
                openSet[tile] = tile.cost
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
