
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Min-heap based on cost

class AStar:
    def __init__(self):
        self.closedSet = set()

    def aStar(self, current, end):
        openSet = set()
        openHeap = []

        startNode = Node('', current, self.manHatDist(current, end))
        openSet.add(startNode)
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            self.closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in self.closedSet:
                    new_cost = self.manHatDist(tile.pos, end) + curNode.cost
                    # Check if this path to the tile is better
                    if tile not in openSet or new_cost < tile.cost:
                        tile.parent = curNode
                        tile.cost = new_cost
                        if tile not in openSet:
                            openSet.add(tile)
                            heapq.heappush(openHeap, tile)

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
                posMoves.append(Node(direction, newPos, float('inf')))  # Use inf as initial cost
        return posMoves

    # Placeholder methods to be implemented
    def manHatDist(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    # Implement these methods based on your grid logic
    def canMove(self, direction, pos):
        # Logic for checking if a move is valid
        pass

    def getLocIfMove(self, curPos, direction):
        # Logic to return new position after move
        pass
