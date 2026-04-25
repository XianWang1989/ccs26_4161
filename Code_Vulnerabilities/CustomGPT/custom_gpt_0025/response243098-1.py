
def path_sel(ftp):
    # Prompt user for directory input
    path = input("Select desired working directory: ")

    # List to store directory names
    directory_list = []
    ftp.retrlines('LIST', directory_list.append)

    # Check if path exists in the directory list
    if path not in directory_list:
        print("ERROR - Directory does not exist.\n")
        return path_sel(ftp)  # Re-ask for the directory if not found
    else:
        print(f'\nChanging to {path}\n')
        ftp.cwd(path)  # Change to the specified directory
        print(path)

        # Check for subdirectories
        subdir_list = []
        ftp.retrlines('LIST', subdir_list.append)
        if any('d' in line for line in subdir_list):  # Check for directories
            return path_sel(ftp)  # Re-ask if a directory exists

    file_dl()  # Proceed to download files

