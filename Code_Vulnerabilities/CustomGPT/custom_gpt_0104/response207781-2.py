
import heapq

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # Min-heap for lowest cost node retrieval
    closedSet = set() # Visited nodes
    startNode = Node(None, current, 0)  # Create the start node
    startNode.heuristic = self.manHatDist(current, end)  # Calculate heuristic

    # Initialize the open set and add the start node
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.heuristic, startNode))

    while openHeap:
        # Get the node with the lowest f-cost
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            tentative_g_score = curNode.cost + self.euclidDist(curNode.pos, tile.pos)

            if tile not in openSet:
                tile.parent = curNode
                tile.cost = tentative_g_score
                tile.heuristic = tentative_g_score + self.manHatDist(tile.pos, end)
                openSet.add(tile)
                heapq.heappush(openHeap, (tile.heuristic, tile))
            elif tentative_g_score < tile.cost:  # Check for a better path
                tile.parent = curNode
                tile.cost = tentative_g_score
                # Update the heap
                # Reinsert the node in the heap to be considered again
                heapq.heappush(openHeap, (tile.heuristic, tile))

    return []
