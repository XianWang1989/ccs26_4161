
import heapq

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    closedSet = set() # Best path so far
    curNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(curNode)
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                if tile not in openSet or (tile in openSet and tile.cost < curNode.cost):
                    if tile in openSet:
                        openSet.remove(tile)
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
