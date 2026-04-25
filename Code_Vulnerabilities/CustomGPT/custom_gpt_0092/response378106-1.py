
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get current position
        t = self.f.tell()
        lc = 0
        current_pos = 0

        # Reset and read through the file
        self.f.seek(0)
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break
            next_pos = current_pos + len(line)
            if t < next_pos:  # Found the line containing the position
                break
            lc += 1
            current_pos = next_pos

        if char:
            return lc, t - current_pos
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Output the current line number
editor.close()
