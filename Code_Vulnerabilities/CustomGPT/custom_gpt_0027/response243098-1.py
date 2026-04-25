
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory list for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):  # Check if first entry is a directory
            return path_sel()  # Return instead of calling directly

# Ensure this function is called in the right context
file_dl()
