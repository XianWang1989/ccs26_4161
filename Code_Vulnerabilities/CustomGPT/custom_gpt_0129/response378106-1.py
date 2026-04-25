
def tell(self, char=False):
    # Store the current position
    current_position = self.f.tell()
    lc = 0  # Line count

    # Seek back to the start of the file
    self.f.seek(0)

    # Read lines and count them until reaching the original position
    for line in self.f:
        line_length = len(line)
        if current_position >= line_length:
            current_position -= line_length
            lc += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_position)

    if char:
        return lc, current_position
    return lc
