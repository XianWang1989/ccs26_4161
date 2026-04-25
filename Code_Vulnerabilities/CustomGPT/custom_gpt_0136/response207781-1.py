
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()
    startNode = Node(None, current, 0)
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openSet:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tentative_g_score = curNode.cost + 1  # Assuming uniform cost
                if tile not in openSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + tentative_g_score
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))
                else:
                    # If this path is faster, update cost and parent
                    if tentative_g_score < tile.cost:
                        tile.parent = curNode
                        tile.cost = tentative_g_score
                        # Since costs have changed, we need to re-sort the heap
                        heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode:
        if tmpNode.value:
            moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
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
