
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison for the priority queue

class AStar:
    def aStar(self, current, end):
        openSet = {}  # Use a dictionary to store nodes and their costs
        openHeap = []  # Min-heap for A* nodes to explore
        closedSet = set()  # Set of visited nodes
        curNode = Node(0, current, self.manHatDist(current, end))

        openSet[curNode.pos] = curNode
        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            del openSet[curNode.pos]

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue  # Skip already evaluated nodes

                tentative_cost = curNode.cost + self.manHatDist(curNode.pos, tile.pos)
                if tile.pos not in openSet or tentative_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost

                    if tile.pos not in openSet:
                        openSet[tile.pos] = tile
                        heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    # Dummy placeholder methods for demonstration purposes
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def canMove(self, direction, pos):
        # Placeholder method - implement your movement logic
        return True

    def getLocIfMove(self, pos, direction):
        # Placeholder method - implement your movement logic
        return (pos[0] + (direction == 'East') - (direction == 'West'),
                pos[1] + (direction == 'South') - (direction == 'North'))

