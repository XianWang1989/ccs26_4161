
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("The result is:", result)
finally:
    print("This block always executes, regardless of whether an error occurred or not.")
