
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean up the entries in 'b' to match your 'path'
    b = [entry.split()[-1] for entry in b]  # Get the last part of the string which is typically the directory name

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask the user for a directory
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()  # If still a directory, ask for directory again

file_dl()
