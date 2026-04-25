
try:
    file = open("example.txt", "w")
    # Simulating an error
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred, doing something with the file.")
finally:
    file.close()  # This will always run
    print("File closed.")
