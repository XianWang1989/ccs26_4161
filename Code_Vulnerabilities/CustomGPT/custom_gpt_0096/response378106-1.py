
def tell(self, char=False):
    # Store the current position
    current_position = self.f.tell()
    line_count = 0
    remaining = current_position

    # Go back to the beginning of the file to read lines
    self.f.seek(0)

    # Read the file line by line
    for line in self.f:
        line_length = len(line)

        if remaining >= line_length:
            remaining -= line_length
            line_count += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_position)

    if char:
        return line_count, remaining
    return line_count
