
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

class AStarSearch:
    def aStar(self, current, end):
        open_set = set()
        open_heap = []
        closed_set = set()
        start_node = Node(0, current, self.manHatDist(current, end))

        open_set.add(start_node)
        heapq.heappush(open_heap, (start_node.cost, start_node))

        while open_heap:
            cur_node = heapq.heappop(open_heap)[1]
            if cur_node.pos == end:
                return self.getDirections(cur_node)

            open_set.remove(cur_node)
            closed_set.add(cur_node)

            for tile in self.getAdjacentNodes(cur_node.pos):
                if tile in closed_set:
                    continue

                g_cost = cur_node.cost + self.euclidDist(cur_node.pos, tile.pos)
                tile.cost = g_cost + self.manHatDist(tile.pos, end)

                if tile not in open_set or g_cost < tile.cost:
                    tile.parent = cur_node
                    if tile not in open_set:
                        open_set.add(tile)
                        heapq.heappush(open_heap, (tile.cost, tile))

        return []

    def getDirections(self, end_node):
        moves = []
        while end_node:
            moves.append(end_node.value)
            end_node = end_node.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, cur_pos):
        all_moves = ['North', 'South', 'East', 'West']
        pos_moves = []
        for direction in all_moves:
            if self.canMove(direction, cur_pos):
                pos_moves.append(Node(direction, self.getLocIfMove(cur_pos, direction), 0))
        return pos_moves

    # Placeholder for distance functions
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

    def canMove(self, direction, cur_pos):
        # Implement movement logic
        pass

    def getLocIfMove(self, cur_pos, direction):
        # Implement logic to get new position based on direction
        pass
