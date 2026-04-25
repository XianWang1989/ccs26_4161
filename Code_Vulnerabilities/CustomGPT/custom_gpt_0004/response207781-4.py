
import heapq

def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()
    startNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            tile.parent = curNode
            tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

            if tile not in openSet or tile.cost < [n.cost for n in openHeap if n[1] == tile][0]:
                openSet.add(tile)
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
