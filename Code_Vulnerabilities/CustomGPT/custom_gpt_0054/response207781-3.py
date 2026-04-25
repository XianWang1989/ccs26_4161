
import heapq

def aStar(self, current, end):
    openSet = {}  # Map of position to Node
    openHeap = []  # Min-heap for exploring nodes
    closedSet = set()  # Explored nodes

    curNode = Node(0, current, self.manHatDist(current, end))
    openSet[current] = curNode
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in closedSet:
                new_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
                if tile.pos not in openSet or new_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = new_cost
                    if tile.pos not in openSet:
                        openSet[tile.pos] = tile
                        heapq.heappush(openHeap, (tile.cost + self.manHatDist(tile.pos, end), tile))

    return []
