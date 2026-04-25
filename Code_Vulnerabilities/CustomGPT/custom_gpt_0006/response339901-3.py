
try:
    value = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("This will always run, even if there was an error.")
