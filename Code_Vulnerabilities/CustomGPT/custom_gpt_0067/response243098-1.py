
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Normalize entries for comparison
        b = [entry.split()[-1] for entry in b]  # Get last part which is the directory name

        if path not in b:
            print "ERROR - Directory does not exist.\n"
        else:
            print '\nChanging to ' + path + '\n'
            ftp.cwd(path)
            print path
            # Recheck the directory after changing
            c = []
            ftp.retrlines('LIST', c.append)
            if any('d' in str(entry) for entry in c):  # Check if it's a directory
                continue  # If it is a directory, prompt again

            break  # Exit loop if valid directory found

    file_dl()
