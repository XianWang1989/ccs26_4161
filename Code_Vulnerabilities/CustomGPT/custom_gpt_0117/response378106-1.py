
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()

        # Move to the start of the file and read all lines
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0
        t = current_position

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the file pointer to its original position
        self.f.seek(current_position)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    print(editor.tell())  # Output the line count based on current position
