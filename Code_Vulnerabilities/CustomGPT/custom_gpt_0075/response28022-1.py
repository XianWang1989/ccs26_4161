
def postback(i, user, tval):
    """Function to post responses based on user input."""

    def ask_brand():
        return api.PostDirectMessage(user, 'Trebuie sa-mi spui si marca pe care o cauti')

    def handle_market():
        return postmarket(user, tval)

    def unknown_sour_creams():
        return api.PostDirectMessage(user, 'Imi pare rau, dar nu stiu unde poti gasi aceste tipuri de smantana: %s' % tval)

    # Create a dictionary to map case values to functions
    actions = {
        1: ask_brand,
        2: handle_market,
        3: unknown_sour_creams
    }

    # Call the function based on i, or return None if i is not found
    return actions.get(i, lambda: None)()

# Example usage:
result = postback(1, 'User123', None)
print(result)
