
import heapq

def aStar(self, current, end):
    openSet = {Node(0, current, 0)}
    openHeap = []
    closedSet = set()

    curNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            g_cost = curNode.cost + 1  # Assuming uniform cost for movements
            h_cost = self.manHatDist(tile.pos, end)
            tile.cost = g_cost + h_cost

            if tile not in openSet or tile.cost < curNode.cost: 
                tile.parent = curNode
                openSet.add(tile)
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
