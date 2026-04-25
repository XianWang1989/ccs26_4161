
try:
    file = open("example.txt", "r")
    data = file.read()
    x = 1 / 0  # This will raise an exception
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred. Data:", data)
finally:
    print("This will always execute.")
    file.close()  # Ensure the file is closed
