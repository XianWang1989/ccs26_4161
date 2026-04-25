
try:
    x = 10 / 0
except Exception:
    e = Exception("An error occurred")
    print(e)  # This will print "An error occurred"
