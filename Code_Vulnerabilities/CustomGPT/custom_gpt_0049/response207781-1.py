
import heapq

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openHeap = []  # Min-heap priority queue
    closedSet = set()  # Best path so far
    curNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        currentCost, curNode = heapq.heappop(openHeap)  # Get the node with the lowest cost

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue  # Skip already evaluated nodes

            tile.parent = curNode
            newCost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

            # If the tile is not in the open set add it
            if tile not in [n[1] for n in openHeap]:  
                tile.cost = newCost
                heapq.heappush(openHeap, (tile.cost, tile))
            else:
                # If we found a better path to tile, update its cost
                for i, (cost, n) in enumerate(openHeap):
                    if n == tile and newCost < n.cost:
                        n.cost = newCost
                        openHeap[i] = (n.cost, n)
                        heapq.heapify(openHeap)  # Reorder heap

    return []
