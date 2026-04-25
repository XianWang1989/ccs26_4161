
def postback(i, user, tval):
    """Function that posts a response based on the case passed."""
    result_cases = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the function corresponding to the case, and call it if exists
    result = result_cases.get(i)
    return result() if result else None

# Usage example
response = postback(2, 'some_user', 'some_val')
print(response)
