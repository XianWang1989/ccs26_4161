
import heapq

def aStar(self, current, end):
    openSet = {}
    openHeap = []
    closedSet = set()

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[startNode] = startNode.cost
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tile.parent = curNode
                tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

                if tile not in openSet or tile.cost < openSet[tile]:
                    openSet[tile] = tile.cost
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
