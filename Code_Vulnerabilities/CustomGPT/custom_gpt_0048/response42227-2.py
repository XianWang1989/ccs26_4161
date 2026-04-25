
# Define a function to get the name based on boolean values
def get_name(a, b, c):
    return {
        (True, True, True): 'first',
        (True, True, False): 'second',
        (True, False, True): 'third',
        (True, False, False): 'fourth',
        (False, True, True): 'fifth',
        (False, True, False): 'sixth',
        (False, False, True): 'seventh',
        (False, False, False): 'eighth',
    }[(a, b, c)]

# Example usage
a = True
b = False
c = True
name = get_name(a, b, c)

print(name)
