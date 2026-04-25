
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

# A* search algorithm
def aStar(self, current, end):
    openSet = set()       # Set of explorable nodes
    openHeap = []         # Priority queue (heap) for the lowest cost node
    closedSet = {}        # Dictionary for the best path so far
    start_node = Node('', current, self.manHatDist(current, end))
    openSet.add(start_node)
    heapq.heappush(openHeap, (start_node.cost, start_node))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]  # Get the lowest cost node
        if curNode.pos == end:
            return self.getDirections(curNode)  # Path found

        openSet.remove(curNode)
        closedSet[curNode.pos] = curNode  # Track closed nodes

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue  # Ignore if already evaluated

            tile.parent = curNode
            tile.cost = (self.manHatDist(tile.pos, end) + 
                          self.euclidDist(tile.pos, current) + 
                          curNode.cost)

            # If this node is not in openSet, add it
            if tile not in openSet:
                openSet.add(tile)
                heapq.heappush(openHeap, (tile.cost, tile))
            else:
                # If tile already in openSet, check if the new cost is better
                existing_node = closedSet[tile.pos]
                if tile.cost < existing_node.cost:
                    # Update parent and cost
                    existing_node.parent = curNode
                    existing_node.cost = tile.cost
                    # Re-add node to the heap (requires re-heapifying)
                    heapq.heappop(openHeap)  # Remove old entry
                    heapq.heappush(openHeap, (existing_node.cost, existing_node))

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost is set via A*
    return posMoves
