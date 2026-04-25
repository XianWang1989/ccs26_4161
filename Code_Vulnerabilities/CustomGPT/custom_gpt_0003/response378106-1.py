
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save current position
        t = self.f.tell()
        self.f.seek(0)  # Move the file pointer to the beginning

        # Read all lines into a list
        lines = self.f.readlines()  
        lc = 0  # Line count

        # Calculate the line and character within the line
        for line in lines:
            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        # Return the appropriate information
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
file_editor = FileEditor('example.txt')
try:
    print(file_editor.tell())  # Output the line number
except OSError as e:
    print(f"An error occurred: {e}")
finally:
    file_editor.close()
