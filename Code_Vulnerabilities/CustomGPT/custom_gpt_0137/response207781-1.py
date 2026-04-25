
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Properly implement less than

class YourClass:
    def aStar(self, current, end):
        openSet = {}   # Using a dictionary for the open set
        openHeap = []  # The min-heap for maintaining the lowest cost on top

        startNode = Node('', current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, (startNode.cost, startNode))

        closedSet = set()

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                if tile.pos not in openSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(current, tile.pos)
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))
                else:
                    # If the node is already in openSet, check if this path is better
                    existingNode = openSet[tile.pos]
                    newCost = self.euclidDist(current, tile.pos) + self.manHatDist(tile.pos, end)
                    if newCost < existingNode.cost:
                        existingNode.parent = curNode
                        existingNode.cost = newCost
                        heapq.heappop(openHeap)  # Remove the old entry
                        heapq.heappush(openHeap, (existingNode.cost, existingNode))  # Push the updated node

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    # Other methods remain unchanged...
