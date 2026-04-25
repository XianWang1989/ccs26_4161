class Node:
    def __init__(self, value, pos, g, h):
        self.value = value
        self.pos = pos
        self.g = g
        self.h = h
        self.cost = g + h
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)


def aStar(self, start, end):
    startNode = Node(None, start, 0, self.manHatDist(start, end))
    openSet = {startNode}
    openHeap = [(startNode.cost, startNode)]
    closedSet = set()

    while openHeap:
        _, current = heapq.heappop(openHeap)
        if current.pos == end:
            return self.getDirections(current)

        openSet.discard(current)
        closedSet.add(current)

        for neighbor in self.getAdjacentNodes(current.pos):
            if neighbor in closedSet:
                continue

            neighbor.g = current.g + 1
            neighbor.h = self.manHatDist(neighbor.pos, end)
            neighbor.cost = neighbor.g + neighbor.h
            neighbor.parent = current

            if neighbor not in openSet:
                openSet.add(neighbor)
                heapq.heappush(openHeap, (neighbor.cost, neighbor))

    return []
