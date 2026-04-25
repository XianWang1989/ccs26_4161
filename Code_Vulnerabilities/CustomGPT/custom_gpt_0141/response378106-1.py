
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        position = self.f.tell()

        # Go to the beginning of the file and initialize line counter
        self.f.seek(0)
        lc = 0  # line counter

        # Iterate through the file to count lines
        for line in self.f:
            if position >= len(line):
                position -= len(line)
                lc += 1
            else:
                break

        # Restore original position
        self.f.seek(position + sum(len(line) for line in open(self.file, 'r')[:lc]))

        if char:
            return lc, position
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')

# Call the tell method to determine the current line
line_count = file_editor.tell()
print(f"Current line count: {line_count}")

file_editor.close()
