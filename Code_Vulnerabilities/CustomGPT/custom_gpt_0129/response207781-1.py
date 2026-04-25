
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison for min-heap

class AStar:
    def aStar(self, current, end):
        openSet = {}  # Dictionary for nodes in the open set
        openHeap = []  # Priority queue for paths
        closedSet = set()  # Set for closed nodes

        startNode = Node(0, current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)  # Mark current node as evaluated

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue  # Skip evaluated nodes

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                    openSet[tile.pos] = tile  # Update open set
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    # Get directions method remains unchanged
    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    # Adjacent nodes method remains similar, but only with defined moves
    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

# Implementation of heuristic functions
def manHatDist(self, pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidDist(self, pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

# This would require integration with your existing methods like canMove and getLocIfMove.
