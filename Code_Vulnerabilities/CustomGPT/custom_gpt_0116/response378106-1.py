
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the original position
        original_position = self.f.tell()
        self.f.seek(0)  # Go back to the start of the file

        # Read all lines first
        lines = self.f.readlines()

        # Calculate line count and remaining position
        lc = 0
        t = original_position

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore original position
        self.f.seek(original_position)

        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()  # Get the line count
print(f'The current line count is: {line_count}')
