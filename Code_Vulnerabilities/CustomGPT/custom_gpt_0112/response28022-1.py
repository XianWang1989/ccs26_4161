
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    # Define functions for each case
    def case1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case2():
        return postmarket(user, tval)

    def case3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    # Create a dictionary of cases
    result = {
        1: case1,
        2: case2,
        3: case3
    }

    # Call the appropriate function
    return result.get(i, lambda: "Invalid case")()  # Default to a lambda for invalid case
