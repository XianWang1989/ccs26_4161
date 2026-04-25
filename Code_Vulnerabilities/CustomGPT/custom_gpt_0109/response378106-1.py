
def tell(self, char=False):
    # Get the current position
    current_pos = self.f.tell()
    # Seek to the start of the file
    self.f.seek(0)

    # Read all lines into a list
    lines = self.f.readlines()

    line_count = 0
    position_within_line = current_pos

    # Calculate the line count and position
    for line in lines:
        if position_within_line >= len(line):
            position_within_line -= len(line)
            line_count += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_pos)

    if char:
        return line_count, position_within_line
    return line_count
