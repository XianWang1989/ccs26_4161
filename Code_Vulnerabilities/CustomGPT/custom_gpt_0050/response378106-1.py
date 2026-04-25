
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        t = self.f.tell()
        # Move to the start of the file to read lines
        self.f.seek(0)
        lines = self.f.readlines()  # Read all lines at once
        lc = 0  # Line counter

        # Calculate the line number and character offset
        for line in lines:
            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        # Return the result
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
print(file_editor.tell())  # Get the current line position
file_editor.close()
