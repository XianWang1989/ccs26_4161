
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in line for line in c):  # Check if 'd' exists in any line
            return path_sel()  # Return if another directory needs to be selected

    return path  # Return the valid path


# Then, call file_dl() after ensuring the path is valid.
valid_path = path_sel()
file_dl(valid_path)
