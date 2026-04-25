
def tell(self, char=False):
    t = self.f.tell()
    self.f.seek(0)  # Go to the start of the file
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line counter

    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    self.f.seek(t)  # Reset the file pointer back to the original position
    if char:
        return lc, t
    return lc
