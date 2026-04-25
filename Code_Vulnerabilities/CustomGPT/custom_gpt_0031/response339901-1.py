
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except Exception as e:
    print("An error occurred:", e)
else:
    print("The result is:", result)
finally:
    print("Execution complete.")
