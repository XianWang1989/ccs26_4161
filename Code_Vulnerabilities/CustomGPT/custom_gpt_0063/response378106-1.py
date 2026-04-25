
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get current byte offset
        t = self.f.tell()

        # Go back to the start of the file
        self.f.seek(0)

        # Read all lines into memory
        lines = self.f.readlines()

        # Determine the line and character position
        lc = 0
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return based on the char parameter
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('test.txt')
editor.f.write("Hello World!\nThis is a test.\nAnother line.\n")
editor.f.flush()  # Ensure the content is written before calling tell()
print(editor.tell())  # Should return the line number
editor.f.seek(0)  # Reset to the start before closing
editor.close()
