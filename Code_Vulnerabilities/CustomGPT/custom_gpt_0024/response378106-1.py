
def tell(self, char=False):
    # Store the current position
    current_position = self.f.tell()

    # To hold the line count and adjusted position
    lc, t = 0, current_position

    # Seek back to the beginning
    self.f.seek(0)

    # Iterate through each line in the file
    for line in self.f:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_position)

    if char:
        return lc, t
    return lc
