
try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
else:
    print("The result is:", result)
finally:
    print("This block always executes. Cleanup actions can be done here.")
