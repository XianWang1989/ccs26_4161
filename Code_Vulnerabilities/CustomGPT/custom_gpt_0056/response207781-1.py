
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Use cost comparison for heapq

class AStarSearch:
    def aStar(self, current, end):
        openSet = set()  # Set of explorable nodes
        openHeap = []    # Min-heap for node exploration
        closedSet = {}    # Dictionary for best path so far
        curNode = Node("", current, self.manHatDist(current, end))
        openSet.add(curNode.pos)
        heapq.heappush(openHeap, (curNode.cost, curNode))

        while openHeap:
            _, curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode.pos)
            closedSet[curNode.pos] = curNode  # Update the closed set

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                if tile.pos not in openSet:
                    openSet.add(tile.pos)
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

    # Define your heuristic functions here
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
