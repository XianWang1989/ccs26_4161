
def tell(self, char=False):
    # Save the current position
    current_position = self.f.tell()

    # Seek to the start of the file
    self.f.seek(0)

    lc = 0  # Line count
    t = current_position  # The position to find in line count

    # Iterate over each line
    for line in self.f:
        if t >= len(line):
            t -= len(line)  # Decrease the target position by the length of the line
            lc += 1  # Increase the line count
        else:
            break  # Break if we have found the line

    # Seek back to the original position
    self.f.seek(current_position)

    # Return the result based on the char flag
    if char:
        return lc, t
    return lc
