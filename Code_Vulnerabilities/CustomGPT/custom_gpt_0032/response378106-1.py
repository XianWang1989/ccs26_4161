
def tell(self, char=False):
    # Store current position
    current_position = self.f.tell()

    # Reset to the beginning of the file
    self.f.seek(0)

    # Initialize line count and adjusted position
    line_count = 0
    remaining_position = current_position

    # Iterate over lines in the file
    for line in self.f:
        line_length = len(line)
        if remaining_position >= line_length:
            remaining_position -= line_length
            line_count += 1
        else:
            break

    # Reset to the original position
    self.f.seek(current_position)

    if char:
        return line_count, remaining_position
    return line_count
