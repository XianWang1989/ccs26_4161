
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current byte position
        self.f.seek(0)     # Move to the beginning of the file
        lc = 0  # Line count

        # Read the file line by line
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break

            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        self.f.seek(t)  # Optionally set back to the original position

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    print(editor.tell())  # Get the line number of the current position
