
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names from the LIST output
    b = [line.split()[-1] for line in b]  # This assumes the last item is the directory name

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask the user if the directory doesn't exist
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item is a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask if it's a directory

# Call your function
path_sel()
file_dl()
