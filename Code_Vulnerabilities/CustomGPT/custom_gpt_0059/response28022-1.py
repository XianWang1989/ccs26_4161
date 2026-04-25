
def postback(i, user, tval):
    """Function that posts a response to the database; the message string must be less than 140 characters."""

    # Define the functions to be called based on the case
    def case_1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case_2():
        return postmarket(user, tval)

    def case_3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    # Create a dictionary with callable functions
    result = {
        1: case_1,
        2: case_2,
        3: case_3
    }

    # Call the function associated with the provided case
    return result.get(i, lambda: None)()  # returns None if i is not in the dictionary
