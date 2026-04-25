
def tell(self, char=False):
    t = self.f.tell()  # Get current byte position
    self.f.seek(0)  # Go back to the beginning of the file
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line count

    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    self.f.seek(t)  # Restore the original position
    if char:
        return lc, t
    return lc
