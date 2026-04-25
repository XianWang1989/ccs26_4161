
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return (self.cost) < (other.cost)

class AStar:
    def aStar(self, current, end):
        openSet = set()  # Set of explorable nodes
        openHeap = []    # All paths heap, lowest cost on top
        closedSet = set() # Visited nodes
        startNode = Node('', current, 0)
        openSet.add(startNode)
        heapq.heappush(openHeap, (0, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in closedSet:
                    tentative_cost = curNode.cost + 1  # Assuming all moves have equal cost
                    if tile not in openSet or tentative_cost < tile.cost:
                        tile.parent = curNode
                        tile.cost = tentative_cost + self.manhattanDist(tile.pos, end)
                        if tile not in openSet:
                            openSet.add(tile)
                            heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def manhattanDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Implement canMove and getLocIfMove methods
