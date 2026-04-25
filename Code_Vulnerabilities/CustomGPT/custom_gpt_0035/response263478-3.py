
row = [10, 20, 30, 40, 50]

# Example calls
result1 = foo(row, func1, a=1, b=2)                          # Returns 3
result2 = foo(row, func2, x=5, static=10)                  # Returns 15
result3 = foo(row, func3, item1='spam', item2='eggs')      # Returns 'spam and eggs'
result4 = foo(row, 2)                                       # Returns 30
result5 = foo(row, 'Hello, World')                          # Returns 'Hello, World'

print(result1, result2, result3, result4, result5)
