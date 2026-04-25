
def postback(i, user, tval):
    """Posts a response based on the case number."""

    # Define the actions as functions
    def case1():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def case2():
        return postmarket(user, tval)

    def case3():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    # Use a dictionary to map case numbers to functions
    result = {
        1: case1,
        2: case2,
        3: case3
    }

    # Call the function associated with the case number
    return result.get(i, lambda: "Invalid case")()

# Example usage
response = postback(2, 'User123', 'sour cream')
print(response)
