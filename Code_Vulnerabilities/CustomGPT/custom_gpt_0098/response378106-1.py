
def tell(self, char=False):
    t = self.f.tell()  # Current position in bytes
    self.f.seek(0)  # Go back to the beginning of the file

    lc = 0  # Line count
    bytes_read = 0

    # Read through the file line by line
    for line in self.f:
        line_length = len(line)
        if bytes_read + line_length > t:
            break
        bytes_read += line_length
        lc += 1

    self.f.seek(t)  # Restore file cursor to the original position

    if char:
        # Remaining bytes in the current line
        return lc, t - bytes_read
    return lc
