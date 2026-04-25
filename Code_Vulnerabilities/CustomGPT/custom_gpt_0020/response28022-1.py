
def postback(i, user, tval):
    """Function that posts a response to the database; 
    the message string must be less than 140 characters."""

    # Store functions (callables) in the dictionary instead of their return values
    result = {
        1: lambda: api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti'),
        2: lambda: postmarket(user, tval),
        3: lambda: api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)
    }

    # Get the callable function based on `i`, then invoke it
    return result.get(i, lambda: "Invalid option!")()  # Return a default message for invalid options

# Example of how to call the function
# postback(1, 'user123', 'some value')
# postback(2, 'user123', 'some value')
# postback(3, 'user123', 'some value')
