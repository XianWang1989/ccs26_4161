
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison

class AStarSearch:
    def aStar(self, current, end):
        openSet = set()
        openHeap = []
        closedSet = set()
        curNode = Node(0, current, self.manHatDist(current, end))
        openSet.add(curNode)
        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)
            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in closedSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                    if tile not in openSet:
                        openSet.add(tile)
                        heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newLoc = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newLoc, 0))  # Cost is recalculated later
        return posMoves

    def manHatDist(self, current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def euclidDist(self, current, end):
        return ((current[0] - end[0]) ** 2 + (current[1] - end[1]) ** 2) ** 0.5

# Example usage
search = AStarSearch()
path = search.aStar((0, 0), (5, 5))
print(path)
