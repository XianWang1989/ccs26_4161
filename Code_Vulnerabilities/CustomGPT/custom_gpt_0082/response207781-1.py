
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
        openSet = set()
        openHeap = []

        start_node = Node("", current, self.manHatDist(current, end))
        openSet.add(start_node)
        heapq.heappush(openHeap, (start_node.cost, start_node))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos not in openSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + curNode.cost
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        return moves[::-1]

    def getAdjacentNodes(self, curPos):
        directions = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in directions:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def manHatDist(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    # Assume the implementation for canMove and getLocIfMove are here
