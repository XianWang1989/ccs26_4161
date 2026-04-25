
def tell(self, char=False):
    t = self.f.tell()  # Get the current position
    self.f.seek(0)     # Move to the start of the file
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line counter

    # Calculate the line and position
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    self.f.seek(t)  # Restore the original file position

    if char:
        return lc, t  # Return line count and character position
    return lc  # Return only line count
