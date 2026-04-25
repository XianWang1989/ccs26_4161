
def tell(self, char=False):
    # Store all lines in a list
    self.f.seek(0)  # Ensure we start reading from the beginning
    lines = self.f.readlines()

    t = self.f.tell()  # Get the current byte position
    lc = 0  # Line count

    # Calculate the line number
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Return line count and remaining bytes if required
    if char:
        return lc, t
    return lc
