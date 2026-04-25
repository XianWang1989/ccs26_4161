
def tell(self, char=False):
    # Store the current file position
    t = self.f.tell()

    # Seek to the beginning of the file to iterate over lines
    self.f.seek(0)

    lc = 0  # Line count
    while True:
        line = self.f.readline()  # Read one line at a time
        if not line:  # Break if we reach the end of the file
            break
        if t >= len(line):
            t -= len(line)  # Reduce the byte count by the line length
            lc += 1  # Increase line count
        else:
            break

    # Reset the file position to the original
    self.f.seek(t + (0 if t == 0 else 1))  # Adjust to return to the right position

    if char:
        return lc, t
    return lc
