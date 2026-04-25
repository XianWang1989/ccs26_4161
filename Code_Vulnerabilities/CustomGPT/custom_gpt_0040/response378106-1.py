
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()

        # Seek to the start to read lines
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        # Calculate line count and position
        lc = 0
        for line in lines:
            if current_position >= len(line):
                current_position -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, current_position
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Prints the line count at current position
editor.close()
