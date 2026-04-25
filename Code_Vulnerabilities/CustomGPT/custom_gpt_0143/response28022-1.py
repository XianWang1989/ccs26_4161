
def postback(i, user, tval):
    """Function that posts a response based on the case; the message string should be less than 140 characters."""
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    selected_case = result.get(i)
    if selected_case:
        return selected_case()  # Call the function stored in the dictionary
    else:
        return None  # Handle invalid case
