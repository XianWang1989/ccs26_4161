
try:
    # Some risky operation
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception:
    e = "An error occurred"  # Custom message
    print(e)
