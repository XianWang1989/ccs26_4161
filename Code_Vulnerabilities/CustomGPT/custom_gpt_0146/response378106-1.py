
class LineFile:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()
        line_count = 0
        char_position = 0

        # Reset the file pointer to the beginning for line counting
        self.f.seek(0)

        # Read lines until we reach the saved position
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break
            line_length = len(line)
            if t >= char_position + line_length:
                char_position += line_length
                line_count += 1
            else:
                break

        # Return line count and optionally character position
        if char:
            return line_count, t - char_position
        return line_count

    def close(self):
        self.f.close()

# Usage
line_file = LineFile('example.txt')
print(line_file.tell())  # Prints the current line number
print(line_file.tell(char=True))  # Prints the current line number and character position
line_file.close()
