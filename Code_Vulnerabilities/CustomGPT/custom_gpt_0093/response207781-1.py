
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
                if tile.pos in [n.pos for n in openSet] or tile.pos in [n.pos for n in closedSet]:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                openSet.add(tile)
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
                new_pos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, new_pos, 0))

        return posMoves
