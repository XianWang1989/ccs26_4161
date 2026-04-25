
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current position
        self.f.seek(0)     # Move to the start of the file
        lines = self.f.readlines()  # Read all lines into memory

        lc = 0
        for line in lines:
            if t >= len(line):  # Check if position is within the line
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t + sum(len(l) for l in lines[:lc]))  # Reset back to the original position
        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Current line position: {line_count}")
