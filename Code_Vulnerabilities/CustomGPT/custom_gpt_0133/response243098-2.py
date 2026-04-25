
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print("ERROR - Directory does not exist.\n")
            continue  # Go back to the start of the loop

        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            continue  # If it's a directory, prompt for another path

        break  # Only exit if we have a valid path

# Call the file download function after the path selection
selected_path = path_sel()
file_dl(selected_path)
