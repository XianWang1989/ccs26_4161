
def tell(self, char=False):
    # Save the current position
    pos = self.f.tell()
    self.f.seek(0)  # Move to the start for iteration
    lc = 0  # Initialize line count

    for line in self.f:
        if pos >= len(line):
            pos -= len(line)
            lc += 1
        else:
            break

    self.f.seek(pos)  # Restore to the original position

    if char:
        return lc, pos
    return lc
