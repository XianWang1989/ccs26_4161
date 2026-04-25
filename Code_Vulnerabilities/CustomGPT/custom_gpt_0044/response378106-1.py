
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Current position
        self.f.seek(0)  # Move to the start of the file
        lc = 0  # Line count
        total_length = 0  # Total bytes read

        # Read the file line by line
        for line in self.f:
            line_length = len(line)
            if total_length + line_length > t:
                break
            total_length += line_length
            lc += 1

        self.f.seek(t)  # Restore the initial position

        if char:
            return lc, t - total_length
        return lc

    def close(self):
        self.f.close()

# Usage example
editor = FileEditor('testfile.txt')
print(editor.tell())  # Returns the number of lines before the current position
editor.close()
