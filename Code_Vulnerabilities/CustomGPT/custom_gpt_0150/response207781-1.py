
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def aStar(self, current, end):
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap, lowest cost on top
        closedSet = set() # Best path so far
        curNode = Node(None, current, self.manHatDist(current, end))

        heapq.heappush(openHeap, (curNode.cost, curNode))
        openSet.add(curNode)

        while openHeap:
            _, curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in closedSet:
                    new_cost = curNode.cost + self.manHatDist(tile.pos, end)
                    if tile not in openSet or new_cost < tile.cost:
                        tile.parent = curNode
                        tile.cost = new_cost
                        if tile not in openSet:
                            openSet.add(tile)
                            heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode:
            if endNode.value:  # Skip the initial node (no direction)
                moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            newPos = self.getLocIfMove(curPos, direction)
            if newPos is not None:
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def canMove(self, direction, curPos):
        # Implement movement logic based on your grid
        pass

    def manHatDist(self, posA, posB):
        # Implement Manhattan distance logic
        pass

    def getLocIfMove(self, curPos, direction):
        # Logic to calculate new position based on direction
        pass
