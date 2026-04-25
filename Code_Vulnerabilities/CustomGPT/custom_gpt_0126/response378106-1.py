
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get current position
        self.f.seek(0)  # Go to the start of the file
        lines = self.f.readlines()  # Read all lines into a list

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)  # Subtract line length from position
                lc += 1  # Increment line count
            else:
                break  # Stop if the current position is within the line

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
print(file_editor.tell())  # Gets the line position
file_editor.close()
