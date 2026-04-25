
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
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in closedSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
