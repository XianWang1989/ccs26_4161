
def get_name(a, b, c):
    state = (a, b, c)
    names = {
        (True, True, True): 'first',
        (True, True, False): 'second',
        (True, False, True): 'third',
        (True, False, False): 'fourth',
        (False, True, True): 'fifth',
        (False, True, False): 'sixth',
        (False, False, True): 'seventh',
        (False, False, False): 'eighth'
    }
    return names[state]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: third
