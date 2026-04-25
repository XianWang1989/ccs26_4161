
try:
    x = 1 / 0
except Exception:
    e = Exception("A division error occurred")  # You cannot directly assign like this.
    print(e)
