
class LineBasedFileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()

        # Seek to the beginning to iterate through lines
        self.f.seek(0)
        lc = 0  # line count
        remaining = current_position  # remaining bytes to process

        for line in self.f:
            line_length = len(line)
            if remaining >= line_length:
                remaining -= line_length
                lc += 1
            else:
                break

        # Reset the pointer back to the original position
        self.f.seek(current_position)

        if char:
            return lc, remaining
        return lc

    def close(self):
        # Don't forget to close the file
        self.f.close()

# Example usage
editor = LineBasedFileEditor('example.txt')
line_count = editor.tell()
print(f"Number of lines before current position: {line_count}")
editor.close()
