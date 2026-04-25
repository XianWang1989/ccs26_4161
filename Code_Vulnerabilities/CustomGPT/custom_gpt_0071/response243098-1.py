
def path_sel():
    path = raw_input("Select desired working directory: ").strip()
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the entries in b to avoid format issues
    b = [line.split()[-1] for line in b]  # Assuming the last element is the directory name

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Ask again if the directory is not found
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check for directories in the output
            path_sel()  # Re-prompt if there's a directory

file_dl()
