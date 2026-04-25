
def tell(self, char=False):
    # Save the current file position
    current_position = self.f.tell()
    line_count = 0
    self.f.seek(0)  # Reset to the beginning of the file

    try:
        for line in self.f:
            if current_position >= len(line):
                current_position -= len(line)
                line_count += 1
            else:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Reset back to the original position after reading
        self.f.seek(current_position)

    if char:
        return line_count, current_position
    return line_count
