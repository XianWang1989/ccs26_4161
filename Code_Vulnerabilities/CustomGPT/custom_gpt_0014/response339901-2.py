
try:
    # Trying to open a file that doesn't exist
    with open("non_existent_file.txt", "r") as f:
        data = f.read()
except Exception as e:
    print(f"An error occurred: {e}")  # Captures and prints the exception message
else:
    print("File read successfully!")
finally:
    print("Execution complete.")  # This will always run
