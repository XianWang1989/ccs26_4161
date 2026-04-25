
def tell(self, char=False):
    t = self.f.tell()  # Current position
    lc = 0  # Line count
    self.f.seek(0)  # Move back to the start of the file

    while True:
        line = self.f.readline()  # Read the next line
        if not line:  # If there's no more to read, break
            break
        line_length = len(line)

        if t >= line_length:
            t -= line_length  # Decrease t by the length of the line
            lc += 1  # Increment line count if we have fully consumed the line
        else:
            # If t is within the line, we stop counting here
            break

    # Restore the original position
    self.f.seek(t + sum(len(self.f.readline()) for _ in range(lc)))

    if char:
        return lc, t
    return lc
