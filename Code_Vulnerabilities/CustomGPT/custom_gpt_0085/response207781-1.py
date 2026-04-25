
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
    open_set = {}  # Dictionary to store nodes in the open set
    open_heap = []  # Heap for prioritizing nodes
    closed_set = set()  # Set of closed nodes

    start_node = Node(0, current, self.manHatDist(current, end))
    open_set[start_node.pos] = start_node
    heapq.heappush(open_heap, (start_node.cost, start_node))

    while open_heap:
        cur_node = heapq.heappop(open_heap)[1]

        if cur_node.pos == end:
            return self.getDirections(cur_node)

        del open_set[cur_node.pos]  # Remove current node from open set
        closed_set.add(cur_node.pos)  # Add current node to closed set

        for tile in self.getAdjacentNodes(cur_node.pos):
            if tile.pos in closed_set:
                continue

            # Update the parent and cost of the tile
            new_cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) 
            tile.cost = new_cost

            # If the tile is not in the open set or found a cheaper path
            if tile.pos not in open_set or new_cost < open_set[tile.pos].cost:
                tile.parent = cur_node

                if tile.pos not in open_set:
                    open_set[tile.pos] = tile
                    heapq.heappush(open_heap, (tile.cost, tile))

    return []

def getAdjacentNodes(self, curPos):
    all_moves = ['North', 'South', 'East', 'West']
    pos_moves = []
    for direction in all_moves:
        if self.canMove(direction, curPos):
            new_pos = self.getLocIfMove(curPos, direction)
            # Check if this node already exists in the open set
            pos_moves.append(Node(direction, new_pos, 0))
    return pos_moves

def getDirections(self, end_node):
    moves = []
    tmp_node = end_node
    while tmp_node.parent is not None:
        moves.append(tmp_node.value)
        tmp_node = tmp_node.parent
    moves.reverse()
    return moves
