
def postback(i, user, tval):
    """Function that posts a response to the database; message string must be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }
    return result.get(i, lambda: None)()  # Call the function (or return None if i is invalid)

# Example usage:
# Assuming you have valid `user` and `tval` variables
response = postback(1, user, tval)  # This will execute the first case
