
try:
    f = open('file.txt', 'r')
    # Do something with the file
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
finally:
    f.close()  # This will always execute
