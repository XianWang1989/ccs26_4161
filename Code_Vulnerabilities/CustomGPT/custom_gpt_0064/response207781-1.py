
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison

class AStar:
    def aStar(self, current, end):
        open_set = {}      # Use a dictionary for open nodes
        open_heap = []     # Min-heap for exploring paths
        closed_set = set() # Explored nodes

        cur_node = Node('', current, self.manHatDist(current, end))
        open_set[current] = cur_node
        heapq.heappush(open_heap, (cur_node.cost, cur_node))

        while open_heap:
            cur_node = heapq.heappop(open_heap)[1]

            if cur_node.pos == end:
                return self.getDirections(cur_node)

            del open_set[cur_node.pos]
            closed_set.add(cur_node.pos)

            for tile in self.getAdjacentNodes(cur_node.pos):
                if tile.pos in closed_set:
                    continue

                # Use Manhattan distance only once
                tile_cost = self.manHatDist(tile.pos, end) + cur_node.cost + 1

                # Check if tile is not in open_set or if a better cost is found
                if tile.pos not in open_set or tile_cost < tile.cost:
                    tile.parent = cur_node
                    tile.cost = tile_cost
                    open_set[tile.pos] = tile
                    heapq.heappush(open_heap, (tile_cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]  # Reverse the list

    def getAdjacentNodes(self, curPos):
        all_moves = ['North', 'South', 'East', 'West']
        pos_moves = []
        for direction in all_moves:
            if self.canMove(direction, curPos):
                new_pos = self.getLocIfMove(curPos, direction)
                pos_moves.append(Node(direction, new_pos, 0))  # Cost is set later
        return pos_moves
