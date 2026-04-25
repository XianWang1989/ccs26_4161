
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison

class AStar:
    def aStar(self, current, end):
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap
        closedSet = {}    # Track best path costs
        curNode = Node('', current, self.manHatDist(current, end))

        openSet.add(curNode)
        heapq.heappush(openHeap, (curNode.cost, curNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet[curNode.pos] = curNode.cost

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet and closedSet[tile.pos] <= tile.cost:
                    continue  # Skip if already found a better path

                tile.parent = curNode
                tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

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
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def canMove(self, direction, curPos):
        # Implement your movement logic based on the grid
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement logic to get the new position after a move
        pass
