
def postback(i, user, tval):
    """Posts a response based on the input; the message must be less than 140 characters"""

    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Execute the function if it exists
    func = result.get(i)
    if func:
        return func()  # Call the stored lambda function
    else:
        return None  # Handle the case where 'i' is not found

# Example usage:
# postback(1, 'username', 'some_value')
