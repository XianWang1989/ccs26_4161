
def postback(i, user, tval):
    """Function that posts responses to the database; the message string must be less than 140 characters."""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Call the function corresponding to the given index i
    func = result.get(i)
    if func:
        return func()  # Execute the function if it exists
    else:
        return None  # Handle cases where i is not in the dictionary

# Example usage
# Assuming appropriate user and tval are provided
response = postback(1, "user123", "sour cream")
