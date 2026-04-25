
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize both the input path and the listed directories for comparison
    if path not in [dir.split()[-1] for dir in b]:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Re-ask for a directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if there's a directory in the listing
        if any('d' in line for line in c):
            return path_sel()  # Recursive call if a directory exists

    file_dl()  # Call to download files at the end

# Assuming ftp is already defined and logged in somewhere above
