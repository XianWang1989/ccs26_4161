
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors occurred, result is:", result)
finally:
    print("This block executes no matter what.")
