
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
        openSet = {}
        openHeap = []
        closedSet = {}

        startNode = Node(0, current, self.manHatDist(current, end))
        openSet[startNode.pos] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            del openSet[curNode.pos]  # Remove from open set

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet[curNode.pos] = curNode

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                # Calculate cost
                g_cost = curNode.cost + 1  # Assuming uniform cost for each movement
                h_cost = self.manHatDist(tile.pos, end)
                tile.cost = g_cost + h_cost
                tile.parent = curNode

                # Only add to open set if it's not already there
                if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                    openSet[tile.pos] = tile
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
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def canMove(self, direction, pos):
        # Implement movement logic
        pass

    def getLocIfMove(self, pos, direction):
        # Return new position after move
        pass
