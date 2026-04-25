
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in item for item in c):  # Check if any item contains 'd'
            return path_sel()  # Return to allow another selection
        else:
            print("No subdirectory found, proceeding.")

# Call the function to start the process
path_sel()
