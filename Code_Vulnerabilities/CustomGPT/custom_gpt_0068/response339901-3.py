
try:
    file = open("non_existent_file.txt", "r")  # This will raise a FileNotFoundError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
finally:
    print("Executing cleanup code.")  # Always runs
