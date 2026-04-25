
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def __del__(self):
        self.f.close()

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()

        # Go to the start of the file and read lines
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # Line count
        remaining = t  # Remaining bytes to account for

        # Calculate the line number and position
        for line in lines:
            line_length = len(line)
            if remaining >= line_length:
                remaining -= line_length
                lc += 1
            else:
                break

        # Return the count of lines and remaining byte position if requested
        if char:
            return lc, remaining
        return lc

# Example usage
if __name__ == "__main__":
    editor = FileEditor("example.txt")
    line_count = editor.tell()
    print(f"Current line number is: {line_count}")
