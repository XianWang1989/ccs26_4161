
try:
    f = open('file.txt')
    # Some operations with the file
except Exception as e:
    print("An error occurred:", e)
else:
    print("File operations were successful.")
finally:
    f.close()  # Ensures the file is closed whether an error occurred or not.
