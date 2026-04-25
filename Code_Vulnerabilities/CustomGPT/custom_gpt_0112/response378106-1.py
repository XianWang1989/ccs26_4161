
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current position
        self.f.seek(0)  # Move to the start of the file
        lc = 0  # Line counter

        # Iterate through the file while keeping track of the lines
        for line in self.f:
            if t >= len(line):  # Check if the position is within the line length
                t -= len(line)  # Decrease t by the length of the line
                lc += 1  # Increment line counter
            else:
                break  # Stop if the line is too long

        self.f.seek(t)  # Restore the file pointer to the original position

        # Return based on char flag
        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()  # Ensure file is closed when object is deleted

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Current line count: {line_count}')
