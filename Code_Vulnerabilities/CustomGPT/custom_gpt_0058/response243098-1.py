
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        # Strip the line to avoid issues with extra spaces
        b = [line.strip() for line in b]

        if path not in b:
            print "ERROR- Directory does not exist.\n"
        else:
            print '\nChanging to ' + path, '\n'
            ftp.cwd(path)
            print path
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)

            # Ensure that you check the correct format
            if 'd' in str(c[0]):  # This may need further refinement
                continue  # Re-ask for the directory if it meets this condition
            break  # Exit loop if everything is okay

file_dl()
