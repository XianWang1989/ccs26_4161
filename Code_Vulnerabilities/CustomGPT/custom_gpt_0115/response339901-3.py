
try:
    x = 1 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors occurred!")
finally:
    print("This block runs no matter what.")
