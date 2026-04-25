
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison logic

class Pathfinding:
    def aStar(self, current, end):
        openHeap = []  # Use priority queue as open set
        closedSet = set()  # Set for closed nodes

        startNode = Node(0, current, self.manHatDist(current, end))
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue  # Skip already explored nodes

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(current, tile.pos)

                # Check if this path is better
                if not any(tile.pos == n[1].pos and tile.cost >= n[1].cost for n in openHeap):
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
        directions = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in directions:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))  # Cost set to 0; recalculated during evaluation
        return posMoves

    # Placeholder methods; implement as necessary
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def canMove(self, direction, curPos):
        # Implement movement validation
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement position calculation based on direction
        pass
