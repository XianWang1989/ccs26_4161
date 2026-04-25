
def tell(self, char=False):
    t = self.f.tell()
    self.f.seek(0)
    lines = self.f.readlines()  # read lines once
    lc = 0

    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break
    self.f.seek(t)  # reset back to the original position

    if char:
        return lc, t
    return lc
