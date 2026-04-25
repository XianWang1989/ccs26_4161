
def postback(i, user, tval):
    """Function that handles a response based on the case number."""

    def case_1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case_2():
        return postmarket(user, tval)

    def case_3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    result = {
        1: case_1,
        2: case_2,
        3: case_3
    }

    # Call the function assigned to the case if it exists
    return result.get(i, lambda: None)()  # Default to a no-op if case not found

# Example usage:
# postback(1, 'username', 'some_value')
