
def path_sel():
    while True:  # Using a loop instead of recursion
        path = input("Select desired working directory: ")  # Updated to use input() for Python 3
        b = []
        ftp.retrlines('LIST', b.append)

        # Create a list of directory names from the entries in b
        directories = [line.split()[-1] for line in b if line.startswith('d')]

        if path not in directories:
            print("ERROR- Directory does not exist.\n")
        else:
            print('\nChanging to ' + path, '\n')
            ftp.cwd(path)
            print(path)
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                continue  # If the first line of c indicates a directory, the loop will re-prompt

            break  # Exit the loop if the selected path is valid

file_dl()
