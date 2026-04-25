
try:
    file = open('example.txt', 'r')
    data = file.read()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
finally:
    file.close()  # This will execute regardless of success or failure
    print("File is now closed.")
