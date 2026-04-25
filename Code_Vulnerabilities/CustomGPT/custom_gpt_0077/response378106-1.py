
def tell(self, char=False):
    # Save the current position
    current_pos = self.f.tell()

    # Go back to the beginning to read lines
    self.f.seek(0)

    # Read lines until reaching the current position
    lc = 0  # line count
    for line in self.f:
        if current_pos <= len(line):
            break
        current_pos -= len(line)
        lc += 1

    # Restore the original position
    self.f.seek(current_pos)

    if char:
        return lc, current_pos
    return lc
