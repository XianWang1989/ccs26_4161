
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current byte position
        t = self.f.tell()
        # Move the cursor to the beginning of the file
        self.f.seek(0)
        # Read all lines into a list
        lines = self.f.readlines()
        lc = 0

        # Iterate through lines to find the line number and character offset
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Close the file after reading
        self.f.close()

        if char:
            return lc, t
        return lc

# Example usage:
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Current line: {line_count}')
