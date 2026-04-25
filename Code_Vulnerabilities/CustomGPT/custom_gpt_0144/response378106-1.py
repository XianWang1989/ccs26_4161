def tell(self, char=False):
    t = self.f.tell()
    self.f.seek(0)
    lc = 0
    pos = 0

    while True:
        line = self.f.readline()
        if not line:
            break
        if t >= pos + len(line):
            pos += len(line)
            lc += 1
        else:
            break

    if char:
        return lc, t - pos
    return lc
