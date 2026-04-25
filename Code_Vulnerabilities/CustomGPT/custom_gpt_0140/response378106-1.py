
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_pos = self.f.tell()

        # Go to the start of the file
        self.f.seek(0)

        # Read lines and count
        lines = self.f.readlines()
        lc = 0
        t = current_pos

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore original position
        self.f.seek(current_pos)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get the line count based on current position
editor.close()
