
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Adding .strip() to clean any extra spaces
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names in the list by stripping whitespace if necessary
    b = [item.strip() for item in b]

    if path not in b:
        print "ERROR - Directory does not exist.\n"
        path_sel()  # Re-prompt for the directory
    else:
        print '\nChanging to ' + path + '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Ensure 'd' in c is checked correctly
        if any('d' in item for item in c):
            print "Found a directory in the list. Prompting for path again."
            path_sel()  # If a directory is discovered, prompt again
        else:
            print "No directories found, proceeding with download."
            file_dl()  # Proceed with file downloading
