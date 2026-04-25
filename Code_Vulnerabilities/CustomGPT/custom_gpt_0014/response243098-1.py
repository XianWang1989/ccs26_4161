
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Use return to handle recursion properly
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            return path_sel()  # Same return behavior here

# Example usage
path_sel()
file_dl()
