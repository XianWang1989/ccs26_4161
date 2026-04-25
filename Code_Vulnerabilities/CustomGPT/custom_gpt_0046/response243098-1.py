
def path_sel():
    path = input("Select desired working directory: ").strip()
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean the list entries
    b = [entry.split()[-1] for entry in b]

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        c = []
        ftp.retrlines('LIST', c.append)
        c = [entry.split()[-1] for entry in c]  # Clean the list entries

        if 'd' in str(c[0]):
            path_sel()  # If it's a directory, re-ask

# Call the file download function
file_dl()
