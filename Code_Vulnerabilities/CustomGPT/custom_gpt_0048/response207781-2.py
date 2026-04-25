
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarPathfinder:
    def aStar(self, current, end):
        openHeap = []
        openSet = {}  # Using a dictionary for quick lookups
        closedSet = set()

        startNode = Node(None, current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.pop(curNode.pos)  # Remove from open set
            closedSet.add(curNode.pos)  # Add to closed set

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue  # Skip if already evaluated

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + (curNode.cost + 1)  # +1 for movement cost

                if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)  # add/update in priority queue

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        # Your existing implementation remains
        # ...

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
