
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # fixes comparison behavior

class AStar:
    def aStar(self, current, end):
        openHeap = []  # All paths heap, lowest cost on top
        closedSet = set()  # Best path so far

        startNode = Node("", current, self.manHatDist(current, end))
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)  # Modify to keep track of positions

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                # Calculate new cost and check for existing nodes
                new_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
                if not any(existing.pos == tile.pos and existing.cost <= new_cost for _, existing in openHeap):
                    tile.cost = new_cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode
                    heapq.heappush(openHeap, (tile.cost, tile))

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
                posMoves.append(Node(direction, newPos, 0))  # Simplified cost
        return posMoves
