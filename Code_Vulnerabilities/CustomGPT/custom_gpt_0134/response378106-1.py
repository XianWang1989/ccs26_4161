
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        # Open the file as 'a+' (append + read)
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position in bytes
        t = self.f.tell()
        # Read all lines from the file
        self.f.seek(0)
        lines = self.f.readlines()
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example of usage
editor = FileEditor('example.txt')
print(editor.tell())  # Returns the line count based on current file position
editor.close()
