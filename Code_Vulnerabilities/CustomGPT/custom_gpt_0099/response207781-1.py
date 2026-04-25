
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarSearch:
    def aStar(self, current, end):
        openSet = set()  # Set of explorable nodes
        openHeap = []    # All paths heap, lowest cost on top
        closedSet = set() # Best path so far
        curNode = Node(None, current, self.manHatDist(current, end))

        openSet.add(curNode)
        heapq.heappush(openHeap, (curNode.cost, curNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode is not None:
            if tmpNode.value is not None:
                moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                new_pos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, new_pos, 0))
        return posMoves

    # Placeholder for distance calculations
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def canMove(self, direction, pos):
        # Implement movement logic here
        pass

    def getLocIfMove(self, pos, direction):
        # Return new position based on direction
        pass
