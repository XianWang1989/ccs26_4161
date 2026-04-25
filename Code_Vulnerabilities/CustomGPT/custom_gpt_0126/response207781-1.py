
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
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap, lowest cost on top
        closedSet = set() # Best path so far

        startNode = Node(0, current, self.manHatDist(current, end))
        openSet.add(current)
        heapq.heappush(openHeap, (startNode.cost, startNode))

        costs = {current: 0}  # Store the best cost to reach each node

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode.pos)
            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                new_cost = costs[curNode.pos] + 1  # Assuming a uniform cost of 1 for each move

                if tile.pos not in costs or new_cost < costs[tile.pos]:
                    costs[tile.pos] = new_cost
                    tile.parent = curNode

                    if tile.pos not in openSet:
                        openSet.add(tile.pos)
                        tile.cost = new_cost + self.manHatDist(tile.pos, end)
                        heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getAdjacentNodes(self, curPos):
        allMoves = ['North','South','East','West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]

    # Placeholder for distance calculations
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def canMove(self, direction, curPos):
        # Implement movement logic based on direction
        pass

    def getLocIfMove(self, curPos, direction):
        # Return new position based on direction
        pass
