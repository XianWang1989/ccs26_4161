
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception:
    e = "An unexpected error occurred."
    print(e)
