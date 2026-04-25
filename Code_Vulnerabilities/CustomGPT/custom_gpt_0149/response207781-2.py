
for tile in self.getAdjacentNodes(curNode.pos):
    if tile not in closedSet:
        tile.parent = curNode
        tile.cost = curNode.cost + self.manHatDist(tile.pos, end)  # Use Manhattan distance for tile
