
try:
    f = open('file.txt', 'r')
    # Read from file
except FileNotFoundError as e:
    print(f"File not found: {e}")
else:
    print("File read successfully!")
finally:
    print("Cleaning up resources.")
    f.close()  # Ensure the file is closed
