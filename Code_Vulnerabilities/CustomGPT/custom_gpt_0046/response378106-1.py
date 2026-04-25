
def tell(self, char=False):
    # Save the current position
    current_pos = self.f.tell()

    # Seek to the beginning of the file
    self.f.seek(0)

    # Read all lines into a list
    lines = self.f.readlines()

    lc = 0  # Line count
    t = current_pos  # Remaining position to check

    # Iterate over the lines
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_pos)

    if char:
        return lc, t
    return lc
