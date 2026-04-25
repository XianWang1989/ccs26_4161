
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()
        # Move to the start to read the file
        self.f.seek(0)
        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0
        t = current_position

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore original position
        self.f.seek(current_position)

        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_number = editor.tell()  # Get the current line number
print(f"Current line number: {line_number}")
