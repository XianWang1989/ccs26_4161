
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()

        # Reset the file pointer to the beginning
        self.f.seek(0)

        # Read all lines into a list without affecting the file pointer
        lines = self.f.readlines()

        # Calculate the line count and position
        lc = 0
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return the line count and possibly the character position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell(char=True))  # Outputs: (line_count, char_position)
editor.close()
