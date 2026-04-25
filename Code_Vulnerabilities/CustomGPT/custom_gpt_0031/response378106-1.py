
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_pos = self.f.tell()
        # Seek to the beginning to read lines
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # Line count
        t = current_pos  # Start with the current position

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the original position
        self.f.seek(current_pos)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
line_count = file_editor.tell()
print(f"Line count: {line_count}")
file_editor.close()
